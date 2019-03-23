# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 17:19
# 基于__new__方法实现
"""
class Singleton(object):
    __instance = None
    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

b = Singleton('donghao')
a = Singleton('donghao')
print(id(b))
print(id(a))
"""


# 基于装饰器实现
def funSingle(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


@funSingle
class Singleton(object):
    a = 123

    def __init__(self, x='donghao'):
        self.name = x
