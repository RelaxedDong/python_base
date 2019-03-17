#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/17 21:57
# multiprocessing包含所有同步原语的等价物threading。例如，可以使用锁来确保一次只有一个进程打印到标准输出
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

# 不使用来自不同进程的锁输出容易被混淆。