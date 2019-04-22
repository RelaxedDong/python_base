#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 19:58

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


class NuWa(object):
    """创建女娲工厂类"""
    @staticmethod
    def create_person(name, gender):
        if gender == 'man':
            return Man(name, gender)
        else:
            return Woman(name, gender)

nuwa = NuWa()

#女娲开始造人了...
man = nuwa.create_person('superman', 'man')
woman = nuwa.create_person('superwoman','woman')


"""输出
superman
man
superwoman
woman
"""






















