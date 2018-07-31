from collections import deque

que = deque([1,2,3,4,5,6,7])
# que.append('hello')
# print(que)
# print(type(que))
# print(que.pop())
# print(que.clear())


que.append('first')
que.append('second')
print(que)
que.popleft()
print(que)