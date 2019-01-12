#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 16:19

class Animal(object):
    def eat(self):
        print('吃')
    def sleep(self):
        print('睡')
    def xx(self):
        print('我执行了1')
class Dog(Animal):
    def brak(self):
        print('咬')
# 继承：子类拥有父类的所有方法
    def xx(self):
        print('我执行了2')
class SuperDog(Dog):
    def fly(self):
        print('fly')
    #重写方法（父类方法不能实现的方法）
    def sleep(self):
        print('超级能睡')
        super().sleep()

xiaotianqian = SuperDog()
xiaotianqian.fly()
xiaotianqian.sleep()
xiaotianqian.xx()

# Dog类是Animal类的派生类
# Animal是Dog类的基类
# Dog类从Aniaml派生



#对父类方法进行扩展
# super（）就是使用super类创建的对象
# 最常用的就是  重写父类的方法是，调用父类中封装方法的实现
