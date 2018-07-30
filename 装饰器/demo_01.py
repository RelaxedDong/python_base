#encoding:utf-8




# def outer(func):
#     def inner(age):
#         if age<0:
#             age = 0
#         func(age)
#     return inner
#
#
#
# def say(age):
#     print('donghao is %d years old'%(age))
#
#
# myage = int(input('请输入年龄：'))
# f = outer(say)
# f(myage)



# def outer(func):
#     def inner(age, name1):
#         if age < 0:
#             age = 0
#         func(age, 'donghao')
#
#     return inner
#
#
# @outer
# def say(age, name):
#     print(name)
#     print('donghao is %d years old' % (age))
#
#
# say(-10, 'donghao1')





def outer(func):
    def inner(*args, **kwargs):
        print(*args)
        print(kwargs)
        args = (-20,'tanyajuan')
        kwargs = {'gender':'男'}
        func(*args, **kwargs)
    return inner


@outer
def say(age, name,**kwargs):
    print(kwargs)
    print('%s is %d years old' % (name,age))


say(-10, 'donghao1')






