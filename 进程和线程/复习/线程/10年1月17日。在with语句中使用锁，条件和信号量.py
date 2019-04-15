#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 13:49
'''
此模块提供的具有acquire()和 release()方法的所有对象都可以用作with 语句的上下文管理器。acquire()输入块时将调用该方法，并release()在退出块时调用该方法。因此，以下片段：

with some_lock:
    # do something...
相当于：

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
目前Lock，RLock，Condition， Semaphore，和BoundedSemaphore对象可以用作 with声明上下文管理。
'''