#encoding:utf-8


from multiprocessing import Queue,Process
import time,os

def write(q):
    print('子进程%s启动'%os.getpid())
    for str in ['A','B','C','D']:
        q.put(str)
        time.sleep(2)
    print('写子进程结束')

def read(q):
    print('子进程%s启动'%os.getpid())
    while True:
        s = q.get()
        print(s)
    print('读子进程结束')



if __name__ == '__main__':
    print('父进程启动')
    q = Queue()
    fw = Process(target=write,args=(q,))
    fr = Process(target=read,args=(q,))
    fw.start()
    fr.start()
    fw.join()
    fr.terminate()
    print('父进程结束')

