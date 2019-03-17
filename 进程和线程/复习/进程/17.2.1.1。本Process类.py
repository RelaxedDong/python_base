#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/17 21:22

# 在multiprocessing，通过创建Process 对象然后调用其start()方法来生成进程。
# Process 遵循API的threading.Thread。多进程程序的一个简单例子是
# from multiprocessing import Process
#
# def f(name):
#     print('hello',name)
#
# if __name__ == '__main__':
#    p =  Process(target=f,args=('donghao',))
#    p.start()
#    p.join()


# 要显示所涉及的各个进程ID，以下是一个扩展示例：

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name',__name__)
    print('parent process',os.getppid())
    print('process id',os.getpid())
    print('*'*30)


def f(name):
    info('function f')
    print('hello',name)

if __name__ == '__main__':
   info('main line')
   p =  Process(target=f,args=('donghao',))
   p.start()
   p.join()