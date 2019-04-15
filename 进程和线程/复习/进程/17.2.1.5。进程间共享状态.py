#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 10:11

# 在进行并发编程时，通常最好尽量避免使用共享状态。使用多个进程时尤其如此。
#


# 但是，如果您确实需要使用某些共享数据，那么 multiprocessing提供了几种方法。
# 共享内存


# 可以使用Value或 将数据存储在共享存储器映射中Array。例如，以下代码
from multiprocessing import Value,Process,Array

"""

def f(n,arr):
    n.value = 3.14
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':
    n = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f,args=(n,arr))
    p.start()
    p.join()
    print(n.value)
    print(arr[:])
    
"""

# 服务器进程
# Manager()控制器返回的管理器对象控制一个服务器进程，该进程保存Python对象并允许其他进程使用代理操作它们。
# 通过返回的经理Manager()将支持类型 list，dict，Namespace，Lock， RLock，Semaphore，
# BoundedSemaphore， Condition，Event，Barrier， Queue，Value和Array
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)

# 服务器进程管理器比使用共享内存对象更灵活，因为它们可以支持任意对象类型。
# 此外，单个管理器可以通过网络由不同计算机上的进程共享。但是，它们比使用共享内存慢。