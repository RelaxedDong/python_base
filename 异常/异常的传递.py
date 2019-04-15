#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/13 14:35

#利用异常的传递性

def model1():
    return int(input('输入一个整数'))

def demo2():
    return model1()

try:
    demo2()
except Exception as result:
    print(result)

# 在主程序中，在主函数中 添加异常捕获