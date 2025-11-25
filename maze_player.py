import pygame
import math
import time

class Player:
    def __init__(self, start_x, start_y, color=(65, 105, 225)):
        self.start_x = start_x
        self.start_y = start_y
        self.x = float(start_x)
        self.y = float(start_y)
        self.color = color
        self.moves_count = 0
        
        # Smooth movement state
        self.moving = False
        self.target_x = float(start_x)
        self.target_y = float(start_y)
        self.move_start_time = 0
        self.move_duration = 0.15 # seconds for one tile move

        # Game timing
        self.level_start_time = 0
        self.level_complete_time = 0 # Used to pause time on win

    def reset(self, new_start_x, new_start_y):
        self.start_x = new_start_x
        self.start_y = new_start_y
        self.x = float(new_start_x)
        self.y = float(new_start_y)
        self.moves_count = 0
        self.moving = False
        self.target_x = float(new_start_x)
        self.target_y = float(new_start_y)
        self.level_start_time = 0
        self.level_complete_time = 0

    def set_target(self, new_target_x, new_target_y):
        """Starts a movement animation to a new grid cell."""
        self.target_x = float(new_target_x)
        self.target_y = float(new_target_y)
        self.move_start_time = time.time()
        self.moving = True
        self.moves_count += 1

    def update(self, snake_distance):
        """Updates the player's position during movement."""
        if self.moving:
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

    def get_level_time(self):
        """Returns the elapsed time for the current level in seconds."""
        if self.level_start_time == 0:
            return 0
        
        current_time_ms = pygame.time.get_ticks()
        start_time_ms = self.level_start_time
        
        if self.level_complete_time > 0:
            # Game is complete, use the recorded end time
            return (self.level_complete_time - start_time_ms) / 1000
        
        # Game is still running
        return (current_time_ms - start_time_ms) / 1000