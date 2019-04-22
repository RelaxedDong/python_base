#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 19:17

class Person(object):
    """构建消费的用户类"""
    def __init__(self,name,money):
        self.name = name
        self._money = money


class WaterDispenser(object):
    """15教售水机类,  单例模式"""
    _instance = None
    def __init__(self, name, drinkcount = 10):
        self.name = name
        self.drinkcount = drinkcount
        self.__money = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def sell(self, person, drinkmoney):
        if self.drinkcount == 0:
            print('*' * 30, person.name)
            print('售水机没有饮料了...')
            return
        if person._money < drinkmoney:
            print('*' * 30, person.name)
            print('钱不够呀，老弟...')
            return
        person._money -= drinkmoney
        self.__money += drinkmoney
        self.drinkcount -= 1
        print('*' * 30, person.name)
        print('购买饮料成功，花费 %d 元'%drinkmoney)

    def check_money(self,person):
        if person.name == 'admin':
            print('*'*30,'管理员')
            print('售水机共卖了%d元'%self.__money)
            print('剩余饮料数量%d'%self.drinkcount)
        else:
            print('权限错误, 无法查询售水机售额')


#构建普通用户
donghao = Person('donghao',100)
admin = Person('admin',1000)

#创建两个对象，因为单例模式，只有一个对象存在。
waterdispenser = WaterDispenser('售水机1')
waterdispenser2 = WaterDispenser('售水机2')

#我在售水机1  购买饮料
waterdispenser.sell(donghao,4)

#管理员查看售水机1 情况
waterdispenser.check_money(admin)


#我在售水机2  购买饮料
waterdispenser2.sell(donghao,3)

#管理员查看售水机2 情况
waterdispenser2.check_money(admin)


"""输出：
****************************** donghao
购买饮料成功，花费 4 元
****************************** 管理员
售水机共卖了4元
剩余饮料数量9
****************************** donghao
购买饮料成功，花费 3 元
****************************** 管理员
售水机共卖了7元
剩余饮料数量8
"""

"""分析：
用户在不同售水机上消费，单例的存在，其实只是在一个售水机上的操作
"""























