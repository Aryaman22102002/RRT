import numpy as np
import matplotlib.pyplot as plt
import random

# Tree Node Class
class TreeNode():
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.children = []
        self.parent = None
    
# RRT Algoritm
class RRTalgoritm():
    def __init__(self, start, goal, Num_Of_Iterations, grid, step_size):
        self.tree = TreeNode(start_position[0], start_position[1])
        self.goal = TreeNode(goal_position[0], goal_position[1])
        self.NearestNode = TreeNode(None, None)
        self.iterations = min(Num_Of_Iterations, 200)
        self.grid = grid
        self.rho = step_size
        self.path_distance = 0
        self.nearest_distance = 10000
        self.Num_Of_Waypoints = 0
        self.List_Of_Waypoints = []
          
    def AddChildNode(self, x_position, y_position):
        if(x_position == self.goal.x_position and y_position == self.goal.y_position):
            self.NearestNode.children.append(self.NearestNode)
            self.goal.parent = self.NearestNode
        else:
            TempNode = TreeNode(x_position, y_position)
            self.NearestNode.children.append(TempNode)
            TempNode.parent = self.NearestNode
            
    def SampleAPoint(self):
        x = random.randint(1, self.grid[1])
        y = random.randint(1, self.grid[0])
        point = np.array([x, y])
        return point
    
    def JoinSamplePoint(self, location_start, location_end):
        offset = self.rho*self.UnitVector(location_start, location_end)
        point = np.array([location_start.x_position + offset[0], location_start.y_position + offset[1]])
        if point[0] >= self.grid.shape[1]:
           point[0] = self.grid.shape[1]
        if point[1] >= self.grid.shape[0]:
           point[1] = self.grid.shape[0]
        return point
            
            
        
        
        
        