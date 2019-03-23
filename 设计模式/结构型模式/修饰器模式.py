# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/23 18:52


# 该模式虽名为修饰器，但这并不意味着它应该只用于让产品看起来更漂亮。修饰器模式通常用于扩展一个对象的功能。
# 这类扩展的实际例子有，给枪加一个消音器、使用不同的照相机镜头

def before(func):  # 定义修饰器
    def wrapper(*args, **kwargs):  # 新函数
        print('Before function called.')  # 新增的语句
        return func(*args, **kwargs)  # 返回旧函数

    return wrapper  # 返回新函数


def after(func):  # 定义修饰器
    def wrapper(*args, **kwargs):  # 新函数
        result = func(*args, **kwargs)  # 调用旧函数
        print('After function called.')  # 增加新语句
        return result  # 返回旧函数

    return wrapper  # 返回新函数


@before  # 外层的修饰
@after  # 内层的修饰
def test():  # 可以理解为print(3)先增加了after修饰的语句后的新函数
    print(3)  # 又增加了before修饰的语句


test()
