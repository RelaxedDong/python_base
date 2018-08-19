from multiprocessing import Process
import time

num = 100

def fun():
    print('子进程开始')
    time.sleep(3)
    global num
    num += 1
    print(id(num))
    print('子进程结束')



if __name__ == '__main__':
    print('父进程开始')

    p = Process(target=fun)
    p.start()
    p.join()
    print(id(num))
    print(num)
    #子进程中修改全局变量修改没有影响
    #在创建子进程时多全局变量做了一个备份，属于不同的变量
    print('父进程结束')