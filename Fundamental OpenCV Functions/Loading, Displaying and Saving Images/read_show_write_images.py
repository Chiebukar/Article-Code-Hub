# import the required packages
import cv2

# load the image from disk
image = cv2.imread('eiffel_tower.jpg')

# get the spatial dimensions
# including width, height, and number of channels
(height, width, channels) = image.shape[:3]

# display the image width, height, and number of channels
print("height: {} pixels".format(height))
print("width: {}  pixels".format(width))
print("channels: {}".format(channels))

# show the image and wait for a keypress to quit display
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk
# with desired filetype and directory
cv2.imwrite("newimage.jpg", image)
