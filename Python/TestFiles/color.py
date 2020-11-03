import numpy as np
import cv2

blue_lower = np.array([100,43,46])
blue_upper = np.array([124,255,255])  #这里是设置颜色
cap = cv2.VideoCapture(0) 

cap.set(3, 320)
cap.set(4, 240)

while 1:
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    # 图像学膨胀腐蚀
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 寻找轮廓并绘制轮廓
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        # 寻找面积最大的轮廓并画出其最小外接圆
        cnt = max(cnts, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (255, 0, 255), 2)
        # 找到物体的位置坐标,获得颜色物体的位置，可以来控制小车的转向
        print(int(x), int(y))
    else:
        pass
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

