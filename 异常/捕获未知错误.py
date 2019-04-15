#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/13 14:21

# try:
#     num = int(input('input a number:'))
#     result = 8/num
# except ValueError:
#     print('输入错误')
# except Exception as result:
#     print('未知错误%s'%result)
#
#
# try:
#     '尝试执行的代码'
# except '错误类型1':
#     pass
#
# except '错误类型2':
#     pass
#
# else:
#     '没有异常，执行的代码'
#
# finally:
#     '无论是否有异常，都会执行'

try:
    a = 1/1
except ValueError:
    print('值错误')

except ZeroDivisionError:
    print('除数不能为0')
else:
    print('我执行了else')
finally:
    print('hahaha')