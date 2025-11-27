import heapq
from collections import deque
import numpy as np
import random

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.height, self.width = maze.shape
    
    def solve_bfs(self, start, end):
        """Breadth-First Search - guarantees shortest path"""
        queue = deque([start])
        visited = {start: None}
        
        while queue:
            current = queue.popleft()
            
            if current == end:
                break
            
            x, y = current
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                if (0 <= nx < self.width and 0 <= ny < self.height and 
                    self.maze[ny][nx] == 0 and neighbor not in visited):
                    queue.append(neighbor)
                    visited[neighbor] = current
        
        # Reconstruct path
        path = []
        if end in visited:
            current = end
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(start)
            path.reverse()
        
        return path, visited.keys()
    
    def solve_dfs(self, start, end):
        """Depth-First Search - doesn't guarantee shortest path"""
        stack = [start]
        visited = {start: None}
        
        while stack:
            current = stack.pop()
            
            if current == end:
                break
            
            x, y = current
            # Explore in random order for more natural DFS
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                if (0 <= nx < self.width and 0 <= ny < self.height and 
                    self.maze[ny][nx] == 0 and neighbor not in visited):
                    stack.append(neighbor)
                    visited[neighbor] = current
        
        # Reconstruct path
        path = []
        if end in visited:
            current = end
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(start)
            path.reverse()
        
        return path, visited.keys()
    
    def solve_a_star(self, start, end):
        """A* Search - efficient with heuristics"""
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, end)}
        
        visited = set()
        
        while open_set:
            current = heapq.heappop(open_set)[1]
            visited.add(current)
            
            if current == end:
                break
            
            x, y = current
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                if (0 <= nx < self.width and 0 <= ny < self.height and 
                    self.maze[ny][nx] == 0):
                    tentative_g = g_score[current] + 1
                    
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                        if neighbor not in visited:
                            heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        # Reconstruct path
        path = []
        if end in came_from:
            current = end
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
        
        return path, visited
    
    def solve_dijkstra(self, start, end):
        """Dijkstra's Algorithm - uniform cost search"""
        distances = {start: 0}
        previous = {}
        nodes = set()
        
        # Initialize nodes
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 0:
                    node = (x, y)
                    nodes.add(node)
                    if node not in distances:
                        distances[node] = float('inf')
        
        while nodes:
            # Get node with smallest distance
            current = min(nodes, key=lambda node: distances[node])
            nodes.remove(current)
            
            if current == end:
                break
            
            if distances[current] == float('inf'):
                break
            
            x, y = current
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                if neighbor in nodes:
                    alt = distances[current] + 1
                    if alt < distances[neighbor]:
                        distances[neighbor] = alt
                        previous[neighbor] = current
        
        # Reconstruct path
        path = []
        if end in previous:
            current = end
            while current != start:
                path.append(current)
                current = previous[current]
            path.append(start)
            path.reverse()
        
        return path, set(previous.keys())