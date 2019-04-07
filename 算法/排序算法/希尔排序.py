# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/14 14:14

def shellSort(arr):
    length = len(arr)
    gap = length // 2  # 初始步长
    while gap >= 1:
        for x in range(gap, length):  # 每一列进行插入排序 , 从gap 到 n-1
            i = x
            while (i - gap) >= 0:
                if arr[i] < arr[i - gap]:
                    arr[i], arr[i - gap] = arr[i - gap], arr[i]  # 值交换
                    i -= gap
                else:
                    break
        gap //= 2  # 更改步长
    print(arr)


import time, random

if __name__ == '__main__':
    mylist = [random.randint(1, 12345) for x in range(1, 123456)]
    start = time.time()
    shellSort(mylist)
    end = time.time()
    print(start - end)
    print('耗时：%0.002f' % (end - start))

# 随机万级数据，耗时 2 S
