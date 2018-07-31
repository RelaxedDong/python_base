from 访问限制 import Person

class Student(Person):
    def __init__(self,name,age,gender,stuid,money):
        super(Student, self).__init__(name,age,gender,money)
        self.stuid = stuid
    def func(self):
        print(self.__money)
stu = Student('donghao',20,1,1000,123456)
print(stu.func())

# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub, sup)
# isinstance(obj, Class)
# 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
