#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 11:40

# 线程可以标记为“守护程序线程”。这个标志的意义在于，当只剩下守护进程线程时，整个Python程序都会退出。
# 初始值继承自创建线程。可以通过daemon属性或守护进程构造函数参数设置该标志

import time
import threading

class Mythread(threading.Thread):
    def __init__(self,*args,**kwargs):
        super(Mythread, self).__init__()
        self.name = kwargs.get('name')

    def run(self):
        print('fun start')
        time.sleep(3)
        print('fun end')


def f():
    print(threading.current_thread())

if __name__ == '__main__':
    m = Mythread(name='donghao thread', target=f)
    m.setDaemon(True)
    m.start()
    time.sleep(1)
    print('main end')
"""   
CPython实现细节：在CPython中，由于Global Interpreter Lock，只有一个线程可以同时执行Python代码（即使某些面向性能的库可能会克服此限制）。
如果您希望应用程序更好地利用多核计算机的计算资源，建议您使用 multiprocessing或concurrent.futures.ProcessPoolExecutor。
但是，如果要同时运行多个I / O绑定任务，则线程仍然是一个合适的模型
"""