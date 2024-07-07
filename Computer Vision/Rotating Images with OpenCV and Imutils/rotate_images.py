# import required libraries
import cv2
import imutils

# load image from disk
image = cv2.imread('eiffel_tower.jpg')

# display image
cv2.imshow('Original image', image)
cv2.waitKey(0)

# grab the dimensions of the image and calculate the center of the
# image
height, width = image.shape[:2]
centerX, centerY = (width // 2, height // 2)

# # rotate our image by 45 degrees around the center of the image

# get rotation matrix
M = cv2.getRotationMatrix2D((centerX, centerY), 45, 1.0)

# rotate image
rotated = cv2.warpAffine(image, M, (width, height))

# display image
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

# rotate the image by 90 degrees in clockwise direction
M = cv2.getRotationMatrix2D((centerX, centerY), -90, 0.5)
rotated = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((15, 10), 30, 1.0)
rotated = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Rotated around an  Arbitrary Point", rotated)
cv2.waitKey(0)

# use the imutils function to rotate an image 30 degrees
rotated = imutils.rotate(image, -30)
cv2.imshow("Rotated by 30 Degrees", rotated)
cv2.waitKey(0)

# rotate the image by 30 degrees, ensuring the
# entire rotated image still views in the viewing area
rotated = imutils.rotate_bound(image, -30)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)