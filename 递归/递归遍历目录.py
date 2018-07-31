#encoding:utf-8

import os

path = r'D:\my_project'

def GetPath(path,sp = ""):
    filelist = os.listdir(path)
    sp += "  "
    for file in filelist:
        # if(os.path.isdir(os.path.join(path,file))):
        #     print(path+file+'是一个文件')
        # else:
        #     print(path + file + '不是一个文件')
        if(os.path.isdir(os.path.join(path,file))):
            print(sp,'目录文件',os.path.join(path,file))
            GetPath(os.path.join(path,file),sp)
        else:
            print(sp,'普通文件',os.path.join(path,file))



GetPath(path,sp="")