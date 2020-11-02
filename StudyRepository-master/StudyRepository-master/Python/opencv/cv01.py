import cv2
#打开一张图片 imread('name',if 0 is grey 1 is colorful)
cv2.namedWindow("test",cv2.WINDOW_AUTOSIZE)
img = cv2.imread('img2.png',1)
cv2.imshow('test',img)
cv2.waitKey(0)
if cv2.waitKey(2) == ord('q'):
    cv2.destroyAllWindows()