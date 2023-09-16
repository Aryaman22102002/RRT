import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from random import randrange
    
x_axis_min_limit = int(0)
x_axis_max_limit = int(100)
y_axis_min_limit = int(0)
y_axis_max_limit = int(100)

fig = plt.figure()
plt.xlim(0, 100)
plt.ylim(0, 100)

num_of_obs = int(input("Please enter the number of obstacles required between 2 to 5: "))
if num_of_obs < 2:
  num_of_obs = 2
elif num_of_obs > 5:
  num_of_obs = 5
  
currentAxis = plt.gca()
i = 0

while i < num_of_obs:
    x_coord = randrange(1, 100)
    y_coord = randrange(1, 100)
    length = randrange(20, 40)
    width = randrange(20, 40)
  
    if(((x_coord > x_axis_min_limit + 5) and ((x_coord + length) < x_axis_max_limit - 5)) and ((y_coord > y_axis_min_limit + 5) and ((y_coord + width) < y_axis_max_limit - 5))):    
        currentAxis.add_patch(Rectangle((x_coord, y_coord), length, width, facecolor="black"))
        i = i + 1

plt.axis('off')

plt.savefig("Images/Obstacles.png")
