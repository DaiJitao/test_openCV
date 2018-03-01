# _*_ coding:utf-8 _*_

import cv2
import numpy as np

img = np.zeros((3,3), dtype=np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


imag_file = r'D:\temp\ss.png'
img = cv2.imread(imag_file)
cv2.imshow("show", img)
k = cv2.waitKey(0) # 等待键盘的输入

print chr(k)
save_path = 'D:\\temp\\'
# cv2.imwrite(save_path + 'test.jpg', img)
# cv2.imshow("my image", img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# 保存图像
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    grayImage = cv2.imread(imag_file, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(save_path + 'test02.jpg', grayImage)


