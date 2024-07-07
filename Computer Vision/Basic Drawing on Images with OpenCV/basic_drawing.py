# import the required packages
import numpy as np
import cv2

# initialize our canvas as a 500x500 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
# cv2.imshow('Original Canvas', canvas)
# cv2.waitKey(0)

# initialize the origin values
originY, originX = 0, 0

# get image spatial dimensions
height, width = canvas.shape[:2]

# # draw a green line from the top-left corner of our canvas to the
# # bottom-right
line_color = (0, 255, 0)  # green color
#
# # drawing green line
# # with tuple values of x,y cordinates
cv2.line(canvas, (originX, originY), (width, height), line_color)

# # displaying image
# cv2.imshow('Canvas with green diagonal line', canvas)
# cv2.waitKey(0)

# draw a 3 pixel thick red line from the top-right corner to the
# bottom-left
line_color = (0, 0, 255)  # red color

thickness = 3  # line thickness

# drawing red line
# with tuple values of x,y cordinates
cv2.line(canvas, (width, originY), (originX, height), line_color, thickness)

# displaying image
# cv2.imshow('Canvas with new red diagonal line', canvas)
# cv2.waitKey(0)

# draw a blue square, starting at 62x62 and ending at 437x437
line_color = (255, 0, 0)  # blue color

# drawing blue rectangle
cv2.rectangle(canvas, (62, 62), (437, 437), line_color)

# # displaying image
# cv2.imshow('Canvas with new blue rectangle', canvas)
# cv2.waitKey(0)

# draw a rectangle (white and filled in )
line_color = (255, 255, 255)  # white color
cv2.rectangle(canvas, (150, 150), (350, 350), line_color, cv2.FILLED)

# # displaying image
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# re-initialize the canvas as an empty array
canvas = np.zeros((500, 500, 3), dtype='uint8')

# compute the center (x, y)-coordinates of the canvas
(centerY, centerX) = (canvas.shape[0] // 2, canvas.shape[1] // 2)
white = (255, 255, 255)

# # loop over increasing radii, from 25 pixels to 275 pixels
# in 25 pixel increments

for radius in range(0, 275, 25):
    # draw a white circle with the current radius size
    cv2.circle(canvas, (centerX, centerY), radius, white)

# display image
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# re-initialize canvas
canvas = np.zeros((500, 500, 3), dtype="uint8")

# draw 25 random circles
for i in range(0, 25):
    # randomly generate a radius size between 5 and 200, generate a
    # random color, and then pick a random point on our canvas where
    # the circle will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    point = np.random.randint(0, high=500, size=(2,))

    # draw the random circle on the canvas
    cv2.circle(canvas, tuple(point), radius, color, -1)


# display the image
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)






