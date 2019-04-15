#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 16:19

class Animal(object):
    def eat(self):
        print('吃')
    def sleep(self):
        print('睡')

class Dog(Animal):
    def brak(self):
        print('咬')

class SuperDog(Dog):
    def fly(self):
        print('fly')
    def sleep(self):
        print('我睡会儿')
        super(SuperDog, self).sleep()
        #python2.x
        # Animal.sleep(self)

        #如果使用子类调用方法，会出现递归调用
        

xiaotianqian = SuperDog()
xiaotianqian.sleep()

