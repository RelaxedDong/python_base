#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/7 21:47

def RemoveNum(arr,val):
    index = 0
    for x in range(0,len(arr)):
        if arr[x]!= val:
            arr[index] = arr[x]
            index += 1

    return index


if __name__ == '__main__':
    arr = [3,2,5,1,2,7,5,8,7]
    val = 2
    RemoveNum(arr,val)