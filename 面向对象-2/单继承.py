class Person(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money

    def run(self):
        print('run')

    def eat(self,food):
        print('eat food '+food)

    def setmoney(self,money):
        self.__money = money


    def getmoney(self):
        return self.__money

class Student(Person):
    def __init__(self,name,age,money):
        #调用父类中的init
        self.name = 'tayajuan'
        super(Student, self).__init__(name,age,money)

    def Attrumoney(self):
        print(self.money)


s = Student('donghao',20,100)
print(s.__dict__)
print(s.getmoney())

s.setmoney(123456)
print(s.getmoney())
# s.Attrumoney()