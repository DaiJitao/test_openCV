# _*_ coding:utf-8 _*_

import cv

def get_max_area(data):
    length = len(data)
    dict_data = dict()
    for i in range(length):
        if i == 0:
            for j in range(i + 1, length):
                for s in range(j+1):
                    dict_data[j] = min()