import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import lines
import random
import sys

np.set_printoptions(precision = 3, suppress = True)

# Tree Node Class
class TreeNode():
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.children = []
        self.parent = None
    
# RRT Algorithm
class RRTalgoritm():
    def __init__(self, start_position, goal_position, Num_Of_Iterations, Max_Num_Of_Iterations, grid, step_size):
        self.tree = TreeNode(start_position[0], start_position[1])
        self.goal = TreeNode(goal_position[0], goal_position[1])
        self.NearestNode = TreeNode(None, None)
        self.iterations = min(Num_Of_Iterations, Max_Num_Of_Iterations)
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
        x = random.randint(1, self.grid.shape[1])
        y = random.randint(1, self.grid.shape[0])
        point = np.array([x, y])
        return point
    
    def CheckPathToSamplePoint(self, location_start, location_end):
        offset = self.rho*self.UnitVector(location_start, location_end)
        point = np.array([location_start.x_position + offset[0], location_start.y_position + offset[1]])
        
        if point[0] >= grid.shape[1]:
           point[0] = grid.shape[1]
        if point[1] >= grid.shape[0]:
           point[1] = grid.shape[0]
        return point
    
    def CheckObstacleCollision(self, location_start, location_end):
        u_hat = self.UnitVector(location_start, location_end)
        temp_point = np.array([0.0, 0.0])
        
        for i in range(self.rho):
            temp_point[0] = location_start.x_position + i*u_hat[0]
            temp_point[1] = location_start.y_position + i*u_hat[1]
            
            if(self.grid[min(int(round(temp_point[1])), self.grid.shape[0] - 1), min(int(round(temp_point[0])), self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])) + 1, self.grid.shape[0] - 1) , min(int(round(temp_point[0])), self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])), self.grid.shape[0] - 1), min(int(round(temp_point[0])) + 1, self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])) + 1, self.grid.shape[0] - 1), min(int(round(temp_point[0])) + 1, self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])) - 1, self.grid.shape[0] - 1), min(int(round(temp_point[0])), self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])), self.grid.shape[0] - 1), min(int(round(temp_point[0])) - 1, self.grid.shape[1] - 1)] == 1 or self.grid[min(int(round(temp_point[1])) - 1, self.grid.shape[0] - 1), min(int(round(temp_point[0])) - 1, self.grid.shape[1] - 1)] == 1):
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
        if goal == None:
            print("Number of iterations have exceeded the maximum limit. Hence, terminating the program.")
            sys.exit()
        if goal.x_position == self.tree.x_position:
            return 
        
        self.Num_Of_Waypoints = self.Num_Of_Waypoints + 1
        
        current_point = np.array([goal.x_position, goal.y_position])
        self.List_Of_Waypoints.insert(0, current_point)
        self.path_distance = self.path_distance + self.rho
        self.BackTraceRRTPath(goal.parent)
        

grid = np.load("Images/Grid.npy")
#start = np.array([100.0, 100.0])
#goal = np.array([420.0, 500.0])
flag = 0

while flag == 0:
    start_x = random.randint(1, grid.shape[1] - 1)
    start_y = random.randint(1, grid.shape[0] - 1)
    goal_x = random.randint(1, grid.shape[1] - 1)
    goal_y = random.randint(1, grid.shape[0] - 1)

    if(grid[start_y, start_x] == 0 and grid[goal_y, goal_x] == 0):
        flag = 1

start = np.array([start_x, start_y])
goal = np.array([goal_x, goal_y])

Num_Of_Iterations = 400
Max_Num_Of_Iterations = 500
step_size = 50
GoalArea = Circle((goal[0], goal[1]), step_size, color = 'b', fill = False)

fig = plt.figure("RRT Algorithm")
plt.imshow(grid, cmap = 'binary')
plt.plot(start[0], start[1], 'ro')
plt.plot(goal[0], goal[1], 'bo')
ax = fig.gca()
ax.add_patch(GoalArea)
plt.xlabel('X-Axis $(m)$')
plt.ylabel('Y-Axis $(m)$')

rrt = RRTalgoritm(start, goal, Num_Of_Iterations, Max_Num_Of_Iterations, grid, step_size)

for i in range(rrt.iterations):
    rrt.ResetNearestAttributeValues()
  #  print("Iteration = ", i+1)
    
    point = rrt.SampleAPoint()
    rrt.FindNearestNode(rrt.tree, point)
    new = rrt.CheckPathToSamplePoint(rrt.NearestNode, point)
    temp_list = new.ravel().tolist()
    if temp_list[0] < grid.shape[1] and temp_list[1] < grid.shape[0]:
       if grid[int(temp_list[1]),int(temp_list[0])] == 0:
        bool = rrt.CheckObstacleCollision(rrt.NearestNode, new)
        if(bool == False):
        # print(grid[point[0], point[1]])
            rrt.AddChildNode(new[0], new[1])
            plt.pause(0.10)
            plt.plot([rrt.NearestNode.x_position, new[0]], [rrt.NearestNode.y_position, new[1]], 'g.--')
            
            if(rrt.GoalReached(new)):
                rrt.AddChildNode(goal[0], goal[1])
                print("Goal Has Been Discovered")
                print("Total Number Of Iterations Required = ", i)
                break
        
rrt.BackTraceRRTPath(rrt.goal)
rrt.List_Of_Waypoints.insert(0, start)
print("Number Of Waypoints = ", rrt.Num_Of_Waypoints)
print("Total Path Distance = ", rrt.path_distance)
print("List Of Waypoints = ", rrt.List_Of_Waypoints)

for i in range(len(rrt.List_Of_Waypoints) - 1):
    plt.plot([rrt.List_Of_Waypoints[i][0], rrt.List_Of_Waypoints[i+1][0]], [rrt.List_Of_Waypoints[i][1], rrt.List_Of_Waypoints[i+1][1]], 'r.--')
    plt.pause(0.10)
    
    if i == len(rrt.List_Of_Waypoints) - 2:
        plt.savefig("Images/Result.png")
    

        

    
        
        
    
        
            
            
        
        
        
        
