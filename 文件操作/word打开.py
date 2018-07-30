#coding=utf-8
path = "c:\\Users\\Administrator\\Desktop\\mytest.wps"

with open(path,'rb') as f:
    data = f.read()
    print(type(data))
