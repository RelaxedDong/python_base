#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/22 10:32

from 小卖部类 import CanteenFactory

class DcorateHouse(object):
    def __init__(self):
        self.component = None

    def decorate(self,component):
        self.component = component

    def show(self):
        if self.component:
            self.component.show()

class Roof(DcorateHouse):
    def show(self):
        super(Roof, self).show()
        print('盖房子')


class Footer(DcorateHouse):
    def show(self):
        super(Footer, self).show()
        print('铺地板')

