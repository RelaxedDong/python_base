#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 15:59

class Woman(object):
    def __init__(self,name):
        self.name = name
        self.__age = 18
    def secret(self):
        print('%s的年龄是%s'%(self.name,self.__age))
        self.__ask_age()

    def __ask_age(self):
        print('私有，不告诉你')

    # def __setattr__(self, key, value):
    #     self.
tanyajuan = Woman(name='谭雅娟')
tanyajuan.secret()
tanyajuan._Woman__ask_age()
tanyajuan._Woman__age = 100
print(tanyajuan._Woman__age)
#python中，并没有真正意义的私有

# python正对私有属性处理方式，在私有属性，私有方法改为 __类名,=>_类名__(属性，方法名)
