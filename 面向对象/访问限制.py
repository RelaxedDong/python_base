class Person(object):
    __money = 0
    school = "默认school"
    def __init__(self,name,age,gender,money):
        self.__money = money
        self.gender = gender
        self.name = name
        self.age = age
        self.__money = money
    def __str__(self):
        return "名字是：%s,年龄是：%s,性别是：%d"%(self.name,self.age,self.gender)
    def setmoney(self,money):
        if money<0:
            money = 0
        self.__money = money
    def getmoney(self):
        print(self.__money)
        return self.__money
p1 = Person('donghao',18,0,1000)

#打印全部属性
print(p1.name,p1.age,p1.gender)

p1.setmoney(12)
p1.getmoney()

#通过内部方法，修改私有属性
#通过自定义的方法实现对室友属性的赋值与取值

print(hasattr(p1,'name'))
'''
你也可以使用以下函数的方式来访问属性：
    getattr(obj, name[, default]) : 访问对象的属性。
    hasattr(obj,name) : 检查是否存在一个属性。
    setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
    delattr(obj, name) : 删除属性。
'''



