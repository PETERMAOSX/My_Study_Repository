import numpy as np 
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#录制视频
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,2)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()