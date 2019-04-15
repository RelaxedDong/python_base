#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/9 14:03

# 1.1 现有字典 d={‘a’:24，‘g’:52，‘i’:12，‘k’:33}请按字典中的 value值进行排序？ (2018-3-30-lxy)
d = {'a':24,'g':52,'i':12,'k':33}
#方法一：
d = sorted(d.items(),key=lambda x:x[1])
# print(d)

#方法二：

# import operator
# c = sorted(d.items(),key = operator.itemgetter(1))
# print(c)


#方法三


#c = zip(d.values(),d.keys())
#c = sorted(c)
#print(c)

