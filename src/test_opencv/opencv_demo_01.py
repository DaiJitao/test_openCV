# _*_ coding:utf-8 _*_

import cv2
import numpy as np

img = np.zeros((3,3), dtype=np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


imag_file = r'D:\temp\ss.png'
img = cv2.imread(imag_file)
print img
save_path = 'D:\\temp\\'
# cv2.imwrite(save_path + 'test.jpg', img)
cv2.imshow("my image", img)
cv2.waitKey()
cv2.destroyAllWindows()