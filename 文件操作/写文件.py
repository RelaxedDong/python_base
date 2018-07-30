

# f = open('test','w')
str = 'asdfasdfsdfasfd懂啊后'
# f.write(str.encode('utf-8'))
# f.close()
str = '啥的飞机轮的就是'
with open('test','wb') as f:
    f.write(str.encode('utf-8'))


with open('test','rb') as f1:

    data = f1.read()
    print(data)
    newdata = data.decode('utf-8')
    print(newdata)