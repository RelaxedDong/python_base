#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 17:47

class Tool(object):
    # 类属性用来记录这个类相关的特性
    #类属型不用于记录对象的特征
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count+=1

t = Tool('钳子')
print(t.count)
#1.首先在对象内部查找
# 2.向上查找，在类中查找
# 3.没找到，报错
t1 = Tool('钳子1')
print(t1.count)

t2 = Tool('钳子2')
print(t2.count)

#对象.类属性  （不推荐）

t2.count = 100
# 对象.类属性 = 值，会给对象添加一个属性，不会影响到类属性
print(t2.count)

print(Tool.count)
print(t1.count)
