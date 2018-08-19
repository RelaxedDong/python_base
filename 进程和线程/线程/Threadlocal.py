import threading

#创建一个全局的threadlocal对象
#每个线程由独立的存储空间
# 每个线程对Threadlocal对象都可以读写，但互不影响

local = threading.local()


def sum(x,n):
    x = x+n
    x = x-n

def run(num):
    local.x = num
    for i in range(10000):
        sum(local.x,num)
    print('%s-%d'%(threading.current_thread().name,local.x))

if __name__ == '__main__':
    print('父线程启动！')
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('父线程结束！')

#作用：为每个线程绑定一个数据库，http请求，用户登录信息等，这样一个
# 线程所有的调用到的处理函数都可以非常方便地访问这些资源