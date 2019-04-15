#encoding:utf-8


# 1.  print(int('1010',base=2))


#2.偏函数（参数上自己定义）
# def fun2(str,base=2):
#     return int(str,base)
# print(fun2('1010'))


#3.把一个参数固定，行成新的函数
from functools import partial

# fun3 = functools.partial(int,base=2)
# print(fun3('1010'))


# def add2(a,b):
#     print(a)
#     print(b)
#     return a+b
# fun4 = functools.partial(add2,23)
#
# print(fun4(3))


func5 = partial(max,5)
print(type(func5))
print(func5(1,3,2,24,56,123))
