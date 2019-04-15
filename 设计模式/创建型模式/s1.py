#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/4 11:38

class Singleton(object):
    a = 123

    def __init__(self, x='donghao'):
        self.name = x

a = Singleton('1')
