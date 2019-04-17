#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/16 12:42

"""

IO多路复用: select,poll,epoll

epoll:（有水平触发，竖直出发两种）
1. 有一个特殊的内存，是 操作系统核(kernel) 和 应用程序共享
2. 里面需要的监听的套接字，去检测的时候方式不是轮询，是时间通知。

1、没有最大并发连接的限制，能打开的FD的上限远大于1024（1G的内存上能监听约10万个端口）；
即Epoll最大的优点就在于它只管你“活跃”的连接，而跟连接总数无关，因此在实际的网络环境中，Epoll的效率就会远远高于select和poll。

3、 内存拷贝，利用mmap(内存映射)文件映射内存加速与内核空间的消息传递；即epoll使用mmap减少复制开销。

水平触发：
当监听的套接字没有被处理时，会一直被通知；

边缘触发：
只通知一次，监听的套接字没有被处理会被丢弃；
"""

from socket import *

s = socket(2,1)
s.setsockopt(1,2,1)
s.bind(('',8080))
s.listen(1024)

s_dict = {}

epoll_instance = epoll()
epoll_instance.register(s.fileno(),EPOLLIN|EPOLLET)
while 1:
    epoll_list = epoll_instance.poll()  #默认会堵塞，直到os检测到数据的到来，通过事件通知的方式 告诉这个程序，此时才会解堵塞

    for fd,event in epoll_list: #（fd: 文件描述符  ，  event事件）
        if fd == s.fileno():
            cs,userinfo = s.accept()
            epoll_instance.register(cs.fileno(),EPOLLIN|EPOLLET)
            s_dict[cs.fileno()] = cs
        else:
            cs = s_dict[fd]
            recv_data = cs.recv(1024)
            print(recv_data.decode('gb2312'))
            if len(recv_data) > 0 :
                cs.send(recv_data)
            else:
                print('adsfasdf')
                epoll_instance.unregister(fd) #移除
                cs.close()
                s_dict.pop(fd) #移除套接字



























