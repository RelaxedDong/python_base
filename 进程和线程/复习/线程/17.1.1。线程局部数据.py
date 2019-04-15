#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 11:32
import threading

# 线程局部数据是其值是线程特定的数据。要管理线程本地数据，只需创建一个local（或子类）实例并在其上存储属性：

local = threading.local()

local.a = 10

def f():
    local.a = 20
    print('线程中',local.a)


if __name__ == '__main__':
    t = threading.Thread(target=f)
    t.start()
    t.join()
    print(local.a)