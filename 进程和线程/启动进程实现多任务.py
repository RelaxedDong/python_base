#encoding:utf-8
#multiprocessing跨平台版本的多进程模块，提供了一个process类代表一个进程对象

# os.getpid()获取当前进程号
from multiprocessing import Process
import os
import time



def run(*args):
    while 1:
        print(args,os.getpid(),os.getppid())
        time.sleep(1)


if __name__ == '__main__':
    print('主（父）进程启动！',os.getpid())

    #创建子进程
    #target说明进程执行的人物
    process = Process(target=run,args=('donghao is','djsafo',))
    process.start()

    while True:
        print('213')
        time.sleep(2)
