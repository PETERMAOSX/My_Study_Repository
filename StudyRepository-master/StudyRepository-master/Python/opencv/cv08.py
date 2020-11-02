import cv2
import numpy as np 
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
img = np.zeros((1024,1024,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(2) == 27:
        break
cv2.destroyAllWindows() 