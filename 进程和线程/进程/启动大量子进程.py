#encoding:utf-8

from multiprocessing import Process,Pool
import time,random,os
def run(name):
    print('子进程启动%s,--pid%s'%(name,os.getpid()))
    stat = time.time()
    time.sleep(1)
    end = time.time()
    print('子进程%s结束'%name,'耗时%0.2f'%(end-stat))


if __name__ == '__main__':
    print('父进程开始')

    #创建多个进程
    #进程池
    pp = Pool(4)
    for i in range(10):
        #创建进程，放入进程池
        pp.apply_async(func=run,args=(i,))

        #在调用join前，必须先调用close，调用close之后不能添加新的进程
    pp.close()
    pp.join()


    print('父进程结束')