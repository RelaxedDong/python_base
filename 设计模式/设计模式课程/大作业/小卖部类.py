#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 20:42

from 小卖部大门类 import CanteenGate
from 小卖部文具类 import Stationery
from 小卖部食物类 import Foods


class FoodsFactory(object):
    """食品工厂"""
    @staticmethod
    def create_foods(name, money):
        return Foods(name, money)




class StationeryFactory(object):
    """文具工厂"""
    @staticmethod
    def create_staionery(name, money):
        return Stationery(name, money)


class CanteenFactory(object):
    """小卖部类"""
    def __init__(self,name):
        self.name = name

    def show(self):
        """装饰模式，装饰小卖部"""
        print('*'*10,'开始装扮 %s'%self.name,'*'*10)

    @staticmethod
    def create_canteen(fill_with_type):
        if fill_with_type == '大门':
            "单例模式"
            return CanteenGate()

        elif fill_with_type == '食品':
            return FoodsFactory()

        elif fill_with_type == '文具':
            return StationeryFactory()








