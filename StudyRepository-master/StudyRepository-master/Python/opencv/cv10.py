import numpy as np 
import cv2
cap = cv2.VideoCapture(0)
ret = cap.set(3,1024)
ret = cap.set(4,720)
while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) is ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
