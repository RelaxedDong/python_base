# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/4 14:06


def main(arr):
    for x in range(1, len(arr)):
        index = x - 1
        current = arr[x]
        while index >= 0 and arr[index] > current:
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = current

    print(arr)


if __name__ == '__main__':
    arr = [6, 4, 8, 9, 2, 1, 10, 7]
    main(arr)
