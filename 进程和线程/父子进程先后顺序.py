from multiprocessing import Process
import time
def run1(*args):
    print('子进程1启动！')
    time.sleep(1)
    print('子进程1结束！')
def run2(*args):
    print('子进程2启动！')
    time.sleep(3)
    print('子进程2结束！')



if __name__ == '__main__':
    print('父进程启动！')
    p1 = Process(target=run1,args=('donghao'))
    p = Process(target=run2,args=('donghao'))
    p1.start()
    p.start()
    p.join()
    p1.join()
    print('父进程结束！')



