#coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
scaling_factor = 0.8

while True:
    ref, frame = cap.read()
    # 调整帧的大小
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()