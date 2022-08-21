#simple program to read and show an image
import cv2

img = cv2.imread("E:\WORKSPACE\PYTHON PROJECT\CODING BLOCKS\image\space.jpg")



cv2.imshow('image',img)
cv2.waitKey(1)
cv2.destroyAllWindows()