#encoding:utf-8
import time

# def maxsum(a,n):
#     sum = 0
#     maxsum = 0
#     i = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum +=a[j]
#             if(sum>maxsum):
#                 maxsum = sum;
#             j+=1
#         i+=1
#     return maxsum

#分而治之
def max(a,left,right):
    sum=i=ret=center=leftmax=rightmax=left_max=right_max= 0
    if right == left:
        return a[left] if a[left] > 0 else 0
    center = (left + right) / 2
    leftmax = max(a, left, center)
    rightmax = max(a, center + 1, right)
    sum = left_max = 0
    for i in range(left,center):
        sum += a[i]
        if (sum > left_max):
            left_max = sum
        i-=1
    sum = 0
    right_max = 0
    for i in range(center+1,right):
        sum += a[i]
        if sum>right_max:
            right_max = sum
        i+=1
    ret = left_max+right_max;
    if(ret <leftmax):
        ret = leftmax;
    if(ret<rightmax):
        ret = rightmax;
    return ret



# 动态规划：
def maxSum(list_of_nums):
    maxsum = 0
    maxtmp = 0
    for i in range(len(list_of_nums)):
        if maxtmp <= 0:
            maxtmp = list_of_nums[i]
        else:
            maxtmp += list_of_nums[i]

        if (maxtmp > maxsum):
            maxsum = maxtmp
    return maxsum

if __name__ == '__main__':
    start = time.time()
    a = [-2,11,-4,13,-5,-2]*1000
    print(maxSum(a))


    end = time.time()
    time = start-end
    print('耗时：%0.002f' % (end - start))