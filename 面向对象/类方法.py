#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 18:04
#
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#
#
#     @classmethod
#     def play(cls):
#         print(cls)
#         print('waner')
#
#
#
#
# p = Person('nnn')
# Person.play()
# # :<class '__main__.Person'>
# p.play()
#类名.调用类方法，调用方法时，不需要传递 cls参数

class Tool(object):
    count = 0
    @classmethod
    def show_tool_count(cls):
        print('show_tool_count工具对象的数量%s'%cls.count)
        cls.show_count(cls)
    def __init__(self,name):
        self.name = name
        Tool.count += 1
    def show_count(self):
        print('show_count工具对象的数量%s' % self.count)

tool1 = Tool('斧头')
tool2= Tool('盆子')
tool3 = Tool('刀')
tool1.show_count()
Tool.show_tool_count()









