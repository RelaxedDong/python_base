#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 21:12

from 小卖部类 import CanteenFactory
from 小卖部文具类 import Stationery
from 小卖部食物类 import Foods
from 小卖部装饰 import *



def main():
    nyist_canteen = CanteenFactory('理工软件学院董豪小卖部')

    stationery = nyist_canteen.create_canteen('文具')
    food = nyist_canteen.create_canteen('食品')

    while True:
        try:
            # fac_type = int(input('请输入物品类型(1.添加食品，2.添加文具, 3.文具查询，4.食品查询，5.添加大门,6.装饰)'))
            fac_type = int(input('\033[32;1m[请输入物品类型(1.添加食品，2.添加文具, 3.文具查询，4.食品查询，5.添加大门,6.装饰]\033[10m'))

        except Exception as e:
            print('输入错误, 请重新输入...')
        else:
            if fac_type == 1:
                name = input('请输入食品名称')
                try:
                    money = float(input('请输入食品价格'))
                except Exception as e:
                    print('金额错误，请重新输入')
                    continue
                newfood = food.create_foods(name, money)
                newfood.add_to_foods()
            if fac_type == 2:
                name = input('请输入文具名称')
                try:
                    money = float(input('请输入文具价格'))
                except Exception as e:
                    print('金额错误，请重新输入')
                    continue
                good = stationery.create_staionery(name, money)
                good.add_to_stationery()
            elif fac_type == 3:
                store = Stationery.get_storage()
                if store:
                    print(store, end='\n')
                else:
                    print('没有存货')
            elif fac_type == 4:
                print(Foods.get_storage(), end='\n')
            elif fac_type == 5:
                door = nyist_canteen.create_canteen("大门")
                print('创建大门实例')
                # print('大门id', id(door))
                print('\033[31;1m[大门]%s，id(%s)\033[0m' % (nyist_canteen.name, id(door)))
            elif fac_type == 6:
                roof = Roof()
                foot = Footer()
                roof.decorate(nyist_canteen)
                foot.decorate(nyist_canteen)
                roof.show()
                foot.show()

if __name__ == '__main__':
    main()


