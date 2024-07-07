# import required packages
import cv2
import imutils

# load and display image
image = cv2.imread('oliver-de-coques.png')

# display image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# get and show the dimensions of original image
OriginalHeight, OriginalWidth = image.shape[:2]
#
print('Dimensions of the original image are: \n height: {}'' \n width: {}'
      .format(OriginalHeight, OriginalWidth))


# # let's resize our image to be 150 pixels wide, but in order to
# # prevent our resized image from being skewed/distorted, we must
# # maintain the same aspect ration of the original image
# # we do this by first calculating the ratio of
# the *new* width to the *old* width


# get the ratio of *new* width to the *original* width
new_width = 400
ratio = new_width / OriginalWidth

# Then we multiply the ratio with height of the original image
# to get a new height that maintains the same aspect ratio
new_height = int(OriginalHeight * ratio) # must be integer

# This then gives a new dimension for the new image that
# sets the width to 400 pixels and maintains the the image aspect ratio

# define new dimension
new_dim = (new_width, new_height)

# show new dimension
print('Dimensions of the new image will be: \n height: {}'' \n width: {}'
       .format(new_dim[1], new_dim[0]))

# resize the image according to new dimensions
resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

# display resized image
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# resizing the image to arbitrary values

# define new dimensions of  500 * 500 square
new_width, new_height = 500, 500

# set new dimensions
new_dim = (new_width, new_height)

# resize the image according to new dimensions
resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

#  draw square round the image edge
cv2.rectangle(resized, (0,0), (new_height, new_width), (0, 0, 0), 3)

# display resized image
cv2.imshow("Square Image", resized)
cv2.waitKey(0)

# Rather than calcuating the aspect ratio each to avoid image
# distortion, we can use the imutils convenience function
#which *automatically* maintains theaspect ratio

# resize image to have height of 200
resized = imutils.resize(image, height=200)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)

# construct the list of interpolation methods in OpenCV
methods = [
           ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
           ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
           ("cv2.INTER_AREA", cv2.INTER_AREA),
           ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
           ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]


#loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 3x using the current
    # interpolation method
    resized = imutils.resize(image, width=OriginalHeight * 3,
                             inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
