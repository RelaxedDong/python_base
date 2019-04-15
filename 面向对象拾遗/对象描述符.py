#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/19 19:11

"""
class Animal(object):
    def __set__(self, instance, value):
        print('*'*30)
        print(instance,value)
        print('__set__......')

    def __get__(self, instance, owner):
        print('__get__.......')
        print('self is ',self)
        print('instance is ',instance) #一个实例
        print('owner is ',owner)

    def __delete__(self, instance):
        print('delete')
class Dog(object):
    x = Animal()
    def __init__(self,x):
        self.x = x
# Dog.x #instance is  None
Dog.x = 'egon'  #没有执行__set__
del Dog.x
"""
# 类属性优先级大于数据描述符


# 数据描述符优先级大于实例属性
"""
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

class People:
    name=Str()
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=People('egon',18)
p1.name
print(p1.__dict__)
del p1.name"""

# 实例属性优先级大于非数据描述符
# 数据描述符：至少实现了 __get__()和__set__()
# 非数据描述符:没有实现 __set__()

# class Foo:
#     def func(self):
#         print('我胡汉三又回来了')
# f1=Foo()
# f1.func() #调用类的方法,也可以说是调用非数据描述符
# #函数是一个非数据描述符对象(一切皆对象么)
# print(dir(Foo.func))
# print(hasattr(Foo.func,'__set__'))
# print(hasattr(Foo.func,'__get__'))
# print(hasattr(Foo.func,'__delete__'))

class Foo:
    def __get__(self, instance, owner):
        print('get')
class Room:
    name=Foo()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

#name是一个非数据描述符,因为name=Foo()而Foo没有实现set方法,因而比实例属性有更低的优先级
#对实例的属性操作,触发的都是实例自己的
r1=Room('厕所',1,1)
r1.name
r1.name='厨房'


def has_descriptor_attrs(obj):
    return set(['__get__', '__set__', '__delete__']).intersection(dir(obj))

def is_descriptor(obj):
    """obj can be instance of descriptor or the descriptor class"""
    return bool(has_descriptor_attrs(obj))

def has_data_descriptor_attrs(obj):
    return set(['__set__', '__delete__']) & set(dir(obj))

def is_data_descriptor(obj):
    return bool(has_data_descriptor_attrs(obj))

print(is_descriptor(classmethod), is_data_descriptor(classmethod))
print(is_descriptor(staticmethod), is_data_descriptor(staticmethod))
print(is_data_descriptor(property))
