#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 9:33
"""
String
Integer
Boolean
Double
Min/Max keys 将一个bson（二进制json)元素的最低值与最高值相对比
arrays
timestamp
Object 内嵌文档
Null
Symbol 符号
Date
Object ID
binary Date
Code 代码类型。用于在文档中存储javascript代码
Regualar expression 正则
"""


"""
启动服务
 mongod.exe --dbpath= your_db_path
"""


"""
Studio 3T 破解教程
1、创建文件studio3t.bat
@echo off
ECHO 重置Studio 3T的使用日期......
FOR /f "tokens=1,2,* " %%i IN ('reg query "HKEY_CURRENT_USER\Software\JavaSoft\Prefs\3t\mongochef\enterprise" ^| find /V "installation" ^| find /V "HKEY"') DO ECHO yes | reg add "HKEY_CURRENT_USER\Software\JavaSoft\Prefs\3t\mongochef\enterprise" /v %%i /t REG_SZ /d ""
ECHO 重置完成, 按任意键退出......
pause>nul
exit

2、将文件studio3t.bat文件移动到如下路径中

C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
3、双击运行
"""
