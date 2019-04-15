#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 13:46
# 此类提供了一个简单的同步原语，供需要相互等待的固定数量的线程使用。
# 每个线程都试图通过调用wait()方法来传递屏障，并将阻塞直到所有线程都进行了调用。在这一点上，线程同时被释放。
# 对于相同数量的线程，屏障可以重复使用任意次数。
# 例如，这是一种同步客户端和服务器线程的简单方法：
'''
from threading import Barrier
b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()
    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()
    while True:
        connection = make_connection()
        process_client_connection(connection)
'''

"""
class threading.Barrier（派对，动作=无，超时=无）
为派对数量的线程创建一个屏障对象。提供的动作是一个可调用的，当它们被释放时由其中一个线程调用。 如果没有为方法指定none，则timeout是默认超时值wait()。

wait（超时=无）
通过障碍。当屏障的所有线程都调用此函数时，它们都会同时释放。如果提供了超时，则优先使用它来提供给类构造函数的任何超时。

返回值是0到party - 1 范围内的整数，每个线程都不同。这可以用来选择一个线程来做一些特殊的内务管理，例如：

i = barrier.wait()
if i == 0:
    # Only one thread needs to print this
    print("passed the barrier")
如果向构造函数提供了一个操作，则其中一个线程将在释放之前调用它。如果此调用引发错误，则屏障将进入损坏状态。

如果呼叫超时，屏障将进入断开状态。

BrokenBarrierError如果在线程等待时屏障被破坏或重置，则此方法可能引发异常。

reset（）
将屏障恢复为默认的空状态。等待它的任何线程都将收到BrokenBarrierError异常。

请注意，如果存在状态未知的其他线程，则使用此函数可能需要一些外部同步。如果障碍被打破，最好离开它并创建一个新障碍。

abort（）
将屏障置于破碎状态。这会导致任何活动或将来的调用wait()失败BrokenBarrierError。例如，如果其中一个需要中止，请使用此方法，以避免应用程序死锁。

可能最好简单地创建具有合理超时值的屏障， 以自动防止其中一个线程出错。

parties
通过障碍所需的线程数。

n_waiting
当前在屏障中等待的线程数。

broken
一个布尔值，True如果屏障处于断开状态。

异常threading.BrokenBarrierError
RuntimeError当Barrier对象被重置或损坏时，会引发 此异常（子类）。"""