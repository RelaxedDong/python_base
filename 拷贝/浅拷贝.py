#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/9 12:59

raw = [1,2,3,4,5,[6,7,8]]

# a = raw
# 复制，以前指向
# print(a)
# raw.append('haha')
# print(raw)
# print(a)

# raw[5].append('666')
# print(raw)
# print(a)

import copy
# 浅拷贝会创建新对象，其内容非原对象本身的引用，而是原对象内第一层对象的引用。

b = copy.copy(raw)
b = list(raw)

raw[5].append('666')

print('raw is ',raw)
print(b)

# print(raw[5][0] is b[5][0])
print(raw[1] is b[1])



"""
二、浅拷贝(shallow copy)
浅拷贝会创建新对象，其内容非原对象本身的引用，而是原对象内第一层对象的引用。
浅拷贝有三种形式:切片操作、工厂函数、copy 模块中的 copy 函数。
比如上述的列表 a；
切片操作：b = a[:] 或者 b = [x for x in a]；
工厂函数：b = list(a)；
copy 函数：b = copy.copy(a)；
浅拷贝产生的列表 b 不再是列表 a 了，使用 is 判断可以发现他们不是同一个对象，使用 id 查看，
他们也不指向同一片内存空间。但是当我们使用 id(x) for x in a 和 id(x) for x in b 来查看 a 和 b 中元
素的地址时，可以看到二者包含的元素的地址是相同的。
在这种情况下，列表 a 和 b 是不同的对象，修改列表 b 理论上不会影响到列表 a。
但是要注意的是，浅拷贝之所以称之为浅拷贝，是它仅仅只拷贝了一层，在列表 a 中有一个嵌套的
list，如果我们修改了它，情况就不一样了。
比如：a[3].append('java')。查看列表 b，会发现列表 b 也发生了变化，这是因为，我们修改了嵌
套的 list，修改外层元素，会修改它的引用，让它们指向别的位置，修改嵌套列表中的元素，列表的地
址并未发生变化，指向的都是用一个位置。
"""






