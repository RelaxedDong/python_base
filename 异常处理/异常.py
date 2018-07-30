#encoding:utf-8

# 需求：当程序遇到问题，不然程序结束，越过错误

'''
    try...except...else
'''
'''
try:
    语句t
except 错误代码:
except 错误码 as e:
except 错误码 as e:
except 错误码 as e:

else:
语句：
else可有可无


作用：用来检测try语句中的错误，excrpt捕获错误，进行处理
1.如果当try语句执行到错误，会匹配第一个错误码，如果没有
匹配上就执行对应语句
2.如果当try语句t 执行没有错误，没有匹配的异常，错误将会提交到上一层
的try语句，或者到程序的最上层
3.如果没有匹配到错误，那么将会执行else语句


'''
#
# try:
#     print(3/0)
# except BaseException as e:
#     print('baseerror')
# except NameError as e:
#     print('NameError')
# except ZeroDivisionError as e:
#     print('ZeroDivisionError')
# else:
#     print('没有错误')


#excrpt(ZeroDivisionError,NameError...)



# 跨越多层调用错误
def func1(num):
    print(num/0)

def func2(num):
    func1(num)

def main():
    func2(1)
try:
    main()
except:
    print('错误')


# try:
# except
# finally:
# 有没有错误，finally都会执行