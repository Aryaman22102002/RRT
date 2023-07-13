from PIL import Image, ImageOps
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open("obstacles.png")
img = ImageOps.grayscale(img)

np_img = np.array(img)
np_img = ~np_img 
np_img[np_img > 0] = 1
plt.set_cmap('binary')
plt.imshow(np_img)

np.save("grid.npy", np_img)

grid = np.load("grid.npy")
plt.imshow(grid, cmap = 'binary')
plt.tight_layout()
plt.show()