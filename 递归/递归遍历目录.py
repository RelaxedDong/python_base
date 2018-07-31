#encoding:utf-8

import os

path = os.path.split(os.path.abspath('.'))[0]

def GetPath(path):
    filelist = os.listdir(path)
    for file in filelist:
        # if(os.path.isdir(os.path.join(path,file))):
        #     print(path+file+'是一个文件')
        # else:
        #     print(path + file + '不是一个文件')
        if(os.path.isdir(os.path.join(path,file))):
            print(os.path.join(path,file)+'是一个文件')
            return GetPath(os.path.join(path,file))
        else:
            print(os.path.join(path,file)+'不是一个文件')



GetPath(path)