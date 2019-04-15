#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 21:18

class Dog(object):
    #既不需要访问实例属性
    # 也不需要访问类属性
    @staticmethod
    def run():
        print('123')

#通过类名，调用静态方法，不需要创建对象
Dog.run()