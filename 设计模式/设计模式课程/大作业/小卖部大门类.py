#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 20:46

def InstanceObject(f):
    __instance = {}
    def inner(*args,**kwargs):
        if not f in __instance:
            __instance[f] = f(*args,**kwargs)
        return __instance[f]
    return inner


#构建小卖部大门类，这里使用装饰器实现。
@InstanceObject
class CanteenGate(object):
    def open_door(self):
        print('小卖部开门了...')


    def close_door(self):
        print('小卖部关门...')


