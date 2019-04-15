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
        print("calling __delattr__")
        super(Dog, self).__delattr__(name)

dog = Dog(2)
# 给dog.age赋值，会调用__setattr__方法
print('dog.age:',dog.age)
# 先调用dog.fly时会返回False，这时因为Dog类属性中有fly属性；
# 之后再给dog.fly赋值，触发__setattr__方法。
print ('dog.fly:',dog.fly)
dog.fly = True
# 再次查看dog.fly的值以及dog和Dog的__dict__;
# 可以看出对dog对象进行赋值，会在dog对象的__dict__中添加了一条对象属性；
# 然而，Dog类属性没有发生变化
# 注意：dog对象和Dog类中都有fly属性，访问时会选择哪个呢？
print ('dog.fly:',dog.fly)
print ('dog.__dict__:',dog.__dict__)
print ('Dog.__dict__:',Dog.__dict__)

del dog.fly
# 再次查看dog对象的__dict__，发现和fly属性相关的信息被删除
print (dog.__dict__)

