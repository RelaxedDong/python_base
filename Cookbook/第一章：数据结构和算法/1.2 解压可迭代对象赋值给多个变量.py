#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/19 15:38
# 问题
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
# 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

# 解决方案
# Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：

# def drop_first_last(grades):
    # first, *middle, last = grades
    # return math.avg(middle)
#
# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
#
# name,email,*phone = record
# print(phone)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

# for tag, *args in records:
#     print(tag,(args))
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
# record = ('ACME', 50, 123.45, (12, 18, 2012))
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012,['abc','hhh','bbb']))
name, *_, (*_, [*_,b]) = record

print(name,b)
items = [1, 10, 7, 4, 5, 9]
def sum(items):
     head, *tail = items
     return head + sum(tail) if tail else head
print(sum(items))