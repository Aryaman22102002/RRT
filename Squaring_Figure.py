from PIL import Image, ImageOps

img = Image.open("Images/Obstacles.png")
x, y = img.size
extra_padding = abs((x-y)/2)
new_size = int(min(x,y) + extra_padding)
img_new = img.resize((new_size, new_size))
img_new.save('Images/Squared_Obstacles_Image.png')

