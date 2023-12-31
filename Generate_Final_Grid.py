from PIL import Image, ImageOps
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open("Images/Squared_Obstacles_Image.png")
img = ImageOps.grayscale(img)

np_img = np.array(img)
np_img = ~np_img 
np_img[np_img > 0] = 1
plt.set_cmap('binary')
plt.imshow(np_img)
np.save("Images/Grid.npy", np_img)

#grid = np.load("Images/Grid.npy")
#plt.imshow(grid, cmap = 'binary')
#plt.tight_layout()
#plt.show()
