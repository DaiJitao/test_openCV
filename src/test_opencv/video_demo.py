# _*_ coding:utf-8 _*_

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print cap.isOpened()
cap.set(3, 800)
print cap.get(3)
print cap.get(4)

fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('D:\\temp\\output.avi',fourcc, 20.0, (640,480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()