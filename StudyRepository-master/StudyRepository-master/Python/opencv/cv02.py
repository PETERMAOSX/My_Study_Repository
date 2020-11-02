import cv2
import numpy as np 
img = cv2.imread('img2.png',1)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k is 27:
    cv2.destroyAllWindows()
elif k is ord('s'):
    cv2.imwrite('test1.png',img)
    cv2.destroyAllWindows()