#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 20:20

"""对于复杂的问题，工厂方法模式会实现很多工厂类，不利于代码维护"""

class Person(object):
    def __init__(self,name):
        self.name = name

class Woman(Person):
    def __init__(self,name,gender):
        super(Woman, self).__init__(name)
        self.gender = gender

class Man(Person):
    def __init__(self,name,gender):
        super(Man, self).__init__(name)
        self.gender = gender

class Factory_gender(object):
    """女娲造人"""
    def create_man(self, name):
        return Man(name, "man")

    def create_woman(self, name):
        return Woman(name, 'woman')

class Factory_butian(object):
    """女娲补天"""
    pass

class NuWa(object):
    """创建女娲工厂类"""
    @staticmethod
    def create_person(product_type):
        if product_type == "造人":
            return Factory_gender()
        elif product_type == "补天":
            return Factory_butian()
        #...other factory

nuwa = NuWa()
genderfactory = nuwa.create_person('造人')

man = genderfactory.create_man('superman')
woman = genderfactory.create_woman('superwoman')

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