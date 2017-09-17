#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年9月2日
有若干个个位数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
@author: xrf
'''
def Three_digits(digits):
    if len(digits) < 3:
        return 0,[]
    list = []
    for i in digits:
        digits1= [b for b in digits if b != i]
        for j in digits1:
            digits2 = [p for p in digits1 if p != j]
            for k in digits2:
                if i*100+j*10+k not in list:
                    list.append(i*100+j*10+k)
    return len(list),list


if __name__ == '__main__':
    print(Three_digits([1,2,4,9,8]))

