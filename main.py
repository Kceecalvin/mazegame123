from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.metrics import dp, sp
import random
import math
import numpy as np
from maze_generator import MazeGenerator
from maze_solver import MazeSolver

class MobilePlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.moving = False
        self.move_progress = 0
        self.move_speed = 0.3
        self.moves_count = 0
        self.level_start_time = 0
        self.level_complete_time = 0
        
    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        self.moving = True
        self.move_progress = 0
        self.moves_count += 1
    
    def update(self):
        if self.moving:
            self.move_progress += self.move_speed
            if self.move_progress >= 1:
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False
            else:
                self.x = self.x + (self.target_x - self.x) * self.move_speed
                self.y = self.y + (self.target_y - self.y) * self.move_speed
    
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.moving = False
        self.move_progress = 0
        self.moves_count = 0

class MobileSnake:
    def __init__(self, x, y, maze, start_delay=10000):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.moving = False
        self.move_progress = 0
        self.move_speed = 0.08
        self.maze = maze
        self.solver = MazeSolver(maze)
        self.path = []
        self.update_counter = 0
        self.update_frequency = 6
        self.active = False
        self.activation_time = 0
        self.start_delay = start_delay
        
    def update_path(self, player_x, player_y):
        if not self.active:
            return
            
        self.update_counter += 1
        if self.update_counter >= self.update_frequency:
            self.update_counter = 0
            start = (int(self.x), int(self.y))
            end = (int(player_x), int(player_y))
            self.path, _ = self.solver.solve_bfs(start, end)
            
            if self.path and len(self.path) > 1:
                self.path = self.path[1:]
    
    def update(self, player_x, player_y, current_time):
        if not self.active and current_time >= self.activation_time:
            self.active = True
        
        if self.active:
            self.update_path(player_x, player_y)
            
            if not self.moving and self.path:
                next_x, next_y = self.path[0]
                
                if (0 <= next_x < self.maze.shape[1] and 
                    0 <= next_y < self.maze.shape[0] and 
                    self.maze[next_y][next_x] == 0):
                    
                    self.target_x = next_x
                    self.target_y = next_y
                    self.moving = True
                    self.move_progress = 0
                    self.path = self.path[1:]
            
            if self.moving:
                self.move_progress += self.move_speed
                if self.move_progress >= 1:
                    self.x = self.target_x
                    self.y = self.target_y
                    self.moving = False
                else:
                    self.x = self.x + (self.target_x - self.x) * self.move_speed
                    self.y = self.y + (self.target_y - self.y) * self.move_speed
    
    def reset(self, x, y, start_delay=10000):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.moving = False
        self.move_progress = 0
        self.path = []
        self.update_counter = 0
        self.active = False
        self.start_delay = start_delay
        self.activation_time = 0
    
    def check_collision(self, player_x, player_y):
        if not self.active:
            return False
        return (abs(self.x - player_x) < 0.5 and abs(self.y - player_y) < 0.5)
    
    def get_activation_countdown(self, current_time):
        if self.active:
            return 0
        time_left = max(0, self.activation_time - current_time)
        return time_left // 1000

class MazeWidget(GridLayout):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.cell_size = dp(25)
        self.cols = 1
        self.rows = 1
        self.bind(size=self._update_canvas)
        
        # Enable swipe gestures for movement
        self.touch_start_pos = None
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.touch_start_pos = touch.pos
            return True
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and self.touch_start_pos:
            # Calculate swipe direction
            dx = touch.pos[0] - self.touch_start_pos[0]
            dy = touch.pos[1] - self.touch_start_pos[1]
            
            # Minimum swipe distance (in dp)
            min_swipe = dp(30)
            
            if abs(dx) > min_swipe or abs(dy) > min_swipe:
                if abs(dx) > abs(dy):
                    # Horizontal swipe
                    if dx > 0:
                        self.game.move_player('right')
                    else:
                        self.game.move_player('left')
                else:
                    # Vertical swipe
                    if dy > 0:
                        self.game.move_player('up')
                    else:
                        self.game.move_player('down')
            
            self.touch_start_pos = None
            return True
        return super().on_touch_up(touch)
        
    def _update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Draw background
            Color(0.9, 0.9, 0.92, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            if self.game.maze is not None:
                self._draw_maze()
    
    def _draw_maze(self):
        maze = self.game.maze
        height, width = maze.shape
        
        # Calculate scaling to fit maze in available space
        available_width = self.width - dp(40)
        available_height = self.height - dp(40)
        
        cell_width = min(available_width / width, available_height / height, dp(30))
        start_x = self.x + (self.width - width * cell_width) / 2
        start_y = self.y + (self.height - height * cell_width) / 2
        
        # Draw maze cells
        for y in range(height):
            for x in range(width):
                rect_x = start_x + x * cell_width
                rect_y = start_y + (height - 1 - y) * cell_width  # Flip Y for proper coordinates
                
                if maze[y][x] == 1:  # Wall
                    Color(0.2, 0.2, 0.3, 1)
                    Rectangle(pos=(rect_x, rect_y), size=(cell_width, cell_width))
                else:  # Path
                    Color(0.96, 0.96, 1, 1)
                    Rectangle(pos=(rect_x, rect_y), size=(cell_width, cell_width))
                
                # Draw hint path
                if self.game.show_hint and self.game.hint_path and (x, y) in self.game.hint_path:
                    Color(1, 0.84, 0, 0.7)
                    center_x = rect_x + cell_width / 2
                    center_y = rect_y + cell_width / 2
                    Ellipse(pos=(center_x - cell_width/6, center_y - cell_width/6), 
                           size=(cell_width/3, cell_width/3))
        
        # Draw start and end
        start_x_pos = start_x + 0 * cell_width
        start_y_pos = start_y + (height - 1 - 1) * cell_width
        end_x_pos = start_x + (width - 1) * cell_width
        end_y_pos = start_y + (height - 1 - (height - 2)) * cell_width
        
        # Start (green)
        Color(0.13, 0.55, 0.13, 1)
        Rectangle(pos=(start_x_pos, start_y_pos), size=(cell_width, cell_width))
        
        # End (red)
        Color(0.86, 0.08, 0.24, 1)
        Rectangle(pos=(end_x_pos, end_y_pos), size=(cell_width, cell_width))
        
        # Draw player
        if self.game.player:
            player_x = start_x + self.game.player.x * cell_width
            player_y = start_y + (height - 1 - self.game.player.y) * cell_width
            Color(0.25, 0.41, 0.88, 1)
            Ellipse(pos=(player_x + cell_width/4, player_y + cell_width/4), 
                   size=(cell_width/2, cell_width/2))
        
        # Draw snake
        if self.game.snake:
            snake_x = start_x + self.game.snake.x * cell_width
            snake_y = start_y + (height - 1 - self.game.snake.y) * cell_width
            if self.game.snake.active:
                Color(0.2, 0.8, 0.2, 1)
            else:
                Color(0.6, 0.6, 0.4, 1)
            Ellipse(pos=(snake_x + cell_width/4, snake_y + cell_width/4), 
                   size=(cell_width/2, cell_width/2))

class MobileMazeGame:
    def __init__(self):
        self.maze = None
        self.player = None
        self.snake = None
        self.game_state = "menu"
        self.current_level = 1
        self.max_level = 10
        self.show_hint = False
        self.hint_path = None
        self.game_started = False
        self.start_time = 0
        
        self.level_configs = {
            1: {"size": 11, "algorithm": "dfs", "snake_speed": 0.08, "snake_freq": 6, "snake_delay": 10000},
            2: {"size": 11, "algorithm": "dfs", "snake_speed": 0.10, "snake_freq": 5, "snake_delay": 9000},
            3: {"size": 15, "algorithm": "dfs", "snake_speed": 0.12, "snake_freq": 5, "snake_delay": 8000},
            4: {"size": 15, "algorithm": "prims", "snake_speed": 0.14, "snake_freq": 4, "snake_delay": 7000},
            5: {"size": 19, "algorithm": "prims", "snake_speed": 0.16, "snake_freq": 4, "snake_delay": 6000},
            6: {"size": 19, "algorithm": "prims", "snake_speed": 0.18, "snake_freq": 3, "snake_delay": 5000},
            7: {"size": 21, "algorithm": "division", "snake_speed": 0.20, "snake_freq": 3, "snake_delay": 4000},
            8: {"size": 23, "algorithm": "division", "snake_speed": 0.22, "snake_freq": 2, "snake_delay": 3000},
            9: {"size": 25, "algorithm": "division", "snake_speed": 0.24, "snake_freq": 2, "snake_delay": 2000},
            10: {"size": 27, "algorithm": "division", "snake_speed": 0.26, "snake_freq": 1, "snake_delay": 1000}
        }
    
    def start_level(self, level):
        self.current_level = level
        config = self.level_configs[level]
        size = config["size"]
        
        generator = MazeGenerator(size, size)
        
        if config["algorithm"] == "dfs":
            self.maze = generator.generate_dfs()
        elif config["algorithm"] == "prims":
            self.maze = generator.generate_prims()
        else:
            self.maze = generator.generate_division()
        
        solver = MazeSolver(self.maze)
        start_pos, end_pos = generator.get_start_end()
        
        # Initialize player
        if not self.player:
            self.player = MobilePlayer(start_pos[0], start_pos[1])
        else:
            self.player.reset(start_pos[0], start_pos[1])
        
        # Initialize snake
        self.snake = MobileSnake(start_pos[0], start_pos[1], self.maze, config["snake_delay"])
        self.snake.move_speed = config["snake_speed"]
        self.snake.update_frequency = config["snake_freq"]
        
        # Generate hint path
        path, _ = solver.solve_bfs(start_pos, end_pos)
        self.hint_path = [(int(x), int(y)) for x, y in path] if path else []
        
        self.game_started = False
        self.game_state = "playing"
        self.start_time = 0
    
    def move_player(self, direction):
        if not self.player or self.player.moving or self.game_state != "playing":
            return
        
        x, y = int(round(self.player.x)), int(round(self.player.y))
        new_x, new_y = x, y
        
        if direction == "up":
            new_y += 1
        elif direction == "down":
            new_y -= 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        
        # Check if move is valid
        if (0 <= new_x < self.maze.shape[1] and 
            0 <= new_y < self.maze.shape[0] and 
            self.maze[new_y][new_x] == 0):
            
            # Start game on first move
            if not self.game_started:
                self.game_started = True
                self.start_time = Clock.get_time() * 1000
                self.snake.activation_time = self.start_time + self.snake.start_delay
            
            self.player.set_target(new_x, new_y)
            return True
        return False
    
    def update(self, dt):
        if self.game_state == "playing" and self.game_started:
            current_time = Clock.get_time() * 1000
            
            # Update player
            self.player.update()
            
            # Update snake
            if self.snake:
                self.snake.update(self.player.x, self.player.y, current_time)
            
            # Check win condition
            start_pos, end_pos = (0, 1), (self.maze.shape[1]-1, self.maze.shape[0]-2)
            player_pos = (int(round(self.player.x)), int(round(self.player.y)))
            if player_pos == end_pos and not self.player.moving:
                self.game_state = "level_complete"
                return True
            
            # Check game over
            if self.snake and self.snake.check_collision(self.player.x, self.player.y):
                self.game_state = "game_over"
                return True
        
        return False
    
    def get_level_time(self):
        if not self.game_started:
            return 0
        current_time = Clock.get_time() * 1000
        return max(0, (current_time - self.start_time) // 1000)

class MazeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = MobileMazeGame()
        self.maze_widget = None
        self.update_event = None
        self._keyboard = None
        
    def build(self):
        # Set window size for mobile testing (comment out for actual device)
        # Window.size = (400, 700)
        
        # Enable multitouch for better mobile experience
        from kivy.config import Config
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        
        # Create main layout
        main_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        
        # Title
        title_label = Label(
            text='Maze Escape',
            font_size=sp(24),
            size_hint=(1, 0.1),
            color=get_color_from_hex('#4169E1')
        )
        main_layout.add_widget(title_label)
        
        # Maze display area
        self.maze_widget = MazeWidget(self.game, size_hint=(1, 0.7))
        main_layout.add_widget(self.maze_widget)
        
        # Controls area
        controls_layout = BoxLayout(orientation='vertical', spacing=dp(5), size_hint=(1, 0.2))
        
        # Movement buttons - larger for mobile
        move_layout = GridLayout(cols=3, rows=3, spacing=dp(5), size_hint=(1, 0.6))
        
        # Empty spaces for grid alignment
        move_layout.add_widget(Label(text=''))
        up_btn = Button(
            text='↑', 
            font_size=sp(32),
            background_color=(0.25, 0.41, 0.88, 1),
            size_hint_min_y=dp(60)
        )
        up_btn.bind(on_press=lambda x: self.move('up'))
        move_layout.add_widget(up_btn)
        move_layout.add_widget(Label(text=''))
        
        left_btn = Button(
            text='←', 
            font_size=sp(32),
            background_color=(0.25, 0.41, 0.88, 1),
            size_hint_min_x=dp(60)
        )
        left_btn.bind(on_press=lambda x: self.move('left'))
        move_layout.add_widget(left_btn)
        
        # Center info label
        info_label = Label(
            text='Swipe or\nUse Buttons',
            font_size=sp(10),
            halign='center'
        )
        move_layout.add_widget(info_label)
        
        right_btn = Button(
            text='→', 
            font_size=sp(32),
            background_color=(0.25, 0.41, 0.88, 1),
            size_hint_min_x=dp(60)
        )
        right_btn.bind(on_press=lambda x: self.move('right'))
        move_layout.add_widget(right_btn)
        
        move_layout.add_widget(Label(text=''))
        down_btn = Button(
            text='↓', 
            font_size=sp(32),
            background_color=(0.25, 0.41, 0.88, 1),
            size_hint_min_y=dp(60)
        )
        down_btn.bind(on_press=lambda x: self.move('down'))
        move_layout.add_widget(down_btn)
        move_layout.add_widget(Label(text=''))
        
        controls_layout.add_widget(move_layout)
        
        # Action buttons
        action_layout = BoxLayout(orientation='horizontal', spacing=dp(5), size_hint=(1, 0.4))
        
        hint_btn = Button(text='Hint', font_size=sp(16))
        hint_btn.bind(on_press=self.toggle_hint)
        action_layout.add_widget(hint_btn)
        
        restart_btn = Button(text='Restart', font_size=sp(16))
        restart_btn.bind(on_press=self.restart_level)
        action_layout.add_widget(restart_btn)
        
        menu_btn = Button(text='Menu', font_size=sp(16))
        menu_btn.bind(on_press=self.show_menu)
        action_layout.add_widget(menu_btn)
        
        controls_layout.add_widget(action_layout)
        main_layout.add_widget(controls_layout)
        
        # Start update loop
        self.update_event = Clock.schedule_interval(self.update, 1.0/60.0)
        
        # Setup keyboard for desktop testing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, main_layout)
        if self._keyboard:
            self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
        # Show level selection
        self.show_level_selection()
        
        return main_layout
    
    def _keyboard_closed(self):
        if self._keyboard:
            self._keyboard.unbind(on_key_down=self._on_keyboard_down)
            self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # Arrow keys or WASD for movement
        key = keycode[1]
        if key in ['up', 'w']:
            self.move('up')
        elif key in ['down', 's']:
            self.move('down')
        elif key in ['left', 'a']:
            self.move('left')
        elif key in ['right', 'd']:
            self.move('right')
        elif key == 'h':
            self.game.show_hint = not self.game.show_hint
        elif key == 'r':
            self.game.start_level(self.game.current_level)
        return True
    
    def move(self, direction):
        if self.game.game_state == "playing":
            self.game.move_player(direction)
    
    def toggle_hint(self, instance):
        self.game.show_hint = not self.game.show_hint
    
    def restart_level(self, instance):
        self.game.start_level(self.game.current_level)
    
    def show_menu(self, instance):
        self.show_level_selection()
    
    def show_level_selection(self):
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        title = Label(text='Select Level', font_size=sp(20))
        content.add_widget(title)
        
        # Create level buttons grid
        grid = GridLayout(cols=5, spacing=dp(5))
        
        for level in range(1, 11):
            btn = Button(
                text=str(level),
                font_size=sp(18),
                background_color=(0.25, 0.41, 0.88, 1) if level <= self.game.current_level else (0.7, 0.7, 0.7, 1)
            )
            btn.bind(on_press=lambda instance, l=level: self.start_level(l))
            grid.add_widget(btn)
        
        content.add_widget(grid)
        
        close_btn = Button(text='Close', size_hint=(1, 0.2))
        content.add_widget(close_btn)
        
        self.popup = Popup(
            title='Level Selection',
            content=content,
            size_hint=(0.8, 0.8),
            auto_dismiss=False
        )
        
        close_btn.bind(on_press=self.popup.dismiss)
        self.popup.open()
    
    def start_level(self, level):
        self.game.start_level(level)
        if self.popup:
            self.popup.dismiss()
    
    def update(self, dt):
        if self.game.update(dt):
            # Game state changed
            if self.game.game_state == "level_complete":
                self.show_level_complete()
            elif self.game.game_state == "game_over":
                self.show_game_over()
        
        # Refresh display
        if self.maze_widget:
            self.maze_widget._update_canvas()
    
    def show_level_complete(self):
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        content.add_widget(Label(text=f'Level {self.game.current_level} Complete!', font_size=sp(20)))
        content.add_widget(Label(text=f'Moves: {self.game.player.moves_count}', font_size=sp(16)))
        content.add_widget(Label(text=f'Time: {self.game.get_level_time()}s', font_size=sp(16)))
        
        next_btn = Button(text='Next Level', size_hint=(1, 0.3))
        menu_btn = Button(text='Main Menu', size_hint=(1, 0.3))
        
        content.add_widget(next_btn)
        content.add_widget(menu_btn)
        
        popup = Popup(
            title='Congratulations!',
            content=content,
            size_hint=(0.8, 0.6)
        )
        
        next_btn.bind(on_press=lambda x: (self.game.start_level(min(self.game.current_level + 1, 10)), popup.dismiss()))
        menu_btn.bind(on_press=lambda x: (popup.dismiss(), self.show_level_selection()))
        
        popup.open()
    
    def show_game_over(self):
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        content.add_widget(Label(text='Game Over!', font_size=sp(20)))
        content.add_widget(Label(text='The snake caught you!', font_size=sp(16)))
        content.add_widget(Label(text=f'Level: {self.game.current_level}', font_size=sp(16)))
        
        restart_btn = Button(text='Restart Level', size_hint=(1, 0.3))
        menu_btn = Button(text='Main Menu', size_hint=(1, 0.3))
        
        content.add_widget(restart_btn)
        content.add_widget(menu_btn)
        
        popup = Popup(
            title='Game Over',
            content=content,
            size_hint=(0.8, 0.6)
        )
        
        restart_btn.bind(on_press=lambda x: (self.game.start_level(self.game.current_level), popup.dismiss()))
        menu_btn.bind(on_press=lambda x: (popup.dismiss(), self.show_level_selection()))
        
        popup.open()

if __name__ == '__main__':
    MazeApp().run()