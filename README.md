# RRT

This is my implementation of a path planning algorithm known as the Rapidly Exploring Random Tree (RRT) algorithm.

## File Structure

```
   ┣ 📂Images
     ┣ 📂Example1_3_Obstacles              # 3 Obstacles Case
     ┃ ┗ 📜Grid.npy                        # Numpy grid of the image
     ┃ ┗ 📜Obstacles.png                   # Image with obstacles. 
     ┃ ┗ 📜Result.png                      # Output screenshot
     ┃ ┗ 📜Squared_Obstacles_Image.png     # Obstacle Image In Square Dimensions
     ┣ 📂Example2_4_Obstacles              # 4 Obstacles Case
     ┃ ┗ 📜Grid.npy                        # Numpy grid of the image
     ┃ ┗ 📜Obstacles.png                   # Image with obstacles. 
     ┃ ┗ 📜Result.png                      # Output screenshot
     ┃ ┗ 📜Squared_Obstacles_Image.png     # Obstacle Image In Square Dimensions
     ┣ 📂Example3_5_Obstacles              # 5 Obstacles Case
     ┃ ┗ 📜Grid.npy                        # Numpy grid of the image
     ┃ ┗ 📜Obstacles.png                   # Image with obstacles. 
     ┃ ┗ 📜Result.png                      # Output screenshot
     ┃ ┗ 📜Squared_Obstacles_Image.png     # Obstacle Image In Square Dimensions
     ┣ 📂Example4_6_Obstacles              # 6 Obstacles Case
     ┃ ┗ 📜Grid.npy                        # Numpy grid of the image
     ┃ ┗ 📜Obstacles.png                   # Image with obstacles. 
     ┃ ┗ 📜Result.png                      # Output screenshot
     ┃ ┗ 📜Squared_Obstacles_Image.png     # Obstacle Image In Square Dimensions
     ┣ 📂Example5_8_Obstacles              # 8 Obstacles Case
     ┃ ┗ 📜Grid.npy                        # Numpy grid of the image
     ┃ ┗ 📜Obstacles.png                   # Image with obstacles. 
     ┃ ┗ 📜Result.png                      # Output screenshot
     ┃ ┗ 📜Squared_Obstacles_Image.png     # Obstacle Image In Square Dimensions
     ┣ 📜RRT.png                           # RRT algorithm flowchart
   ┣ 📂Videos
   ┃ ┗ 📜Example1.mp4                      # Video of the simulation for 3 obstacles case.
   ┃ ┗ 📜Example2.mp4                      # Video of the simulation for 4 obstacles case.
   ┃ ┗ 📜Example3.mp4                      # Video of the simulation for 5 obstacles case.
   ┃ ┗ 📜Example4.mp4                      # Video of the simulation for 6 obstacles case.
   ┃ ┗ 📜Example5.mp4                      # Video of the simulation for 8 obstacles case.                 
   ┣ 📜Generate_Final_Grid.py              # Converts the image with obstacles into a numpy array/grid.
   ┣ 📜Generate_Obstacles.py               # Generates an image with black rectangular obstacles.                    
   ┣ 📜LICENSE
   ┣ 📜README.md
   ┣ 📜RRT.py                              # RRT algorithm
   ┣ 📜Squaring_Figure.py                  # Converts the rectangular obstacles image to a square
   ┣ 📜start.py                            # Runs all three required python files in appropriate sequence. 
```

## Requirements
<p>
<image src="https://user-images.githubusercontent.com/82901720/212160658-6f195834-8872-4203-85ce-061a18272f86.svg" width=50 title="python"> &nbsp; Python <br> <br>
<image src="https://user-images.githubusercontent.com/50221806/86498201-a8bd8680-bd39-11ea-9d08-66b610a8dc01.png" width=50 title="numpy"> &nbsp; Numpy <br> <br>
<image src="https://tse3.mm.bing.net/th?id=OIP.PLA7xUWKJtFAZzQz9rzC1wHaDt&pid=Api&P=0&h=180" width=50 title="pillow"> &nbsp; Pillow <br> <br>
<image src="https://www.fireblazeaischool.in/blogs/wp-content/uploads/2020/06/matplotlib1.jpg" width=50 title="matplotlib"> &nbsp; Matplotlib <br>
</p>

## How to run
- Just run the `start.py` file to start the simulation using the command `python3 start.py`.

## RRT Algorithm Flowchart

![RRT](https://user-images.githubusercontent.com/82901720/269403165-29186ec5-657f-43bd-9f65-e088ccafba04.png)

## Output

### Example 1
![Result](https://user-images.githubusercontent.com/82901720/268761840-febe97e2-fe19-4f06-b96c-b62c020e7853.png)

https://user-images.githubusercontent.com/82901720/273644116-a3662107-2fbe-4a68-9b94-b6a0875c6d03.mp4

### Example 2
![Result](https://user-images.githubusercontent.com/82901720/268761861-ac79028f-3492-4102-b469-1443e6dfebda.png)

https://user-images.githubusercontent.com/82901720/273644269-8774fff8-8e56-4840-85eb-929224f75897.mp4

### Example 3
![Result](https://user-images.githubusercontent.com/82901720/268761922-83f3bc2f-128e-4c72-a075-e124f7aa28f9.png)

https://user-images.githubusercontent.com/82901720/273644309-94a4b5f1-c8f7-49d7-8201-12666217e1a7.mp4

### Example 4
![Result](https://user-images.githubusercontent.com/82901720/268761937-5da00a10-f929-4f06-bc7b-71b5aa8fcd96.png)

https://user-images.githubusercontent.com/82901720/273644357-53697df8-3d2a-4868-9595-36fb023127bc.mp4

### Example 5
![Result](https://user-images.githubusercontent.com/82901720/268761949-6f830025-08aa-44d0-9d01-5e05a4ed4e79.png)

https://user-images.githubusercontent.com/82901720/273644398-57133e26-9ee2-4d5c-ba1b-def2a5154bce.mp4





