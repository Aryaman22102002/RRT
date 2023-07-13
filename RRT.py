import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

np.set_printoptions(precision = 3, suppress = True)

# Tree Node Class
class TreeNode():
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.children = []
        self.parent = None
    
# RRT Algoritm
class RRTalgoritm():
    def __init__(self, start_position, goal_position, Num_Of_Iterations, grid, step_size):
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
    
    def ObstacleCollision(self, location_start, location_end):
        u_hat = self.UnitVector(location_start, location_end)
        temp_point = np.array([0.0, 0.0])
        
        for i in range(self.rho):
            temp_point[0] = location_start.x_position + i*u_hat[0]
            temp_point[1] = location_start.y_position + i*u_hat[1]
            
            if(self.grid[round(temp_point[1]), round(temp_point[0])] == 1):
                return True
            else:
                return False
            
    def UnitVector(self, location_start, location_end):
        v = np.array([location_end[0] - location_start.x_position, location_end[1] - location_start.y_position])
        u_hat = v/np.linalg.norm(v)
        return u_hat
    
    def FindNearestNode(self, root, point):
        if not root:
            return
        
        dist = self.distance(root, point)
        
        if dist <= self.nearest_distance:
            self.NearestNode = root
            self.nearest_distance = dist
            
        for child in root.children:
            self.FindNearestNode(child, point)
        
        pass
    
    def distance(self, node1, point):
        dist = np.sqrt((node1.x_position - point[0])**2 + (node1.y_position - point[1])**2)   
        return dist
    
    def GoalReached(self, point):
        if self.distance(self.goal, point) <= self.rho:
            return True
        pass
    
    def ResetNearestAttributeValues(self):
        self.NearestNode = None
        self.nearest_distance = 10000
        
    def BackTraceRRTPath(self, goal):
        if goal.x_position == self.tree.x_position:
            return 
        
        self.Num_Of_Waypoints = self.Num_Of_Waypoints + 1
        
        current_point = np.array([goal.x_position, goal.y_position])
        self.List_Of_Waypoints.insert(0, current_point)
        self.path_distance = self.path_distance + self.rho
        self.BackTraceRRTPath(goal.parent)
        

grid = np.load("grid.npy")
start = np.array([100.0, 100.0])
goal = np.array([500.0, 500.0])
Num_Of_Iterations = 200
step_size = 50
GoalArea = Circle((goal[0], goal[1]), step_size, color = 'b', fill = "False")
    
        
        
    
        
            
            
        
        
        
        