#encoding:utf-8
import os
#获取操作系统类型  nt->windows
print(os.name)

#打印操作系统详细信息，windows不支持
# print(os.uname())


#获取操作系统所有环境变量
# print(os.environ)
#获取指定环境变量
# print(os.environ.get('APPDATA'))


#获取当前目录  ./a/
# print(os.curdir)

#获取当前工作目录
# print(os.getcwd())

#列表形式返回 所有文件
# print(os.listdir(os.path.dirname(__file__)))


#创建一个目录
# os.mkdir('os创建的目录')

#删除目录
# os.rmdir('os创建的目录')

#获取文件属性
# print(os.stat('os模块.py'))

#重命名
# os.rename('old','new')

#删除普通文件
# os.remove('path')

#运行shell命令
# os.system('notepad')
#记事本
# os.system("write")
#关闭
# os.system('taskkill /f /im no notpad++.exe')
#画图
# os.system('mspaint')
#设置
# os.system('msconfig')
#设置关机
# os.system("shutdown -s -t 500")
#取消关机
# os.system("shutdown -a")


#--------------------------
#查看当前绝对路径
# print(os.path.abspath('.'))

#拼接路径
# p1 = 'e:\pycharm_pro\基础文件\os模块'
# p2 = 'test\\a\\b\\c'
# print(os.path.join(p1,p2))


#拆分路径
# print(os.path.split(r'e:\pycharm_pro\基础文件\os模块\test\a\b\c'))

#获取扩展名
# print(os.path.splitext(r'e:\pycharm_pro\基础文件\os模块\test\a\b\c'))


#判断是否是目录
# print(os.path.isdir(os.path.curdir))
# print(os.path.isdir(os.getcwd()))

#判断文件存在
# print(os.getcwd())
# print(os.path.isfile(os.path.join(os.getcwd(),'os模块.py')))

#判断目录是否存在
# print(os.path.exists())

#获取文件大小(字节)
# print(os.path.getsize(os.path.join(os.getcwd(),'os模块.py')))

#文件的目录
# print(os.path.dirname(os.getcwd()))
# print(os.path.basename(os.getcwd()))