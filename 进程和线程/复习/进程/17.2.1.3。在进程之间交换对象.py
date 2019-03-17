#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/17 21:45
# multiprocessing 支持进程之间的两种通信通道：

# 队列
# 这个Queue班级是近乎克隆的queue.Queue。例如：
from multiprocessing import Process, Queue,Pipe
import multiprocessing
"""

def f(q):
    print(multiprocessing.current_process())
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    print(multiprocessing.current_process())
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
"""


# 队列是线程和进程安全的


# 管道
# 该Pipe()函数返回一个由管道连接的连接对象，默认情况下为双工（双向）。例如：

def f(conn):
    conn.send([42,None,'hello'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe() #两个连接对象Pipe()表示管道的两端
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('parent send')
    p.join()
# 两个进程（或线程）同时尝试读取或写入管道的同一端，则管道中的数据可能会损坏
# 当然，同时使用管道的不同端的进程不存在损坏的风险




