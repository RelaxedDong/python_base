#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/9 15:31

"""
1. 引用计数:

引用计数也是一种垃圾收集机制，而且也是一种最直观，最简单的垃圾收集技术。
当 Python 的某个对象的引用计数降为 0 时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。
比如某个新建对象，它被分配给某个引用，对象的引用计数变为 1。
如果引用被删除，对象的引用计数为 0，那么该对象就可以被垃圾回收。不过如果出现循环引用的话，引用计数机制就不再起有效的作用了
"""

mystr = 'scasubstrxrhaha'
mydict = {}
for index,x in enumerate(mystr):
    str = x
    for y in range(index+1,len(mystr)):
        str = str + mystr[y]
        mydict[str] = index
print(mydict)
print(mydict.get('rhaha',-1))


