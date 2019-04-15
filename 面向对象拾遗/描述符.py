class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        # print(obj)  # <__main__.Myclass object at 0x027A3390>
        # print(objtype) # <class '__main__.Myclass'>
        # print('我描述了')
        print( 'Retrieving', self.name)

        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class Myclass(object):
    x = RevealAccess(10,'var "x"')
    y = 5

m = Myclass()
print(m.x)
m.x = '123'
print(m.x)

# __getattribute__是实例对象查找属性或方法的入口。
# 实例对象访问属性或方法时都需要调用到__getattribute__，之后才会根据一定的规则在各个__dict__中查找相应的属性值或方法对象，
# 若没有找到则会调用__getattr__（后面会介绍到）。__getattribute__是Python中的一个内置方法
# ，关于其底层实现可以查看相关官方文档，后面将要介绍的属性访问规则就是依赖于__getattribute__的。