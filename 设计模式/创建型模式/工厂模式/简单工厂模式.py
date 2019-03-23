# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 17:39

# 简单工厂模式(Simple Factory Pattern):是通过专门定义一个类来负责创建其他类的实例，
# 被创建的实例通常都具有共同的父类

# 使用：
# 1.不知道用户想要创建什么样的对象
#
# 2.当你想要创建一个可扩展的关联在创建类与支持创建对象的类之间。

# 缺点：
# 但是工厂的职责过重，而且当类型过多时不利于系统的扩展维护。

class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == 'baoma':
            return Baoma('baoma')
        elif car_type == 'benchi':
            return Benchi('benchi')
        elif car_type == 'dazhong':
            return Dazhong('dazhong')


# 现代汽车4s店类
class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)


class Car(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print('%s is moving' % self.name)


class Baoma(Car):
    pass


class Benchi(Car):
    pass


class Dazhong(Car):
    pass


car_store = CarStore()
car = car_store.order('baoma')
car.move()
