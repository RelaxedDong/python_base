import pickle

mylist = [1,234,23,'董豪']

f = open('test1.txt','wb')
pickle.dump(mylist,f)
f.close()


with open('test1.txt','rb') as f:
    templist = pickle.load(f)
    print(templist)