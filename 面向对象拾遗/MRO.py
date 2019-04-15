#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/15 11:13
#
#
#
# class Parent(object):
#     def __init__(self,name):
#         print('parent 开始调用')
#         self.name = name
#         print('Parent 调用完成')
#
#
#
# class Son1(Parent):
#     def __init__(self,name,age):
#         print('Son1 调用')
#         self.age = age
#         Parent.__init__(self,name)
#         print('Son1 调用完成')
#
#
# class Son2(Parent):
#     def __init__(self,name,gender):
#         print('Son2 调用')
#         self.gender = gender
#         Parent.__init__(self, name)
#         print('Son2 调用完成')
#
#
#
# class Grandson(Son1,Son2):
#     def __init__(self,name,gender,age):
#         print('Grandson 调用')
#         self.gender = gender
#         self.age = age
#         Son1.__init__(self,name,age) #单独调用父类方法
#         Son2.__init__(self,name,gender)
#         print('Grandson 调用完成')
#
# s = Grandson('123','男',19)



#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/15 11:13



class Parent(object):
    def __init__(self,name,*args,**kwargs):
        print('parent 开始调用')
        self.name = name
        print('Parent 调用完成')

class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        print('Son1 调用')
        self.age = age
        super().__init__(self,name,*args,**kwargs)
        print('Son1 调用完成')

class Son2(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print('Son2 调用')
        self.gender = gender
        super().__init__(self,name,*args,**kwargs)
        print('Son2 调用完成')

class Grandson(Son1,Son2):
    def __init__(self,name,gender,age):
        print('Grandson 调用')
        self.gender = gender
        self.age = age
        # super().__init__(name,gender,age) #  == super(Grandson, self).__init__(name,gender)
        super(Son1,self).__init__(name,age,gender)
        print('Grandson 调用完成')

s = Grandson('donghao','男',19)
print(Grandson.__mro__)
"""
(<class '__main__.Grandson'>, 
<class '__main__.Son1'>, 
<class '__main__.Son2'>, 
<class '__main__.Parent'>, 
<class 'object'>)
"""

"""
Grandson 调用
Son1 调用
Son2 调用
parent 开始调用
Parent 调用完成
Son2 调用完成
Son1 调用完成
Grandson 调用完成



super(Son1, self).__init__(name,gender,age)
Grandson 调用
Son2 调用
parent 开始调用
Parent 调用完成
Son2 调用完成
Grandson 调用完成
"""