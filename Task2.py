#TASK-2 :convert pixel of grayscale image to either 1 or 0 (Binerization)
#TASK-3 : ADD gray scale image and binay image

import numpy as np 
import cv2

# Read color image
img = cv2.imread('Nazuko.jpg')

# Get the image's height, width, and channels
height, width, channels = img.shape

# Create blank Binary Image
img_binary = np.zeros((height,width,1))

# Create grayscale image
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print img_grayscale.shape
(thresh, img_binary) = cv2.threshold(img_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Write image
cv2.imwrite('image_binary.jpg',img_binary)
cv2.imwrite('gray.jpg',gray_image)
# View image
cv2.imshow('Grayscale', gray_image)
cv2.imshow('image',img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()