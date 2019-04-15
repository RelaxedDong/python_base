#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 13:44
'''
此类表示仅在经过一定时间后才应运行的操作 - 计时器。 Timer是一个子类，Thread 因此也可以作为创建自定义线程的示例。

通过调用start() 方法，计时器与线程一样启动。通过调用cancel()方法可以停止计时器（在其动作开始之前） 。计时器在执行其操作之前等待的时间间隔可能与用户指定的时间间隔不完全相同。

例如：

def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
class threading.Timer（interval，function，args = None，kwargs = None ）
创建一个定时器，在经过间隔秒后，将使用参数args和关键字参数kwargs运行函数。如果args是（默认值），则将使用空列表。如果kwargs是（默认值），那么将使用空的dict。NoneNone

在版本3.3中更改：从工厂功能更改为类。

cancel（）
停止计时器，取消执行计时器的操作。这仅在定时器仍处于等待阶段时才有效。
'''
from threading import Timer
def hello():
    print("hello, world")

t = Timer(5.0, hello)
t.start()
'''
class threading.Timer（interval，function，args = None，kwargs = None ）
创建一个定时器，在经过间隔秒后，将使用参数args和关键字参数kwargs运行函数。如果args是（默认值），则将使用空列表。如果kwargs是（默认值），那么将使用空的dict。NoneNone

在版本3.3中更改：从工厂功能更改为类。

cancel（）
停止计时器，取消执行计时器的操作。这仅在定时器仍处于等待阶段时才有效'''