# import the required packages

import cv2


# load the image
image = cv2.imread('coal_city.jpg')

# display image
cv2.imshow('original image', image)
cv2.waitKey(0)

# display the image pixel values at the origin (top left corner)
(b, g, r) = image[0, 0] # values at origin
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#updating image pixels
# update the pixel at (50, 20)  to red
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# get the spatial dimensions of the image

# get image origin
originY, originX = 0, 0

# get image height and width
height, width = image.shape[:2]

# compute the center of the image
# which is simply the width and height
# divided by two
(centerX, centerY) = (width // 2, height // 2)

print('Image height: ', height)
print('Image width: ', width)
print('Center location: ', (centerY, centerX))


# since images are read as numpy arrays
# sections of the image can be cropped through slicing operations
# to crop the top left corner of the image
# slice the height pixels from origin to center
# and width from origin to center
top_left = image[originY:centerY, originX:centerX]
cv2.imshow("Top-Left Corner", top_left)
cv2.waitKey(0)

# crop the top right corner
# to crop the top right corner
# slice the height pixels from origin to center
# and width from center to top right(width)
top_right = image[originY:centerY, centerX:width]
cv2.imshow("Top-Right Corner", top_right)
cv2.waitKey(0)


# crop the bottom left corner
# to crop the bottom left corner
# slice the height pixels from origin to center
# and width from center to top right(width)
bottom_left = image[centerY:height, originX:centerX]
cv2.imshow("Bottom-Left Corner", bottom_left)
cv2.waitKey(0)


# crop the bottom right corner
# to crop the bottom right corner
# slice the height pixels from origin to center
# and width from center to top right(width)
bottom_right = image[centerY:height, centerX:width]
cv2.imshow("Bottom-Right Corner", bottom_right)
cv2.waitKey(0)


# set the top-left corner of the original image to be green
image[originY:centerY, originX:centerX] = (0, 255, 0)

# Show the updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)