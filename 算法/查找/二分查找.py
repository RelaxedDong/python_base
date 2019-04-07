# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/7 20:14

def BineraSearch(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1


if __name__ == '__main__':
    arr = [x for x in range(1000000)]
    n = 999999
    mid = BineraSearch(arr, n)
    print(mid)
