#TASK-3 : ADD gray scale image and binay image

from typing import final
import cv2
img1 = cv2.imread('gray.jpg')
img2 = cv2.imread('image_binary.jpg')

Final_img = cv2.add(img1, img2)

cv2.imwrite("final.jpg", Final_img)
cv2.imshow("Combined image", Final_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
