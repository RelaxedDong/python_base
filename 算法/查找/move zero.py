# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/7 20:42


def move(arr):
    # 方法1：

    # result = []
    # for x in arr:
    #     if x != 0:
    #         result.append(x)
    # for y in range(len(arr)-len(result)):
    #     result.append(0)
    # print(result)

    # 方法2：
    # for x in arr:
    #     print(x)
    #     if x == 0:
    #         arr.pop(arr.index(x))
    #         arr.append(x)
    # return arr

    # 第三种
    # index = 0
    # for x in arr:
    #     if x != 0:
    #         arr[index] = x
    #         index +=1
    # for y in range(index,len(arr)):
    #     arr[y] = 0

    # 第四种
    index = 0
    for x in range(0, len(arr)):
        if arr[x] != 0:
            arr[x], arr[index] = arr[index], arr[x]
            index += 1
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 40, 0, 23, 0, 123, 3, 0, 89, 23, 1, 0, 23, 4]
    move(arr)
