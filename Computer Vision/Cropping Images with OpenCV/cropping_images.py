# import required packages
import cv2
import matplotlib.pyplot as plt

# Images are read as numpy arrays
# the image can be cropped through slicing operations
# images are sliced in [startY:endY, startX:endX] format
# since we need the correct X and Y coordinates to crop
# images, we would plot the image with matplotlib.pyplot
# function to get coordinate values

# load and display the original image
image = cv2.imread('Flag_of_Ghana.png')
cv2.imshow("Original", image)
cv2.waitKey(0)

# get the coordinates of the star
# # read and plot the image with matplotlib
plt_flag = plt.imread('Flag_of_Ghana.png')
plt.imshow(plt_flag)
plt.show()

# from the plot
# define coordinates that map out star
startX, startY = 244, 142
endX, endY = 395, 285

# # crop out the star using coordinates
star = image[startY:endY, startX:endX]
print(star.shape)
cv2.imshow("Star", star)
cv2.waitKey(0)


# crop out the red region using the coordinates
startX, startY = 0, 0
endX, endY = 640, 140

# crop out red region using the coordinates
red = image[startY:endY, startX:endX]
cv2.imshow("red region", red)
cv2.waitKey(0)

# define the coordinates that map out the yellow region
startX, startY = 0, 143
endX, endY = 640, 282

# crop out the yellow region using the coordinates
yellow = image[startY:endY, startX:endX]
cv2.imshow("yellow region", yellow)
cv2.waitKey(0)

# define the coordinates that map out the green region
startX, startY = 0, 285
endX, endY = 640, 425

# crop out green using coordinates
green = image[startY:endY, startX:endX]
cv2.imshow("Green", green)
cv2.waitKey(0)
