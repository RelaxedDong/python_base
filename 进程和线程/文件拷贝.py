#encoding:utf-8
import os
import time

def Copyfile(path,topath):
    pr = open(path,'rb')
    pw = open(topath,'wb')

    context = pr.read()
    pw.write(context)
    pr.close()
    pw.close()

from multiprocessing import Process,Pool
if __name__ == '__main__':
    path = r'E:\pycharm_pro\基础文件\tkinter'
    rofile = r'E:\pycharm_pro\基础文件\进程和线程\tofile'

    # start = time.time()
    # pathlist = os.listdir(path)
    # for file in pathlist:
    #     Copyfile(os.path.join(path,file),os.path.join(rofile,file))
    # end = time.time()
    # print('耗时：%0.002f'%(end-start))

    filelist = os.listdir(path)

    pp = Pool(4)
    start = time.time()
    for filename in filelist:
        pp.apply_async(func=Copyfile,args=(os.path.join(path,filename),os.path.join(rofile,filename)))

    pp.close()
    pp.join()
    end = time.time()
    print('耗时：%0.002f'%(end-start))





