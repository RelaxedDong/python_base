#encoding:utf-8

class Father(object):
    def __init__(self,money):
        self.money = money

    def func(self):
        print('func1')


class Mother(object):
    def __init__(self, facevalue):
        self.facevalue = facevalue

    def func(self):
        print('func2')

class Child(Father,Mother):
    def __init__(self,money,facevalue):
        super(Father, self).__init__()

c = Child(1000,'goodlooking')

print(c.__dict__)