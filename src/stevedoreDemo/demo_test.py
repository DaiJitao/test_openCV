# __*__ coding:utf-8 __*__
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=False)
print '默认模式：',"/ ".join(seg_list)

seg_list = jieba.cut("小明1995年毕业于清华大学")
print '/ '.join(seg_list)

seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=True)
print "Full mode ", '/ '.join(seg_list)

seg_list = jieba.cut_for_search("小明1995年毕业于清华大学")
print '搜索引擎模式：', '/'.join(seg_list)

def savefile(savepath, content):
    """保存文件"""
    fp = open(savepath, "wb")
    fp.close();

def readfile(path):
    """读取文件"""
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    return content


def deco(func):
	def inner():
		print "running inner()"
	return inner

@deco
def target():
	print "running target()"


registry = []
def register(func):
	print 'runninr register(%s)'  %func
	registry.append(func)
	return func

@register
def f1():
	print 'running f1()'

@register
def f2():
	print 'running f2()'

def f3():
	print 'running f3()'

def main():
	print 'running main()'
	print 'registry -> ', registry


if __name__ == '__main__':
	import pdb
	pdb.set_trace()
	main()




