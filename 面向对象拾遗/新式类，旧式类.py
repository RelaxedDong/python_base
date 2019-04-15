#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 17:05

#dir()   查看内置属性和方法

# 新式类：object为基类  拥有object内置属性和方法


#旧式类（经典类，不推荐使用）
# 在python2中 只有__doc__ , '__module__内置方法'
# __module__ :
# 如果当前模块为顶层模块执行 则打印__main__
# 如果当前模块为被调用模块的时候 打印当前模块的名称


# 如果在python3中没有指定父类，会默认使用object作为基类
# 新式类和经典类在多继承时，==会影响到方法搜索顺序

class B:
    '''说明'''
    def __init__(self,name):
        self.name = name
b = B('donghao')
# print(b.__doc__)用于描述该对象的作用
print(b.__module__)
print(b.__name__)