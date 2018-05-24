#coding:utf-8

import cv2
import numpy as np

nose_path = r"E:\pycharm_workspace\machine_learning\test_openCV\resource\ml_instances\Chapter10\cascade_files\haarcascade_mcs_nose.xml"
eye_path = r"E:\pycharm_workspace\machine_learning\test_openCV\resource\ml_instances\Chapter10\cascade_files\haarcascade_eye.xml"
face_path = r"E:\pycharm_workspace\machine_learning\test_openCV\resource\ml_instances\Chapter10\cascade_files\haarcascade_frontalface_alt.xml"
# 导入人脸检测级联文件
face_cascade = cv2.CascadeClassifier(face_path) # 人脸检测
eye_cascade = cv2.CascadeClassifier(eye_path)
nose_cascade = cv2.CascadeClassifier(nose_path)

if face_cascade.empty():
    raise IOError("脸部级联文件无法加载！")
# 检查眼睛级联文件是否加载
if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade classifier xml file')
# 检查鼻子级联文件是否加载
if nose_cascade.empty():
    raise IOError('Unable to load the nose cascade classifier xml file')

cap = cv2.VideoCapture(0)
scaling_factor = 0.7


while True:
    ref, frame = cap.read()
    # 调整帧的大小
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,interpolation=cv2.INTER_AREA)
    # 将图像转为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 在灰度图像上运行人脸检测器
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 在脸部画出矩形
    for (x, y, w, h) in face_rects:
        # 从彩色与灰度图中提取人脸ROI信息
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # 在灰度图ROI信息中检测眼睛
        eye_rects = eye_cascade.detectMultiScale(roi_gray)
        # 在灰度图ROI信息中检测鼻子
        nose_rects = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)
        # 在眼睛周围画绿色的圈
        for (x_eye, y_eye, w_eye, h_eye) in eye_rects:
            center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5 * h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0, 255, 0)
            thickness = 3
            cv2.circle(roi_color, center, radius, color, thickness)

        for (x_nose, y_nose, w_nose, h_nose) in nose_rects:
            cv2.rectangle(roi_color, (x_nose, y_nose), (x_nose + w_nose,
                                                        y_nose + h_nose), (0, 255, 0), 3)
            break
    cv2.imshow("Webcam", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
