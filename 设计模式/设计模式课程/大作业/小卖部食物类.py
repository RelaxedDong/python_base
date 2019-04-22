#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 20:59
from 基本物品类 import Goods

class Foods(Goods):
    __storage = []
    def add_to_foods(self):
        exists = False
        for good in self.__storage:
            if self.name in good.values():
                good['库存'] += 1
                good['价格'] = self.money
                exists = True
                break
        if not exists:
            self.__storage.append({'食物名称': self.name, '价格': self.money, '库存': 1})

    @classmethod
    def get_storage(cls):
        return cls.__storage


