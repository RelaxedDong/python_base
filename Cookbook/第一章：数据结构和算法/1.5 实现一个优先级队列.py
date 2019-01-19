#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/19 17:00

import heapq

class Mydeque():
    def __init__(self):
        self._deque = []
        self._index = 0

    def push(self,item,property):
        # heapq.heappush(self.deque,(item,property))
        heapq.heappush(self._deque, (-property, self._index, item))
        self._index+=1

    def pop(self):
        return heapq.heappop(self._deque)

class Item():
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    deque = Mydeque()
    deque.push(Item('a'),1)
    deque.push(Item('c'),3)
    deque.push(Item('e'),5)
    deque.push(Item('b'),2)
    deque.push(Item('aaaaaaaaaa'),2)
    deque.push(Item('d'),4)
    print(deque.pop())
    print(deque.pop())
    print(deque.pop())
    print(deque.pop())
    print(deque.pop())
    print(deque.pop())
# 仔细观察可以发现，第一个 pop() 操作返回优先级最高的元素。
# 另外注意到如果两个有着相同优先级的元素（ foo 和 grok ），pop 操作按照它们被插入到队列的顺序返回的。
# 在上面代码中，队列包含了一个 (-priority, index, item) 的元组。 优先级为负数的目的是使得元素按照优先级从高到低排序。 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
#
# index 变量的作用是保证同等优先级元素的正确排序。 通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
# 而且， index 变量也在相同优先级元素比较的时候起到重要作用。

#
# 为了阐明这些，先假定 Item 实例是不支持排序的：
#
# >>> a = Item('foo')
# >>> b = Item('bar')
# >>> a < b
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unorderable types: Item() < Item()
# >>>
# 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。 但是如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错：
#
# >>> a = (1, Item('foo'))
# >>> b = (5, Item('bar'))
# >>> a < b
# True
# >>> c = (1, Item('grok'))
# >>> a < c
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unorderable types: Item() < Item()
# >>>
# 通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的避免上面的错误， 因为不可能有两个元素有相同的 index 值。Python 在做元组比较时候，如果前面的比较已经可以确定结果了， 后面的比较操作就不会发生了：
#
# >>> a = (1, 0, Item('foo'))
# >>> b = (5, 1, Item('bar'))
# >>> c = (1, 2, Item('grok'))
# >>> a < b
# True
# >>> a < c
# True
# >>>
