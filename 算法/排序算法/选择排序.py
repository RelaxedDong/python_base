# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/4 13:58

def main(arr):
    for x in range(len(arr) - 1):
        minflag = x
        for j in range(x + 1, len(arr)):
            if arr[j] < arr[minflag]:
                minflag = j
        arr[x], arr[minflag] = arr[minflag], arr[x]

    print(arr)


# 其时间复杂度为 O(N^2)
if __name__ == '__main__':
    arr = [6, 4, 8, 9, 2, 1, 10, 7]
    main(arr)
