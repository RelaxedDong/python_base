#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 15:25
# @Author  : Py.qi
# @File    : greenlet_now.py
# @Software: PyCharm
import greenlet

def A():
    print('a.....')
    g2.switch()  #切换至B
    print('a....2')
    g2.switch()
def B():
    print('b.....')
    g1.switch()  #切换至A
    print('b....2')

g1 = greenlet.greenlet(A) #启动一个线程
g2 = greenlet.greenlet(B)
g1.switch()