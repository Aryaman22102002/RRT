import os

os.system('python3 Generate_Obstacles.py input')
os.system('python3 Generate_Final_Grid.py')
os.system('python3 RRT.py')