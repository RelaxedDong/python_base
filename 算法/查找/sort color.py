# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/8 10:25

def sortColors(arr):
    # mydict = {}
    # for x in arr:
    #     if x in mydict:
    #         mydict[x] += 1
    #     else:
    #         mydict[x] = 1
    # index = 0
    # for x in range(mydict[0]):
    #     arr[index] = 0
    #     index+=1
    #
    # for x in range(mydict[1]):
    #     arr[index] = 1
    #     index+=1
    #
    # for x in range(mydict[2]):
    #     arr[index] =2
    #     index+=1
    #
    # print(arr)

    zero = -1
    two = len(arr)
    i = 0
    while i < two:
        if arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            two -= 1
            arr[i], arr[two] = arr[two], arr[i]
        else:
            zero += 1
            arr[i], arr[zero] = arr[zero], arr[i]
            i += 1
    return arr


if __name__ == '__main__':
    arr = [2, 0, 2, 1, 1, 0]
    sortColors(arr)
