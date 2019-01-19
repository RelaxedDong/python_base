#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/19 21:57
# 问题
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
#
# 解决方案
# 考虑下面的股票名和价格映射字典：

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

from heapq import nsmallest,nlargest

#1. 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。 比如，下面是查找最小和最大股票价格和股票值的代码：
a = zip(prices.values(),prices.keys())
# small = min(a)
# print(small)
# large = max(a)
# print(large)

# 2.small = nsmallest(1,prices.items(),lambda x:x[1])
#     large = nlargest(len(prices),prices.items(),lambda x:x[1])

# 排序字典:
# 1.small = nsmallest(1,prices.items(),lambda x:x[1])
#     large = nlargest(len(prices),prices.items(),lambda x:x[1])
#2.
# price_sorted = sorted(zip(prices.values(),prices.keys()))
# print(price_sorted)
# 反序
# price_sorted = sorted(zip(prices.values(),prices.keys()),reverse=True)
# print(price_sorted)
#
# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：
#
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

# 最大值，最小值
# b = min(prices, key=lambda k: prices[k]) # Returns 'FB'
# c = max(prices, key=lambda k: prices[k]) # Returns 'AAPL'
# print(b)
# print(c)
# min_value = prices[min(prices, key=lambda k: prices[k])]
# print(min_value)


# 需要注意的是在计算操作中使用到了 (值，键) 对。当多个实体拥有相同的值的时候，键会决定返回结果。 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：
#
# >>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
# >>> min(zip(prices.values(), prices.keys()))
# (45.23, 'AAA')
# >>> max(zip(prices.values(), prices.keys()))
# (45.23, 'ZZZ')
# >>>
