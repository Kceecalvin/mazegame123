import pygame
import math
import time
from collections import deque
import numpy as np
import random 

class Snake:
    def __init__(self, start_x, start_y, maze, start_delay=10000, color=(50, 205, 50)):
        self.start_x = start_x
        self.start_y = start_y
        self.x = float(start_x)
        self.y = float(start_y)
        self.color = color 
        self.maze = maze
        self.height, self.width = maze.shape

        # Movement control
        self.update_frequency = 12 
        self.last_update_time = time.time()
        self.update_interval = self.update_frequency / 60.0 
        
        # NEW: Smartness factor (0.0 = pure random, 1.0 = pure shortest path, 
        # typically kept low, e.g., 0.1 - 0.5)
        self.bias_factor = 0.0

        # State
        self.is_active = False
        self.start_delay = start_delay # Time in milliseconds before the snake starts moving
        self.activation_time = pygame.time.get_ticks() + start_delay 
        self.moving = False
        
        # Animation targets
        self.target_x = self.x
        self.target_y = self.y
        self.move_start_time = 0
        self.move_duration = self.update_interval 

    def _animate_move(self):
        """Updates the snake's position during smooth movement."""
        elapsed = time.time() - self.move_start_time
        progress = min(1.0, elapsed / self.move_duration)
        
        # Interpolate position
        start_x, start_y = (self.x, self.y)
        
        self.x = start_x + (self.target_x - start_x) * progress
        self.y = start_y + (self.target_y - start_y) * progress
        
        if progress >= 1.0:
            self.moving = False
            # Snap to the exact grid cell position
            self.x = self.target_x
            self.y = self.target_y
            self.move_start_time = 0


    def _get_valid_moves(self, curr_x, curr_y):
        """Finds all valid adjacent path cells the snake can move to."""
        valid_moves = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = curr_x + dx, curr_y + dy
            
            # Check bounds and if it's a path (0)
            if (0 <= next_x < self.width and 0 <= next_y < self.height and 
                self.maze[next_y][next_x] == 0):
                valid_moves.append((next_x, next_y))
        return valid_moves
    
    
    def _calculate_distance(self, x1, y1, x2, y2):
        """Simple Manhattan distance for heuristic check."""
        return abs(x1 - x2) + abs(y1 - y2)

    
    def _choose_biased_move(self, curr_x, curr_y, player_x, player_y):
        """
        Chooses a next cell using Biased Random Walk.
        Moves that decrease distance to the player are prioritized.
        """
        valid_moves = self._get_valid_moves(curr_x, curr_y)
        
        if not valid_moves:
            return None, None

        current_dist = self._calculate_distance(curr_x, curr_y, player_x, player_y)
        
        # Assign weights based on distance change
        moves_with_weights = []
        base_weight = 1.0 

        for move_x, move_y in valid_moves:
            new_dist = self._calculate_distance(move_x, move_y, player_x, player_y)
            
            weight = base_weight
            
            if new_dist < current_dist:
                # Move brings the snake CLOSER to the player (Good move)
                weight += self.bias_factor
            elif new_dist > current_dist:
                # Move takes the snake FARTHER from the player (Bad move)
                weight -= (self.bias_factor / 2) # Reduce weight slightly
            # If distance is the same, weight remains base_weight
            
            # Ensure weight is not negative
            weight = max(0.1, weight)
            
            moves_with_weights.append(((move_x, move_y), weight))

        # Separate moves and weights for random.choices
        moves = [move for move, weight in moves_with_weights]
        weights = [weight for move, weight in moves_with_weights]
        
        # Select one move based on the calculated weights
        chosen_move = random.choices(moves, weights=weights, k=1)[0]
        return chosen_move


    def update(self, player_x, player_y):
        """Main update loop: checks activation, randomly moves with bias."""
        
        if not self.is_active:
            # Check if delay period is over 
            if pygame.time.get_ticks() >= self.activation_time:
                self.is_active = True
            else:
                return # Snake is not yet active

        # Handle animation if currently moving
        if self.moving:
            self._animate_move()
            return
        
        # --- Biased Wandering Movement Logic ---
        current_time = time.time()
        
        # Check if it's time for the snake to make a new grid move
        if current_time - self.last_update_time >= self.update_interval:
            self.last_update_time = current_time

            current_grid_x = int(round(self.x))
            current_grid_y = int(round(self.y))
            
            #  CHANGED: Use the new biased selection method
            next_x, next_y = self._choose_biased_move(current_grid_x, current_grid_y, player_x, player_y)
            
            if next_x is not None:
                # Set target for smooth animation
                self.target_x = float(next_x)
                self.target_y = float(next_y)
                self.move_start_time = current_time
                self.moving = True
            
            # If no valid move, the snake stays put.


    def check_collision(self, player_x, player_y):
        """Checks if the snake's current grid position matches the player's current grid position."""
        if not self.is_active:
            return False
            
        snake_grid_x = int(round(self.x))
        snake_grid_y = int(round(self.y))
        player_grid_x = int(round(player_x))
        player_grid_y = int(round(player_y))

        return snake_grid_x == player_grid_x and snake_grid_y == player_grid_y