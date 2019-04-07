# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/4 13:48


def main(arr):
    for x in range(len(arr)):
        flag = False
        for y in range(len(arr) - 1 - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                flag = True
        if not flag:
            break
    print(arr)


"""

冒泡排序总的平均时间复杂度为  O(n²)

"""

if __name__ == '__main__':
    arr = [6, 4, 8, 9, 2, 1, 10, 7]
    main(arr)
