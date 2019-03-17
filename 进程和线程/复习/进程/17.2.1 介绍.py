#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/17 21:21

from multiprocessing import Pool

# multiprocessing是一个使用类似于threading模块的API支持生成进程的包。
# 该multiprocessing软件包提供本地和远程并发，通过使用子进程而不是线程有效地支持 全局解释器锁。
# 因此，该multiprocessing模块允许程序员充分利用给定机器上的多个处理器。它可以在Unix和Windows上运行。
#
# 该multiprocessing模块还引入了threading模块中没有模拟的API 。
# 一个主要的例子是该 Pool对象提供了一种方便的方法，可以跨多个输入值并行化函数的执行，跨过程分配输入数据（数据并行）。
# 以下示例演示了在模块中定义此类函数的常见做法，以便子进程可以成功导入该模块。这个数据并行的基本例子使用Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))