# import OpenCV
import cv2

# # load an display the original image
image = cv2.imread('logo.jpg')
# cv2.imshow("Original", image)
# cv2.waitKey(0)

# # flip the image horizontally
# flipped = cv2.flip(image, 1)
# cv2.imshow("Flipped Horizontally", flipped)
# cv2.waitKey(0)

# # flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
# cv2.waitKey(0)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)





