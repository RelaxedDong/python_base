class Animal(object):
    run = True
class Dog(Animal):
    fly = False
    def __init__(self, age):
        self.age = age
    def __getattr__(self, name):
        print ("calling __getattr__")
        if name == 'adult':
            return True if self.age >= 2 else False
        else:
            print('我不是adult')
    def __setattr__(self, name, value):
        print ("calling __setattr__")
        super(Dog, self).__setattr__(name, value)
    def __delattr__(self, name):
        print ("calling __delattr__")
        super(Dog, self).__delattr__(name)

# 创建实例对象dog
dog = Dog(1)
# 检查一下dog和Dog的__dict__
print ('dog.__dict__:',dog.__dict__)
print ('Dog.__dict__:',Dog.__dict__)
# 获取dog的age属性
print('dog.age:',dog.age)
# 获取dog的adult属性。
# 由于__getattribute__没有找到相应的属性，所以调用__getattr__。
print ('dog.adult:',dog.adult)
# 调用一个不存在的属性name，__getattr__捕获AttributeError错误
print('dog.name:',dog.name)

# 可以看到，属性访问时，当访问一个不存在的属性时触发__getattr__，它会对访问行为进行控制。
