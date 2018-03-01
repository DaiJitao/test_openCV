# _*_ coding:utf-8 _*_

from PIL import Image
import os
from pylab import *

basePath = r'D:\QQfiles\976185561\Image\Group\Image3'
pil_img = Image.open(basePath + "\\001.jpg")
print pil_img
print pil_img.convert('L')

def get_imlist(path):
    """返回目录中所有的JPG图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

data = get_imlist(basePath)
print len(data)
print data[0]

im = array(Image.open(data[4]).convert('L'))
print "im:", im
imshow(im)
x = [100,100,400,400]
y = [200,500,200,500]
plot(x,y, 'r*', 10)
plot(x[:2], y[:2], 'r--')
title('Plotting: "empire.jpg"')
show()