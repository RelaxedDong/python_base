#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/19 14:16

class Person(object):
    def __init__(self,value):
        self.firstname = value

    # getter function
    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self,value):
        self._firstname = value+'123'
    @firstname.deleter
    def firstname(self):
        raise AttributeError("Can't delete attribute")
# class Person:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)
#
#     # Getter function
#     def get_first_name(self):
#         return self._first_name
#
#     # Setter function
#     def set_first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     # Deleter function (optional)
#     def del_first_name(self):
#         raise AttributeError("Can't delete attribute")
#
#     # Make a property from existing get/set methods
#     name = property(get_first_name, set_first_name, del_first_name)


class Child(Person):
    @property
    def firstname(self):
        print('child getting name')
        return super().firstname

    @firstname.setter
    def firstname(self,value):
        print('setting name')
        super(Child, Child).firstname.__set__(self,value)

    @firstname.deleter
    def firstname(self):
        print('delete name')
        super(Child, Child).firstname.__delete__(self)

# child = Child('guido')
# print(child.firstname)
# del child.firstname
# 如果你仅仅只想扩展property的某一个方法，那么可以像下面这样写：

class SubPerson(Person):
    @Person.firstname.getter
    def firstname(self):
        print('Getting name')
        return super().firstname
# 或者，你只想修改setter方法，就这么写：

class SubPerson(Person):
    @Person.firstname.setter
    def firstname(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).firstname.__set__(self, value)