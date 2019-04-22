#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 20:11


class Person(object):
    def __init__(self,name):
        self.name = name

class Woman(Person):
    def __init__(self,name,gender):
        super(Woman, self).__init__(name)
        self.gender = gender

class Man(Person):
    def __init__(self, name, gender):
        super(Man, self).__init__(name)
        self.gender = gender


class Factory_man(object):
    def create_person(self, name):
        return Man(name, "man")

class Factory_woman(object):
    def create_person(self, name):
        return Woman(name, 'woman')


class NuWa(object):
    """创建女娲工厂类"""
    @staticmethod
    def gender_type(gender):
        if gender == 'man':
            return Factory_man()
        else:
            return Factory_woman()

nuwa = NuWa()

#女娲开始造人了...
factory_man = nuwa.gender_type('man')
factory_woman = nuwa.gender_type('woman')

man = factory_man.create_person('superman')
woman = factory_woman.create_person('superwoman')

print(man.name)
print(man.gender)

print(woman.name)
print(woman.gender)

"""输出
superman
man
superwoman
woman
"""

"""
简单工厂模式存在一个问题，当要增加产品时，需要修改工厂类或者工厂方法，
这违背了扩展开放，修改封闭的原则，因此是不可取的。
工厂方法模式能够实现最小化地修改工厂类或工厂函数
"""

