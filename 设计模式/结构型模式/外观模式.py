# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 19:47
"""
外观模式又叫做门面模式。在面向对象程序设计中，解耦是一种推崇的理念。
但事实上由于某些系统中过于复杂，从而增加了客户端与子系统之间的耦合度。
例如：在家观看多媒体影院时，更希望按下一个按钮就能实现影碟机，电视，音响的协同工作，而不是说每个机器都要操作一遍。
这种情况下可以采用外观模式，即引入一个类对子系统进行包装，让客户端与其进行交互。



外观模式(Facade Pattern)：外部与一个子系统的通信必须通过一个统一的外观对象进行，
为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，
这个接口使得这一子系统更加容易使用。外观模式又称为门面模式，它是一种对象结构型模式。
"""

"""
大话设计模式
设计模式——外观模式
facade_pattern.py
外观模式(Facade Pattern):为子系统中的一组接口提供一个一致界面,此模式定义一个高层接口,使得子系统更加容易是用
"""


# 外观类
class Fund(object):

    def __init__(self):
        self.stocka = StockA()
        self.stockb = StockB()
        self.realty = Realty()

    def buy(self):
        self.stocka.buy()
        self.stockb.buy()
        self.realty.buy()

    def sell(self):
        self.stocka.sell()
        self.stockb.sell()
        self.realty.sell()


# 投资股票A类
class StockA(object):

    def buy(self):
        print('buy StockA')

    def sell(self):
        print('sell StockA')


# 投资股票B类
class StockB(object):

    def buy(self):
        print('buy StockB')

    def sell(self):
        print('sell StockB')


# 投资房地产
class Realty(object):

    def buy(self):
        print('buy Realty')

    def sell(self):
        print('sell Realty')


if __name__ == "__main__":
    fund = Fund()
    fund.buy()
    fund.sell()
