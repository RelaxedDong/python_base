#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 13:42
'''
信号量通常用于保护容量有限的资源，例如数据库服务器。在资源大小固定的任何情况下，您应该使用有界信号量。在生成任何工作线程之前，您的主线程将初始化信号量：

maxconnections = 5
# ...
pool_sema = BoundedSemaphore(value=maxconnections)
一旦产生，工作线程在需要连接到服务器时调用信号量的获取和释放方法：

with pool_sema:
    conn = connectdb()
    try:
        # ... use connection ...
    finally:
        conn.close()
使用有界信号量可以减少导致信号量被释放的编程错误超过其获取的编程错误的可能性。
'''