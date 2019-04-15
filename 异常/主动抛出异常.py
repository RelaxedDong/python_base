#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/13 14:38

# 1.创建异常exception对象
# 2.使用raise关键字 抛出异常

def func():
    pass_word = input('请输入密码')
    if len(pass_word) > 8:
        return pass_word
    raise Exception('密码长度错误')

try:
    print(func())
except Exception as result:
    print(result)




