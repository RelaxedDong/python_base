#encoding:utf-8
#__author__ = 'donghao'
#__time__ = 2019/1/11 21:16

# def func():
#     '''测试函数'''
#     print('hello python')
#
#
# [print(i+'\n') for i in dir(func)]
# print(func.__doc__) #'''测试函数'''
# class Person(object):
#     def __init__(self,name):
#         print('我执行了__init__')
#         self.name = name
#         #实例化对象，调用方法
#     def __new__(cls, *args, **kwargs):
#         print('我执行了__new__')
#         #创建对象时，调用的方法
#         return object.__new__(cls)
#
#     # 第一个参数cls是当前正在实例化的类。
#     #
#     # 如果要得到当前类的实例，应当在当前类中的
#     # __new__()
#     # 方法语句中调用当前类的父类的
#     # __new__()
#     # 方法。
#     # 　　例如，如果当前类是直接继承自
#     # object，那当前类的
#     # __new__()
#     # 方法返回的对象应该为：
#
#
#     def __del__(self):
#         print('销毁对象%s'%self.name)
#
#     def __str__(self):
#         return '我是对象%s'%self.name
#
# p1 = Person('1')
# p2 = Person('2')
# p3 = Person('3')
# print(p1,p2,p3)

class Animal(object):
    count = 0
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        print(args,kwargs)
        # print('动物类__new__')
        cls.count+=1
        # print('我执行了%d'%cls.count)
        return super(Animal, cls).__new__(cls)
    def __call__(self, *args, **kwargs):
        print('hahaha')

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)

    def __new__(cls, *args, **kwargs):
        print(args,kwargs)
        # print('创建小狗类')
        return super(Dog, cls).__new__(cls, *args, **kwargs)
    def eat(self):
        print(self.it_name,'吃')
dog1= Dog('小狗1')
dog2 = Dog('小狗2')
dog3 = Dog('小狗3')
# 对象dog1,dog2,dog3记录的是记录对象在内存中的地址*(16进制表示)
# 也就是dog1,dog2,dog3引用了新建的Dog对象
# print(dog1) <__main__.Dog object at 0x027D2A50>
print(dog1)
# print('%x'%id(dog1))
dog1.age= 20
mydog = dog1
print(dog1.age)
mydog.age = 100
print(mydog.age)
print(dog1.age)
dog2.it_name = '小狗汪汪'
dog2.eat()
