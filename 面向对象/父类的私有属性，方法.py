#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 16:43

class Father(object):
    def __init__(self,name):
        self.name = name
        self.__money = 1000
    def __test(self):
        print('私有方法%s%d'%(self.name,self.__money))

    def test(self):
        self.__test()

class Children(Father):
    def __init__(self,name):
        super(Children, self).__init__(name)
c = Children('donghao')
# 子类对象可以调用父类共有方法，从而间接调用父类私有方法