#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 22:02

#单例模式
# 目的：让类创建对象，在系统中只有唯一一个实例
# 每一次执行 类名（）返回的对象，内存地址都是相同的

# __new__方法
#1.在内存中为对象分配内存空间
#2.返回对象的引用

# python解释器 获得对象的引用后，将引用作为第一个参数，传递给__init__方法
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('我执行了')
        print(cls)
        # return super(Person, cls).__new__(cls)
        return object.__new__(cls)


    def __init__(self,name):
        self.name = name
class Man(Person):
    def __init__(self,name):
        super(Man, self).__init__(name)

    def __new__(cls, *args, **kwargs):
        return super(Man, cls).__new__(cls)


p = Man('donghao')
p.name

