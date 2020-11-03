import cv2
import dlib
from skimage import io

# 使用特征提取器get_frontal_face_detector
detector = dlib.get_frontal_face_detector()
# dlib的68点模型，使用作者训练好的特征预测器
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 图片所在路径
img = io.imread("2.jpg")
# 生成dlib的图像窗口
win = dlib.image_window()
win.clear_overlay()
win.set_image(img)

# 特征提取器的实例化
dets = detector(img, 1)
print("人脸数：", len(dets))

for k, d in enumerate(dets):
        print("第", k+1, "个人脸d的坐标：",
              "left:", d.left(),
              "right:", d.right(),
              "top:", d.top(),
              "bottom:", d.bottom())

        width = d.right() - d.left()
        heigth = d.bottom() - d.top()

        print('人脸面积为：',(width*heigth))