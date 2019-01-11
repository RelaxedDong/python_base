#encoidng:utf-8
from werkzeug.security import check_password_hash,generate_password_hash
# class Person(object):
#     name = ''
#     age = ''
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print(self.name+'eat')
#
# p = Person('donghao')
# p1 = Person('donghao')
#
# p.weight = 20
# print(p.weight)
#
class User(object):
    __password = ''
    id = ''
    username = ''
    def __init__(self,*args,**kwargs):
        print(type(self))
        if 'password' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(User, self).__init__(*args,**kwargs)


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,inputpwd):
        self.__password = generate_password_hash(inputpwd)

    def checkpwd(self,raw_password):
        if(check_password_hash(self.__password,raw_password)==True):
            print('密码正确')
        else:
            print('密码错误')

p = User()
p.username = 'dongha'
p.password = '123'
p.id = '1'
print(p.__dict__)



# password = generate_password_hash('123456')
# inputpassword = input('请输入密码：')
# if check_password_hash(password,inputpassword):
#     print('密码正确')
#     print(check_password_hash(password,inputpassword))
# else:
#     print('密码错误')