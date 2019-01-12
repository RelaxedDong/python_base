#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 16:54

class Father(object):
    def __init__(self):
        self.gender = '男'

    def drink(self):
        print('Father喝')
class Mother(object):
    def __init__(self):
        self.gender = '女'
    def drink(self):
        print('Mother喝')

class Children(Mother,Father):
    def __init__(self):
        super(Children, self).__init__()

    def drink(self):
        print('我喝')
        super(Children, self).drink()

c = Children()
c.drink()
print(c.gender)

# MRD ：method resolution order
# python中针对类提供了一个内置属性，__mro__可以查看方法搜索顺序
# print(Children.__mro__)
# (<class '__main__.Children'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>)
# 如果最后一个类没找到，就会报错