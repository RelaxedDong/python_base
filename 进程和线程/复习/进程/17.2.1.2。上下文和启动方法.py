#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/17 21:28
# 根据平台，multiprocessing支持三种启动流程的方法。这些启动方法是
#
# 卵
# 父进程启动一个新的python解释器进程。子进程只会继承运行进程对象run()方法所需的那些资源。特别是，不会继承父进程中不必要的文件描述符和句柄。与使用fork或forkserver相比，使用此方法启动进程相当慢。
#
# 可在Unix和Windows上使用。Windows上的默认设置。
#
# 叉子
# 父进程用于os.fork()分叉Python解释器。子进程在开始时实际上与父进程相同。父进程的所有资源都由子进程继承。请注意，安全分叉多线程进程存在问题。
#
# 仅适用于Unix。Unix上的默认值。
#
# forkserver
# 当程序启动并选择forkserver start方法时，将启动服务器进程。从那时起，每当需要一个新进程时，父进程就会连接到服务器并请求它分叉一个新进程。fork服务器进程是单线程的，因此它可以安全使用os.fork()。没有不必要的资源被继承。
#
# 可在Unix平台上使用，支持通过Unix管道传递文件描述符

# 要选择启动方法，请使用主模块set_start_method()的子句中的。例如：if __name__ == '__main__'


# import multiprocessing as mp
#
# def f(q,name):
#     q.put(name)
#
# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     p = mp.Process(target=f,args=(q,1,))
#     p.start()
#     print(q.get())
#     p.join()

# set_start_method() 不应该在程序中多次使用


# 或者，您可以使用get_context()获取上下文对象。
# 上下文对象与多处理模块具有相同的API，并允许在同一程序中使用多个启动方法。



import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo,args=(q,))
    p.start()
    print(q.get())
    p.join()

# 请注意，与一个上下文相关的对象可能与不同上下文的进程不兼容。特别是，使用fork上下文创建的锁不能传递给使用spawn或forkserver start方法启动的进程 。
#
# 想要使用特定启动方法get_context()的库可能应该用来避免干扰库用户的选择。


