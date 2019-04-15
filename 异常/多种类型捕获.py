#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/13 14:18

try:
    num = int(input('input a number:'))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输入一个整数')

print('----'*28)