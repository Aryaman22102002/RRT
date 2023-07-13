from PIL import Image, ImageOps
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from random import randrange
    
x_axis_min_limit = int(0)
x_axis_max_limit = int(1000)
y_axis_min_limit = int(0)
y_axis_max_limit = int(1000)

fig = plt.figure()
plt.xlim(0, 1000)
plt.ylim(0, 1000)

num_of_obs = int(input("Please enter the number of obstacles required between 10 to 20: "))
if num_of_obs < 10:
  num_of_obs = 10
elif num_of_obs > 20:
  num_of_obs = 20
  
i = 0

while i < num_of_obs:
    x_coord = randrange(1, 1000)
    y_coord = randrange(1, 1000)
    length = randrange(100, 150)
    width = randrange(100, 150)
  
    if(((x_coord > x_axis_min_limit + 5) and ((x_coord + length) < x_axis_max_limit - 5)) or ((y_coord > y_axis_min_limit + 5) and ((y_coord + width) < y_axis_max_limit - 5))):   
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((x_coord, y_coord), length, width, facecolor="black"))
        i = i + 1

plt.show()