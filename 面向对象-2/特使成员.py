# encoding:utf-8

# __getitem__、__setitem__、__delitem__
#
# 用于索引操作，如字典。以上分别表示获取、设置、删除数据
# class Foo(object):
#     def __getitem__(self, item):
#         print('__getitem__',item)
#
#     def __setitem__(self, key, value):
#         print('setitem',key,value)
#
#     def __delitem__(self, key):
#         print('delitem',key)
#
#
# obj = Foo()
# result = obj['hahahahaha']
#
# obj['k2'] = 'donghao'
#
# del obj['k1']

#
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     def __call__(self, *args, **kwargs):
#         print('我执行了')
#
#
# p = Person('donghao')()


# 该三个方法用于分片操作，如：列表  python2写法
# __getslice__、__setslice__、__delslice__


# class Foo(object):
#
#     def __setslice__(self, i, j, sequence):
#         print('__setslice__', i, j)
#
#
#     def __delslice__(self, i, j):
#         print('__delslice__', i, j)
#
# obj = Foo()
#
# obj[-1:1]  # 自动触发执行 __getslice__
# obj[0:1] = (11, 22, 33, 44)  # 自动触发执行 __setslice__
# del obj[0:2]  # 自动触发执行 __delslice__
# python3:
# -*- coding:utf-8 -*-
# File Name:slice_operator.py
# Created Time:2018-12-31 17:50:31


# class Foo(object):
#
#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             print("Get slice---------> start: %s, stop: %s, step: %s." \
#                   % (str(index.start), str(index.stop), str(index.step)))
#
#     def __setitem__(self, index, value):
#         if isinstance(index, slice):
#             print("Set slice---------> start: %s, stop: %s, step: %s." \
#                   % (str(index.start), str(index.stop), str(index.step)))
#             print("\tThe value is:", value)
#
#     def __delitem__(self, index):
#         if isinstance(index, slice):
#             print("Delete slice------> start: %s, stop: %s, step: %s." \
#                   % (str(index.start), str(index.stop), str(index.step)))
#
#
# if __name__ == "__main__":
#     obj = Foo()
#     obj[-1:10]
#     obj[-1:10:1] = [2, 3, 4, 5]
#     del obj[-1:10:2]

# class Foo(object):
#
#     def __init__(self, sq):
#         self.sq = sq
#
#     def __iter__(self):
#         return iter(self.sq)
#
# obj = Foo([11,22,33,44])
#
# for i in obj:
#     print(i)


# __new__
# 和
# __metaclass__


# class Foo(object):
#
#     def __init__(self):
#         pass
#
#
# obj = Foo()  # obj是通过Foo类实例化的对象
#
# print(type(obj))
# print(type(Foo))

# .特殊方式（type类的构造函数）

# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# Person = type('Person',(object,),{'__init__':__init__})
#
# class p(Person):
#     def __init__(self,name,age):
#         Person.__init__(self,name,age)
#
#
# cas = p('donghao',20)
# print(cas.__dict__)

# 等于运算
