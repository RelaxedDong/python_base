#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 17:19


# 多态：$$$$$$$$$$$$$$$$$$$$$$$不同的子类对象调用父类方法，产生不同的执行效果
# 多态可以增加代码的灵活度
# 以继承和充血父类的方法为前提
# /是调用的方法技巧，不会影响到类的内部设计

        
class Animal(object):
    def __init__(self,name):
        self.name = name

class Person(Animal):
    def __init__(self,name):
        super(Person, self).__init__(name)
    def game_with_dog(self,dog):
        dog.game()
        
class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
    
    def game(self):
        print('小狗玩耍')
        
class XiaoTianQuan(Dog):
    def __init__(self,name):
        super(XiaoTianQuan, self).__init__(name)
    
    def game(self):
        super(XiaoTianQuan, self).game()
        print('神犬上天啦！')
    
    
super_dog = XiaoTianQuan('哮天犬')

me = Person('董浩')
me.game_with_dog(super_dog)
        
        