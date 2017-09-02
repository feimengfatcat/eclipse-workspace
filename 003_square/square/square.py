#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年9月2日
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
@author: xrf
'''
import math


def square_num(x, y):
    i = 1
    b = None
    while i:
        if math.sqrt(i + x) == int(math.sqrt(i + x)) and math.sqrt(i + y) == int(math.sqrt(i + y)):
            b = i
            break
        else:
            i += 1
    return b


if __name__ == '__main__':
    print square_num(100, 3681)