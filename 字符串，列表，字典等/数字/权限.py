#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/18 11:12

class Permission(object):
    # 全部权限
    ALL_PERMISSION = 0b11111111
    #访问者权限
    VISOTOR =        0b00000001
    # 管理帖子权限
    POSTER =         0b00000010
    #管理评论权限
    COMMENTER =      0b00000100
    #管理板块
    BOARDER =        0b00001000
    #管理前台用户
    FRONT =          0b00010000
    #CMS
    ADMIN =          0b00100000

class Person(object):
    def __init__(self,name,permission):
        self.name = name
        self.permission = permission

    def has_permission(self,permission):
        return self.permission & permission == permission


visitor = Person(name='访问者',permission=Permission.VISOTOR)

operator = Person(name='运营',permission=Permission.VISOTOR|Permission.POSTER|Permission.COMMENTER|
                  Permission.BOARDER)
developer = Person(name='开发者',permission=Permission.ALL_PERMISSION)

admin = Person('管理员',permission=Permission.VISOTOR|Permission.BOARDER|Permission.COMMENTER|
               Permission.POSTER|Permission.FRONT|Permission.ADMIN)

"""
print(visitor.permission)
print(operator.permission)
print(developer.permission)
print(admin.permission)
"""

result = operator.has_permission(Permission.ADMIN)
print(result)
