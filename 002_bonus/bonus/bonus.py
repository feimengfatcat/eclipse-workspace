#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年9月2日
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
@author: xrf
'''
def bonus(num):
    total = 0
    if num < 0:total = 0
    numlist = [100000, 100000, 200000, 200000, 400000,0]
    perlist = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    for i, j in zip(numlist, perlist):
        if num > i:
            total += i*j
            num -= i
        else:
            total += num*j
            break
    return total


if __name__ == '__main__':
    print bonus(1000000)