#encoding:utf-8
#访问受限
class Person(object):
    @property
    def name(self):
        return self.__age


    def __init__(self):
        self.__age = 123


    @name.setter
    def age(self,age):
        self.__age = age


p = Person()
p.age = 50

print(p.age)