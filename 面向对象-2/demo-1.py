# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#     def say(self):
#         p = self.__class__('tanyajuan',20)
#         print(p.name,p.age)
#         print('my name is %s,age is %d'%(self.name,self.age))
#
# p = Person('donghao',20)
#
# p.say()
# print(p.__class__)
class Person(object):
    def __init__(self,money):
        self.__money = money

    def setmoney(self,money):
        if money<0:
            money = 0
        self.__money = money

    def getmoney(self):
        return self.__money


p = Person(200)

p.setmoney(-1)
p._Person__money = 200
print(p.getmoney())
print(p.__dict__)