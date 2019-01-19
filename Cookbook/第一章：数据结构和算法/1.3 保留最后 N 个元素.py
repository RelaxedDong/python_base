#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/19 16:20

# 问题
# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
#
# 解决方案
# 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的最后N行：

from collections import deque

def search(lines,keyword,long=5):
    pre_lines = deque(maxlen=long)
    for line in lines:
        if keyword in line:
            yield line,pre_lines
        pre_lines.append(line)

from io import TextIOWrapper
if __name__ == '__main__':
    # with open('somefile.txt',encoding='utf-8') as f:
    #     for line ,pre_lines in search(f,'python',5):
    #         print(line)
    #         for pre in pre_lines:
    #             print(pre)
    #         print('*'*40)


# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉
    a = deque(maxlen=3)
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)
    a.append(4)
    print(a)
    a.pop()
    print(a)
    a.append('123')
    print(a)
