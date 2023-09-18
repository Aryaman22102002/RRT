from PIL import Image, ImageOps
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open("Images/Obstacles.png")
img = ImageOps.grayscale(img)
img_1 = img.load()
print(img.size)
print(img_1[386,288])
np_img = np.array(img)
print(np_img.shape)
with np.printoptions(threshold=np.inf):
  f = open("demofile8.txt", "a")
  f.write(str(np_img))
  f.close()
print(np_img[386,288])
  
np_img = ~np_img 
with np.printoptions(threshold=np.inf):
  f = open("demofile12.txt", "a")
  f.write(str(np_img))
  f.close()
np_img[np_img > 0] = 1
with np.printoptions(threshold=np.inf):
  f = open("demofile14.txt", "a")
  f.write(str(np_img))
  f.close()
plt.set_cmap('binary')
with np.printoptions(threshold=np.inf):
  f = open("demofile10.txt", "a")
  f.write(str(np_img))
  f.close()
print(np_img.shape)
print(np_img[288,386])
