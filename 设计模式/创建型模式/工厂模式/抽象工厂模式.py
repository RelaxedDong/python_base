# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 18:11
# 抽象工厂模式(Abstract Factory Pattern):提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类


"""抽象工厂模式的实现"""

import random


class PetShop(object):
    """宠物商店"""

    def __init__(self, animal_factory=None):
        """宠物工厂是我们的抽象工厂。我们可以随意设置。"""
        self.pet_factory = animal_factory

    def show_pet(self):
        """使用抽象工厂创建并显示一个宠物"""
        pet = self.pet_factory.get_pet()
        print("我们有一个可爱的 {}".format(pet))
        print("它说 {}".format(pet.speak()))
        print("我们还有 {}".format(self.pet_factory.get_food()))


# 工厂生产的事物

class Dog(object):

    def speak(self):
        return "汪"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "喵"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "狗食"


class CatFactory(object):

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "猫粮"


# 随机创建合适的工厂
def get_factory():
    """让我们动起来！"""
    return random.choice([DogFactory, CatFactory])()


# 多个工厂显示宠物
if __name__ == "__main__":
    for i in range(4):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

"""优点
 具体工厂类如get_factory在一个应用中只需要初始化一次，这样改动一个具体工厂变得很容易，
只需要改变具体工厂就可以改变整个产品的配置。
 
  具体的创建实例过程与客户端分离，客户端通过他们的抽象接口操纵实例，产品的具体类名也被具体工厂的实现分离，
不会出现在客户端代码中
"""

# 缺点：在新增一个具体工厂就需要增加多个类才能实现
