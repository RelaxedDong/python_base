#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/19 15:02
# 定义一个延迟属性的一种高效方法是通过使用一个描述器类，如下所示：
class Lazyproperty:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            print('value is',value)
            setattr(instance,self.func.__name__,value)
            return value


import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        # print('computing area')
        return math.pi*self.radius**2

    @Lazyproperty
    def perimeter(self):
        # print('computing perimeter')
        return 2*math.pi*self.radius

c = Circle(4)
# print(c.radius)
# print(c.area)
# print(c.area)
# print(c.area)
# print(c.perimeter)
# print(c.perimeter)
print(vars(c))
print(c.area)
print(c.perimeter)
print(vars(c))

#不允许修改属性值
# def lazyproperty(func):
#     name = '_lazy_' + func.__name__
#     @property
#     def lazy(self):
#         if hasattr(self, name):
#             return getattr(self, name)
#         else:
#             value = func(self)
#             setattr(self, name, value)
#             return value
#     return lazy

