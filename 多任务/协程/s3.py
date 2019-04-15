# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2018/1/24 15:59
# # @Author  : Py.qi
# # @File    : gevent_noe.py
# # @Software: PyCharm
# import gevent
#
# def foo():
#     print('running in foo')
#     gevent.sleep(2)
#     print('com back from bar in to foo')
# def bar():
#     print('running in bar')
#     gevent.sleep(2)
#     print('com back from foo in to bar')
#
# gevent.joinall([      #创建线程并行执行程序，碰到IO就切换
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])