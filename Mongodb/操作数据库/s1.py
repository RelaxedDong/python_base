#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 9:56
"""
1. 创建数据库
 use 数据库名 （数据库不存在 创建数据库）
注意：如果刚刚创建的数据库不在列表内，如果要显示它，我们需要向里面插入数据。

例如：
db.student.insert({name:"donghao",age:21,gender:1})
2.查看数据库
show dbs

3.查看当前使用数据库
    db
   db.getName()

4. 结构：
{
    "_id" : ObjectId("5cbfc370e8fd2b09d6fc4c2a"),
    "name" : "donghao",
    "age" : 21.0,
    "gender" : 1.0
}

5. 查看指令
help

6.删除数据库
前提：使用当前数据库
db.dropDatebase()

"""






















