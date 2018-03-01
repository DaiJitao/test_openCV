# _*_ coding:utf-8 _*_


import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),35)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'HELLO',(100,500), font, 4,(255,255,255),2)
winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)