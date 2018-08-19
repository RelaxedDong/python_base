# import time
from dongProcess import myProcess

# print(time.time())
# import random
# print(random.choice([2,3,4,5]))

if __name__ == '__main__':
    print('父进程开始')
    p1 = myProcess('donghao1')
    #自动调用run()方法
    p2 = myProcess('donghao2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('子进程结束')
