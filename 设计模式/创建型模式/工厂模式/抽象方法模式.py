# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 18:29
"""
定义:定义一个创建对象的接口(工厂接口),让子类决定实例化哪个接口

     角色:抽象工厂角色,具体工厂角色,抽象产品角色,具体产品角色

     适用场景:需要生产多种,大量复杂对象的时候,需要降低代码耦合度的时候,当系统中的产品类经常需要扩展的时候

     优点:每个具体的产品都对应一个具体工厂,不需要修改工厂类的代码,工厂类可以不知道它所创建的具体的类,隐藏了对象创建的实现细节

     缺点:每增加一个具体的产品类,就必须增加一个相应的工厂类
"""


class LeiFeng():
    def buy_rice(self):
        pass

    def sweep(self):
        pass


class Student(LeiFeng):
    def buy_rice(self):
        print('大学生帮你买米')

    def sweep(self):
        print('大学生帮你扫地')


class Volunteer(LeiFeng):
    def buy_rice(self):
        print('社区志愿者帮你买米')

    def sweep(self):
        print('社区志愿者帮你扫地')


class LeiFengFactory():
    def create_lei_feng(self, type):
        map_ = {
            '大学生': Student(),
            '社区志愿者': Volunteer()
        }
        return map_[type]


if __name__ == '__main__':
    leifeng1 = LeiFengFactory().create_lei_feng('大学生')
    leifeng2 = LeiFengFactory().create_lei_feng('社区志愿者')
    leifeng1.buy_rice()
    leifeng1.sweep()
    leifeng2.buy_rice()
    leifeng2.sweep()
