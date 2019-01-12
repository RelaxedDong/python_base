#encoding:utf-8

import threading
import time
local = threading.local()
local.a = 10

# def run():
#     print('子线程(%s)启动'%threading.current_thread().name)
#     global a
#     a +=1
#     time.sleep(2)
#     print('开始打印')
#     time.sleep(1)
#     print('开始保存')
#     time.sleep(1)
#     print('子线程结束')


def run(n):
    local.a = 200
    print(local.a)


if __name__ == '__main__':
    #任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程
    #current_thread返回当前线程的实例
    print('主线程(%s)启动！'%(threading.current_thread().name))

    # 创建子线程
    #name指线程的名称
    t1 = threading.Thread(target=run,name='donghao1',args=(6,))
    t1.start()
    print(local.a)

    t1.join()
    print('主线程(%s)结束！'%(threading.current_thread().name))

