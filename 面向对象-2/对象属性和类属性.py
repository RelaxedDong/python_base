#encoding:utf-8

# class Person(object):
#     #类属性(类名来调用的属性)
#     name = 'person'
#     # 类名来调用
#     def __init__(self,age):
#         self.age = 20
#
#
# print(Person.name)
#
# p = Person(20)

# print(p.__dict__)

#
# class Man(object):
#     pass
#
# from types import MethodType


# m = Man()
# m.name = 'donghao'
# def say(self):
#     print('my name is %s'% self.name)
#
# m.speak = MethodType(say,m)
#
# m.speak()


# class Person(object):
#     def __init__(self,name,password):
#         self.name = name
#         self.__password = password
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self,password):
#         self.__password = password
#
# p = Person('donghao','1234566')
#
#
# print(p.password)

class Person(object):
    def __init__(self,age):
        self.age = age

    def __add__(self, other):
        return Person(self.age+other.age)

    def __str__(self):
        return 'age sum is %d'%self.age

p1 = Person(1)
p2 = Person(3)
print(p1+p2)
