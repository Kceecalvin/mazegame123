import random
import numpy as np
from collections import deque

class MazeGenerator:
    def __init__(self, width, height):
        # Ensure dimensions are odd for proper maze generation
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.maze = None
    
    def generate_dfs(self):
        """Depth-First Search with recursive backtracking"""
        # Initialize maze with walls
        maze = np.ones((self.height, self.width), dtype=int)
        
        def carve_path(x, y):
            maze[y][x] = 0  # Mark as path
            directions = [(2,0), (0,2), (-2,0), (0,-2)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width-1 and 0 < ny < self.height-1 and maze[ny][nx] == 1:
                    # Carve path between current cell and next cell
                    maze[y + dy//2][x + dx//2] = 0
                    carve_path(nx, ny)
        
        # Start from top-left (ensure odd coordinates)
        start_x, start_y = 1, 1
        carve_path(start_x, start_y)
        
        # FIXED: Create proper entrance and exit
        maze[1][0] = 0  # Entrance - left side
        maze[self.height-2][self.width-1] = 0  # Exit - right side
        
        self.maze = maze
        return maze
    
    def generate_prims(self):
        """Prim's Algorithm for maze generation"""
        maze = np.ones((self.height, self.width), dtype=int)
        
        # Start with a cell and add its walls to the list
        start_x, start_y = 1, 1
        maze[start_y][start_x] = 0
        
        walls = []
        # Add neighboring walls of the starting cell
        for dx, dy in [(2,0), (0,2), (-2,0), (0,-2)]:
            nx, ny = start_x + dx, start_y + dy
            if 0 < nx < self.width-1 and 0 < ny < self.height-1:
                walls.append((nx, ny, start_x + dx//2, start_y + dy//2))
        
        while walls:
            # Randomly select a wall
            wall_idx = random.randint(0, len(walls)-1)
            x, y, cx, cy = walls.pop(wall_idx)
            
            if maze[y][x] == 1:  # If the cell is still a wall
                # Carve passage
                maze[y][x] = 0
                maze[cy][cx] = 0  # Carve between cells
                
                # Add new walls
                for dx, dy in [(2,0), (0,2), (-2,0), (0,-2)]:
                    nx, ny = x + dx, y + dy
                    if 0 < nx < self.width-1 and 0 < ny < self.height-1 and maze[ny][nx] == 1:
                        walls.append((nx, ny, x + dx//2, y + dy//2))
        
        # FIXED: Create proper entrance and exit
        maze[1][0] = 0
        maze[self.height-2][self.width-1] = 0
        
        self.maze = maze
        return maze
    
    def generate_kruskals(self):
        """Kruskal's Algorithm using union-find"""
        maze = np.ones((self.height, self.width), dtype=int)
        
        # Each cell is its own set initially
        parent = {}
        rank = {}
        
        def find(cell):
            if parent[cell] != cell:
                parent[cell] = find(parent[cell])
            return parent[cell]
        
        def union(cell1, cell2):
            root1, root2 = find(cell1), find(cell2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1
                return True
            return False
        
        # Initialize sets for each cell
        for y in range(1, self.height-1, 2):
            for x in range(1, self.width-1, 2):
                cell = (x, y)
                parent[cell] = cell
                rank[cell] = 0
                maze[y][x] = 0  # Make cell a passage
        
        # Create all possible edges between cells
        edges = []
        for y in range(1, self.height-1, 2):
            for x in range(1, self.width-1, 2):
                if x + 2 < self.width-1:
                    edges.append(((x, y), (x+2, y), (x+1, y)))  # Horizontal edge
                if y + 2 < self.height-1:
                    edges.append(((x, y), (x, y+2), (x, y+1)))  # Vertical edge
        
        random.shuffle(edges)
        
        # Process edges
        for cell1, cell2, wall in edges:
            if union(cell1, cell2):
                maze[wall[1]][wall[0]] = 0  # Remove wall
        
        # FIXED: Create proper entrance and exit
        maze[1][0] = 0
        maze[self.height-2][self.width-1] = 0
        
        self.maze = maze
        return maze
    
    def generate_division(self):
        """Recursive Division method"""
        maze = np.zeros((self.height, self.width), dtype=int)
        
        # Create border
        maze[0, :] = 1
        maze[self.height-1, :] = 1
        maze[:, 0] = 1
        maze[:, self.width-1] = 1
        
        def divide(x, y, width, height):
            if width < 3 or height < 3:
                return
            
            # Choose orientation (vertical or horizontal)
            horizontal = height > width if random.random() > 0.5 else width > height
            if width == height:
                horizontal = random.choice([True, False])
            
            # Wall position (must be even)
            wx = x + (0 if horizontal else random.randrange(1, width-1) // 2 * 2)
            wy = y + (random.randrange(1, height-1) // 2 * 2 if horizontal else 0)
            
            # Passage position (must be odd)
            px = wx + (0 if horizontal else random.randrange(0, 2) * 2 - 1)
            py = wy + (random.randrange(0, 2) * 2 - 1 if horizontal else 0)
            
            # Draw wall
            if horizontal:
                for i in range(x, x + width):
                    if i != px:
                        maze[wy][i] = 1
            else:
                for i in range(y, y + height):
                    if i != py:
                        maze[i][wx] = 1
            
            # Recursively divide sub-rooms
            if horizontal:
                divide(x, y, width, wy - y)  # Top
                divide(x, wy + 1, width, y + height - wy - 1)  # Bottom
            else:
                divide(x, y, wx - x, height)  # Left
                divide(wx + 1, y, x + width - wx - 1, height)  # Right
        
        # Start division
        divide(1, 1, self.width-2, self.height-2)
        
        # FIXED: Create proper entrance and exit
        maze[1][0] = 0
        maze[self.height-2][self.width-1] = 0
        
        self.maze = maze
        return maze
    
    def get_start_end(self):
        """Get start and end positions - FIXED to match maze layout"""
        # Start is just to the left of the entrance (which is at (0,1))
        start = (0, 1)
        # End is just to the right of the exit (which is at (width-1, height-2))
        end = (self.width-1, self.height-2)
        return start, end