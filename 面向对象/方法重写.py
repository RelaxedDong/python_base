#encoding:utf-8
'''
	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
'''
class Person(object):
    school = "默认school"
    def __init__(self,name,age,gender):
        self.gender = gender
        self.name = name
        self.age = age
    def __str__(self):
        return "名字是：%s,年龄是：%s,性别是：%d"%(self.name,self.age,self.gender)
p1 = Person('donghao',18,0)
#打印全部属性
print(p1.name,p1.age,p1.gender)
print(p1)


class Parent():
    def parentmethod(self):
        print('parent方法')
class Son(Parent):
    def child(self):
        print('son方法')
son = Son()
son.parentmethod()
'''
下表列出了一些通用的功能，你可以在自己的类重写：
序号	方法, 描述 & 简单的调用
1	__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)'''


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')



class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')



c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法