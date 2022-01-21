#Task 1 : Convert RBG Image to gray scale and also find the matrices of image

# Import the necessary libraries
from PIL import Image
import cv2
import numpy
from numpy import asarray


# load the image and convert into
# numpy array
img = Image.open('Nazuko.jpg')
numpydata = asarray(img)
np_img = numpy.array(img)

#Size of Image
print(np_img.shape)

# data
print(numpydata)

#convert to gray scale image
# Load the input image
image = cv2.imread('Nazuko.jpg')

cv2.imshow('Original', image)
cv2.waitKey(0)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('Nazuko_Gray.jpg', gray_image) 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0) 
 
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
