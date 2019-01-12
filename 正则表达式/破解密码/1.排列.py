import itertools


mylist = [1,2,3,4]

list1 = list(itertools.permutations(mylist,3))
print(list1)
print(len(list1))