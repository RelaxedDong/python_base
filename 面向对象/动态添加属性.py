#encoding:utf-8


class Person(object):
    pass


per = Person()
per.name = 'donghao'
# print(per.name)

#动态添加方法
def speak(self):
    print('xxxxxx'+self.name)
from types import MethodType
# per.say = speak(per)

per.say = MethodType(speak,per)

#限制实例属性的方法
# 例如：只允许添加name,age属性
class Children(object):
    __slots__ = ("name","age")
p = Children()
p.name = 'donghao'
print(p.name)
p.age = 10
print(p.age)