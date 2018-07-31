# 1.栈(stacks)是一种只能通过访问其一端来实现数据存储与检索的线性数据结构，
# 具有后进先出(last in first out，LIFO)的特征


# 2.队列(queue)是一种具有先进先出特征的线性数据结构，
# 元素的增加只能在一端进行，元素的删除只能在另一端进行。能够增加元素的队列一端称为队尾，
# 可以删除元素的队列一端则称为队首。

stack = [1,2,3,4,5,6,6]
# 去重：
stack = list(set(stack))
stack.append('a')
# 出栈
# list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
stack.pop()

print(stack)