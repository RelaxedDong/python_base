#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/9 14:13
"""
1.2 说一下字典和 json 的区别？(2018-3-30-lxy)

字典是一种数据结构，json 是一种数据的表现形式，字典的 key 值只要是能 hash 的就行，json 的
必须是字符串

"""
import json

d = {'name':'odngha','age':20}

# c = json.dumps(d) # dict to str
# print(c) # <class 'str'>
# print(type(c))

mystr = '{"school":"nyist","age":20}'

# myjson = json.loads(mystr) # str to dict
# print(myjson)
# print(type(myjson))


class Person():
    def __init__(self):
        self.name = 'donghao'
        self.age = 20
        self.school = 'nyist'


p = Person()
print(p.__dict__)
mydict = p.__dict__
c = json.dumps(mydict)
print(c)
print(type(c))

json.dump() #把dict文件转换成 json
json.dumps() #把dict转换成 json


json.loads() #把json转换成dict
json.load() #把json文件转换成dict