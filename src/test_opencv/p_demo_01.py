# _*_ coding:utf-8 _*_

from PIL import Image
from pylab import *
import os

def get_imlist(path):
    """返回目录中所有的JPG图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
basePath = r'D:\QQfiles\976185561\Image\Group\Image3'
data = get_imlist(basePath)


im = array(Image.open(data[0]))
imshow(im)
print "Please click 3 points"
x = ginput(3)
print "you clicked:", x
show()