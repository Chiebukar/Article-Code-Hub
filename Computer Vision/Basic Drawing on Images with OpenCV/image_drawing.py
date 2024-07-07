# import required packages
import matplotlib.pyplot as plt
import cv2

# load the input image from disk
image = cv2.imread('samuel.jpg')

# display image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# initialize the origins and  center cordinates
originY, originX = 0, 0
(centerY, centerX) = (image.shape[0]//2, image.shape[1]//2)

# draw a circular edge around picture
# set color at edge to white
color = (255, 255, 255)  # white
radius = round((centerY**2 + centerX ** 2) ** 0.5)  # radius from center to origin
thickness = 100
cv2.circle(image, (centerX, centerY), radius, color, thickness)

# display image
cv2.imshow('Image', image)
cv2.waitKey(0)


# draw two filled in circles covering the
# eyes, and a rectangle over top of my mouth

# display image with matplotlib to view
# image with cordinates
plt.imshow(image)
plt.show()

# initialize eyes coordinates as
# gotten from plot
eyes1, eyes2 = (192, 167), (332, 162)
radius = 50
color = (0, 0, 255)

# draw red circles around the eyes
cv2.circle(image, eyes1, radius, color, -1)
cv2.circle(image, eyes2, radius, color, -1)

# display image
cv2.imshow('Image', image)
cv2.waitKey(0)

# draw blue rectangle around the mouth
color = (255, 0, 0)  # blue
startX, startY = 180, 235
stopX, stopY = 340, 315
cv2.rectangle(image, (startX, startY), (stopX, stopY),  color, -1)

# display image
cv2.imshow('Image', image)
cv2.waitKey(0)
