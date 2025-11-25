import pygame
import numpy as np
import math
import time

class MazeVisualizer:
    def __init__(self, cell_size=25, margin=1):
        pygame.init()
        self.cell_size = cell_size
        self.margin = margin
        self.screen = None
        self.clock = pygame.time.Clock()
        
        # Colors (Defined globally for a consistent look)
        self.WALL_COLOR = (50, 50, 50)
        self.PATH_COLOR = (240, 240, 245)
        self.START_COLOR = (144, 238, 144) # Light Green
        self.END_COLOR = (255, 99, 71)    # Tomato Red
        self.ACCENT_COLOR = (65, 105, 225) # Royal Blue
        self.TEXT_COLOR = (30, 30, 30)
        self.TEXT_LIGHT_COLOR = (100, 100, 100)
        
        # Fonts
        self.font = pygame.font.Font(None, 24)
        self.bold_font = pygame.font.Font(None, 28)
        self.title_font = pygame.font.Font(None, 64)
        
        # UI Rects (for button handling in main.py)
        self.hint_button_rect = None 

    def init_pygame(self, maze_width, maze_height):
        """Initializes or re-initializes the Pygame window based on maze size."""
        self.maze_pixel_width = maze_width * (self.cell_size + self.margin) + self.margin
        self.maze_pixel_height = maze_height * (self.cell_size + self.margin) + self.margin
        
        # Determine total window size
        ui_panel_width = 250
        total_width = self.maze_pixel_width + ui_panel_width
        total_height = max(self.maze_pixel_height, 600) 
        
        self.screen = pygame.display.set_mode((total_width, total_height))
        pygame.display.set_caption("Chase the Exit")
        
        # Calculate maze offset to center it vertically
        self.offset_y = (total_height - self.maze_pixel_height) // 2
        self.offset_x = 0
        self.ui_x = self.maze_pixel_width


    def draw_maze_game(self, maze, player, snake, show_hint, hint_path):
        """Draws the main game screen (maze, player, snake, and UI background)."""
        self.screen.fill(self.WALL_COLOR) # Fill background with wall color

        # Draw the maze cells
        for y in range(maze.shape[0]):
            for x in range(maze.shape[1]):
                cell_rect = self._get_cell_rect(x, y)
                
                # Check for Start/End
                color = self.PATH_COLOR
                if x == 0 and y == 1: # Start
                    color = self.START_COLOR
                elif x == maze.shape[1] - 1 and y == maze.shape[0] - 2: # End
                    color = self.END_COLOR
                elif maze[y, x] == 0:
                    color = self.PATH_COLOR
                else:
                    color = self.WALL_COLOR
                
                pygame.draw.rect(self.screen, color, cell_rect)
                
        # Draw hint path if enabled
        if show_hint and hint_path:
            for i, (hx, hy) in enumerate(hint_path):
                if i > 0 and (hx, hy) != (player.target_x, player.target_y): # Don't draw on player's current target
                    cell_rect = self._get_cell_rect(hx, hy)
                    center = cell_rect.center
                    # Fade the path
                    hint_color = (255, 215, 0)
                    pygame.draw.circle(self.screen, hint_color, center, self.cell_size // 4)

        return maze.shape[1], maze.shape[0] # Return width/height for UI

    def _get_cell_rect(self, x, y):
        """Helper to get the pixel rectangle for a grid cell."""
        x_pos = self.offset_x + self.margin + x * (self.cell_size + self.margin)
        y_pos = self.offset_y + self.margin + y * (self.cell_size + self.margin)
        return pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)

    def draw_player(self, player, maze_width):
        """Draws the Player."""
        # Calculate interpolated position
        interp_x = player.x * (self.cell_size + self.margin) + self.margin + self.offset_x
        interp_y = player.y * (self.cell_size + self.margin) + self.margin + self.offset_y
        
        # Draw a circle for the player
        center = (interp_x + self.cell_size // 2, interp_y + self.cell_size // 2)
        radius = self.cell_size // 2 - 2
        
        pygame.draw.circle(self.screen, player.color, center, radius)
        # Highlight for better visibility
        pygame.draw.circle(self.screen, (255, 255, 255), center, radius // 2)


    def draw_snake(self, snake, maze_width):
        """Draws the Snake."""
        if not snake.is_active and snake.start_delay > 0 and not snake.activation_time < pygame.time.get_ticks():
            # Draw a 'Zzz' icon when completely inactive/sleeping (before first move)
            if not getattr(self, 'game_started_flag', False): # Check if game hasn't started
                text = self.bold_font.render("Zzz", True, (0, 150, 0))
                self.screen.blit(text, (self.offset_x + self.margin*2, self.offset_y + self.cell_size + self.margin*2))
            return

        interp_x = snake.x * (self.cell_size + self.margin) + self.margin + self.offset_x
        interp_y = snake.y * (self.cell_size + self.margin) + self.margin + self.offset_y
        
        rect = pygame.Rect(interp_x, interp_y, self.cell_size, self.cell_size)
        
        # Draw a stylized snake head (square with rounded corners)
        pygame.draw.rect(self.screen, snake.color, rect, border_radius=4)
        
        # Eyes
        eye_color = (255, 255, 255)
        pupil_color = (255, 0, 0)
        eye_size = self.cell_size // 6
        
        pygame.draw.circle(self.screen, eye_color, (rect.x + self.cell_size//3, rect.y + self.cell_size//3), eye_size)
        pygame.draw.circle(self.screen, pupil_color, (rect.x + self.cell_size//3, rect.y + self.cell_size//3), eye_size // 2)
        
        pygame.draw.circle(self.screen, eye_color, (rect.x + 2*self.cell_size//3, rect.y + self.cell_size//3), eye_size)
        pygame.draw.circle(self.screen, pupil_color, (rect.x + 2*self.cell_size//3, rect.y + self.cell_size//3), eye_size // 2)


    def draw_button(self, text, rect, hover=False, color=None, text_color=(255, 255, 255)):
        """Helper function to draw a styled button."""
        if color is None:
            color = self.ACCENT_COLOR
        
        # Color change on hover for visual feedback
        if hover:
            color = (min(color[0] + 20, 255), min(color[1] + 20, 255), min(color[2] + 20, 255))
        
        # Draw shadow
        shadow_rect = rect.copy()
        shadow_rect.y += 3
        pygame.draw.rect(self.screen, (color[0]//2, color[1]//2, color[2]//2), shadow_rect, border_radius=10)
        
        # Draw main button
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        pygame.draw.rect(self.screen, (30, 30, 30), rect, 2, border_radius=10)
        
        text_surf = self.bold_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)
        
        return rect # return the button rect for click detection

    
    def draw_game_ui(self, level, moves, elapsed_time, snake_distance, snake, maze_width, maze_height, show_hint, game_started):
        """Draws the side UI panel with stats and buttons."""
        
        # Store game_started flag in visualizer for draw_snake access
        self.game_started_flag = game_started

        ui_rect = pygame.Rect(self.ui_x, 0, self.screen.get_width() - self.ui_x, self.screen.get_height())
        pygame.draw.rect(self.screen, (220, 220, 220), ui_rect)
        pygame.draw.line(self.screen, (150, 150, 150), (self.ui_x, 0), (self.ui_x, self.screen.get_height()), 2)
        
        # Title
      
        # Stats
        y_pos = 100
        stats = [
            (f"LEVEL:", f"{level}", self.TEXT_COLOR),
            (f"TIME:", f"{int(elapsed_time)}s", self.TEXT_COLOR),
            (f"MOVES:", f"{moves}", self.TEXT_COLOR)
        ]
        
        for label, value, color in stats:
            label_text = self.bold_font.render(label, True, self.TEXT_LIGHT_COLOR)
            value_text = self.bold_font.render(value, True, color)
            self.screen.blit(label_text, (self.ui_x + 20, y_pos))
            self.screen.blit(value_text, (self.ui_x + 230 - value_text.get_width(), y_pos))
            y_pos += 30
        
        y_pos += 20
        # Snake Status
        snake_label = self.bold_font.render("SNAKE STATUS", True, self.TEXT_COLOR)
        self.screen.blit(snake_label, (self.ui_x + 125 - snake_label.get_width()//2, y_pos))
        y_pos += 30

        if not game_started:
            # State 1: Game hasn't started (Pre-first move)
            status_text = self.bold_font.render("AWAITING MOVE", True, (0, 150, 0)) # Green text
            self.screen.blit(status_text, (self.ui_x + 125 - status_text.get_width()//2, y_pos))
            y_pos += 30
            
            delay_text = self.font.render("Delay: " + str(snake.start_delay // 1000) + "s (Starts on move)", True, self.TEXT_LIGHT_COLOR)
            self.screen.blit(delay_text, (self.ui_x + 125 - delay_text.get_width()//2, y_pos))
            y_pos += 30

        elif not snake.is_active:
            # State 2: Countdown Active (After first move, before activation time)
            delay_time_left = max(0, snake.activation_time - pygame.time.get_ticks()) / 1000
            
            if delay_time_left > 0:
                status_text = self.bold_font.render("ACTIVATING IN...", True, self.END_COLOR)
                self.screen.blit(status_text, (self.ui_x + 125 - status_text.get_width()//2, y_pos))
                y_pos += 30
                time_text = self.title_font.render(f"{delay_time_left:.1f}", True, self.END_COLOR)
                self.screen.blit(time_text, (self.ui_x + 125 - time_text.get_width()//2, y_pos))
                y_pos += 50
            else:
                # If time ran out, but logic hasn't updated snake.is_active yet, show WANDERING
                snake.is_active = True 
        
        if snake.is_active:
            # State 3: Snake is Active (Wandering)
            status_text = self.bold_font.render("WANDERING", True, self.END_COLOR)
            self.screen.blit(status_text, (self.ui_x + 125 - status_text.get_width()//2, y_pos))
            y_pos += 30
            
            # Snake pace information
            speed_text = self.font.render(f"Pace: {snake.update_frequency} frames/move", True, self.TEXT_LIGHT_COLOR)
            self.screen.blit(speed_text, (self.ui_x + 125 - speed_text.get_width()//2, y_pos))
            y_pos += 30
            
            time_text = self.font.render(f"Interval: {snake.update_interval:.2f}s", True, self.TEXT_LIGHT_COLOR)
            self.screen.blit(time_text, (self.ui_x + 125 - time_text.get_width()//2, y_pos))
            y_pos += 30

        y_pos += 40
        
        # Hint Button
        hint_hover = False
        if self.hint_button_rect:
            hint_hover = self.hint_button_rect.collidepoint(pygame.mouse.get_pos())

        hint_color = (255, 215, 0) if show_hint else (100, 100, 100)
        hint_text = "HINT: ON (H)" if show_hint else "HINT: OFF (H)"
        hint_button = pygame.Rect(self.ui_x + 25, y_pos, 200, 40)
        self.hint_button_rect = self.draw_button(hint_text, hint_button, hover=hint_hover, color=hint_color)
        
        y_pos += 50
        
        # Controls Button
        controls_button = pygame.Rect(self.ui_x + 25, y_pos, 200, 40)
        self.draw_button("Pause (P/ESC)", controls_button, hover=controls_button.collidepoint(pygame.mouse.get_pos()), color=(100, 100, 150))


    def draw_main_menu(self, level_buttons_data, current_level, max_level, mouse_pos=(0, 0)):
        """Draws the main menu with level selection and the new Instructions button."""
        self.screen.fill((230, 230, 235))
        
        # Title
        title = self.title_font.render("MAZE ESCAPE", True, self.ACCENT_COLOR)
        self.screen.blit(title, (self.screen.get_width()//2 - title.get_width()//2, 80))
        
        # Subtitle
        subtitle = self.bold_font.render("Select a Level to Play", True, self.TEXT_LIGHT_COLOR)
        self.screen.blit(subtitle, (self.screen.get_width()//2 - subtitle.get_width()//2, 160))

        # Level Grid
        button_rects = []
        buttons_per_row = 5
        button_size = 70
        button_margin = 15
        
        grid_width = buttons_per_row * (button_size + button_margin) - button_margin
        start_x = self.screen.get_width() // 2 - grid_width // 2
        start_y = 250
        
        for i in range(max_level):
            row = i // buttons_per_row
            col = i % buttons_per_row
            x = start_x + col * (button_size + button_margin)
            y = start_y + row * (button_size + button_margin)
            
            rect = pygame.Rect(x, y, button_size, button_size)
            button_rects.append(rect)
            
            is_unlocked = i < current_level
            is_current = i + 1 == current_level
            is_hover = rect.collidepoint(mouse_pos)
            
            if is_unlocked:
                color = self.ACCENT_COLOR if is_current else self.START_COLOR
                hover_color = (min(color[0] + 20, 255), min(color[1] + 20, 255), min(color[2] + 20, 255)) if is_hover else color
                
                # Draw button
                self.draw_button(str(i + 1), rect, hover=is_hover, color=hover_color)
                
            else:
                # Draw locked button
                pygame.draw.rect(self.screen, (150, 150, 150), rect, border_radius=12)
                lock_text = self.font.render("🔒", True, (255, 255, 255))
                self.screen.blit(lock_text, (rect.centerx - lock_text.get_width()//2, rect.centery - lock_text.get_height()//2))

        # Draw Instructions Button
        num_rows = (max_level + buttons_per_row - 1) // buttons_per_row
        instructions_y = start_y + num_rows * (button_size + button_margin) + 40
        
        instruction_button = pygame.Rect(self.screen.get_width()//2 - 150, instructions_y, 300, 45)
        
        instruction_hover = instruction_button.collidepoint(mouse_pos)
        instruction_rect = self.draw_button("Instructions (I)", instruction_button, hover=instruction_hover, color=(100, 100, 150))

        return button_rects, instruction_rect # Returns both lists

    
    def draw_instructions_screen(self, back_hover=False):
        """Draw a dedicated screen for game instructions."""
        self.screen.fill((230, 230, 235))
        
        box_width, box_height = 650, 500
        box_x = (self.screen.get_width() - box_width) // 2
        box_y = (self.screen.get_height() - box_height) // 2
        
        # Main instruction card
        pygame.draw.rect(self.screen, (255, 255, 255), (box_x, box_y, box_width, box_height), border_radius=20)
        pygame.draw.rect(self.screen, self.ACCENT_COLOR, (box_x, box_y, box_width, box_height), 3, border_radius=20)
        
        # Header
        header_rect = pygame.Rect(box_x, box_y, box_width, 80)
        # Draw a rounded header box
        pygame.draw.rect(self.screen, self.ACCENT_COLOR, header_rect, border_radius=20)
        # Fill the unrounded bottom part of the header
        pygame.draw.rect(self.screen, self.ACCENT_COLOR, (box_x, box_y + 40, box_width, 40)) 
        
        title_text = self.title_font.render("HOW TO PLAY", True, (255, 255, 255))
        self.screen.blit(title_text, (box_x + (box_width - title_text.get_width()) // 2, box_y + 20))
        
        # Content
        y_pos = box_y + 110
        padding_x = box_x + 40
        
        # 1. Goal
        self.screen.blit(self.bold_font.render("GOAL:", True, self.TEXT_COLOR), (padding_x, y_pos))
        self.screen.blit(self.font.render("Find the EXIT (red) before the Snake catches you!", True, self.TEXT_LIGHT_COLOR), (padding_x + 100, y_pos + 3))
        y_pos += 40
        
        # 2. Controls
        self.screen.blit(self.bold_font.render("CONTROLS:", True, self.TEXT_COLOR), (padding_x, y_pos))
        y_pos += 30
        
        control_items = [
            ("ARROW KEYS", "Move your player one square."),
            ("H", "Toggle the shortest path hint."),
            ("P / ESC / SPACE", "Pause the game."),
            ("R", "Restart the current level."),
            ("M", "Return to Main Menu (from anywhere).")
        ]
        
        for key, instruction in control_items:
            key_text = self.bold_font.render(key, True, self.ACCENT_COLOR)
            desc_text = self.font.render(instruction, True, self.TEXT_COLOR)
            
            self.screen.blit(key_text, (padding_x + 10, y_pos))
            self.screen.blit(desc_text, (padding_x + 150, y_pos + 3))
            y_pos += 35
            
        # 3. Snake Danger
        self.screen.blit(self.bold_font.render("DANGER ZONE:", True, self.TEXT_COLOR), (padding_x, y_pos + 10))
        snake_info = self.font.render("The snake wanders randomly and gets faster every level!", True, self.END_COLOR)
        self.screen.blit(snake_info, (padding_x + 180, y_pos + 13))

        # Back Button
        back_button = pygame.Rect(box_x + box_width // 2 - 100, box_y + box_height - 70, 200, 45)
        back_rect = self.draw_button("Back to Menu (M)", back_button, hover=back_hover, color=(100, 100, 150))
        
        return back_rect

    
    def draw_pause_menu(self, current_level, moves, elapsed_time, resume_hover=False, restart_hover=False, menu_hover=False):
        """Draws the pause menu overlay and returns button rects."""
        # Semi-transparent overlay
        s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))  
        self.screen.blit(s, (0, 0))

        center_x = self.screen.get_width() // 2
        center_y = self.screen.get_height() // 2

        # Pause text
        pause_text = self.title_font.render("GAME PAUSED", True, (255, 255, 255))
        self.screen.blit(pause_text, (center_x - pause_text.get_width()//2, center_y - 150))
        
        # Stats in pause menu
        stats_y = center_y - 80
        stats = [
            (f"LEVEL:", f"{current_level}"),
            (f"TIME:", f"{int(elapsed_time)}s"),
            (f"MOVES:", f"{moves}")
        ]
        for label, value in stats:
            label_text = self.bold_font.render(label, True, (200, 200, 200))
            value_text = self.bold_font.render(value, True, (255, 255, 255))
            self.screen.blit(label_text, (center_x - 120, stats_y))
            self.screen.blit(value_text, (center_x + 120 - value_text.get_width(), stats_y))
            stats_y += 30

        # Buttons
        button_width, button_height = 200, 50
        y_start = center_y + 30
        
        resume_button_rect = pygame.Rect(center_x - button_width//2, y_start, button_width, button_height)
        restart_button_rect = pygame.Rect(center_x - button_width//2, y_start + 65, button_width, button_height)
        menu_button_rect = pygame.Rect(center_x - button_width//2, y_start + 130, button_width, button_height)

        resume_button = self.draw_button("RESUME (SPACE)", resume_button_rect, hover=resume_hover, color=self.ACCENT_COLOR)
        restart_button = self.draw_button("RESTART (R)", restart_button_rect, hover=restart_hover, color=(255, 165, 0))
        menu_button = self.draw_button("MAIN MENU (M)", menu_button_rect, hover=menu_hover, color=(100, 100, 150))

        return resume_button, restart_button, menu_button

    def draw_level_complete(self, current_level, moves, elapsed_time, maze_width, maze_height):
        """Draws the level complete screen."""
        # Semi-transparent overlay
        s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))  
        self.screen.blit(s, (0, 0))

        center_x = self.screen.get_width() // 2
        center_y = self.screen.get_height() // 2

        # Title
        complete_text = self.title_font.render(f"LEVEL {current_level} COMPLETE!", True, self.START_COLOR)
        self.screen.blit(complete_text, (center_x - complete_text.get_width()//2, center_y - 120))
        
        # Stats
        stats_y = center_y - 40
        stats = [
            (f"TIME TAKEN:", f"{int(elapsed_time)}s"),
            (f"TOTAL MOVES:", f"{moves}")
        ]
        for label, value in stats:
            label_text = self.bold_font.render(label, True, (200, 200, 200))
            value_text = self.bold_font.render(value, True, (255, 255, 255))
            self.screen.blit(label_text, (center_x - 120, stats_y))
            self.screen.blit(value_text, (center_x + 120 - value_text.get_width(), stats_y))
            stats_y += 30

        # Next Level Button
        button_width, button_height = 250, 60
        next_button_rect = pygame.Rect(center_x - button_width//2, center_y + 80, button_width, button_height)
        
        mouse_pos = pygame.mouse.get_pos()
        hover = next_button_rect.collidepoint(mouse_pos)
        
        return self.draw_button("NEXT LEVEL (SPACE)", next_button_rect, hover=hover, color=self.ACCENT_COLOR)


    def draw_game_over(self, current_level):
        """Draws the game over screen."""
        # Semi-transparent overlay
        s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        s.fill((150, 0, 0, 220))  # Dark Red Overlay
        self.screen.blit(s, (0, 0))

        center_x = self.screen.get_width() // 2
        center_y = self.screen.get_height() // 2

        # Title
        game_over_text = self.title_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(game_over_text, (center_x - game_over_text.get_width()//2, center_y - 120))
        
        level_text = self.bold_font.render(f"You were caught on Level {current_level}", True, (255, 200, 200))
        self.screen.blit(level_text, (center_x - level_text.get_width()//2, center_y - 60))

        # Buttons
        button_width, button_height = 200, 50
        y_start = center_y + 30
        
        restart_button_rect = pygame.Rect(center_x - button_width//2, y_start, button_width, button_height)
        menu_button_rect = pygame.Rect(center_x - button_width//2, y_start + 65, button_width, button_height)

        mouse_pos = pygame.mouse.get_pos()
        
        restart_button = self.draw_button("RESTART (R)", restart_button_rect, hover=restart_button_rect.collidepoint(mouse_pos), color=(255, 165, 0))
        menu_button = self.draw_button("MAIN MENU (M)", menu_button_rect, hover=menu_button_rect.collidepoint(mouse_pos), color=(100, 100, 150))

        return restart_button, menu_button