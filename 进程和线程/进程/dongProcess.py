from multiprocessing import Process
import os,time

class myProcess(Process):
    def __init__(self,name):
        super(myProcess, self).__init__()
        self.name = name

    def run(self):
        print('子进程%s启动'%(self.name),os.getpid())
        time.sleep(2)
        print('子进程结束')