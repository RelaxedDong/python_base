#encoding:utf-8
import tkinter
import socket
import threading
import time
from datetime import datetime

s = socket.socket()  # 创建 socket 对象
        # host = ipplace_text.get()  # 获取本地主机名
        # port = port_text.get()  # 设置端口


sender = ''
ccc = ''

def func():
    host = ipplace_text.get()
    port = port_text.get()
    s.bind((host, int(port)))  # 绑定端口
    # print(port_text.get())
    # 绑定端口
      # 建立客户端连接。
     # 等待客户端连接
    text.insert(tkinter.INSERT, '等待客户端连接...' + '      ')
    s.listen(5)
    global sender
    c, addr = s.accept()
    text.insert(tkinter.INSERT, '连接成功...地址：' + addr[0]+'     ')
    strr = bytes('你好客户端，欢迎访问服务器~!                    ', encoding="utf8")
    c.send(strr)
    sender = c
    while True:
        message = c.recv(1024)
        if not message:
            break
        message = bytes.decode(message)
        text.insert(tkinter.INSERT,'客户端：'+message+'  '+str(datetime.now())[:19]+'      ')
    c.close()  # 关闭连接

def thredt_it():
    t = threading.Thread(target=func)
    t.setDaemon(True)
    # 启动
    t.start()

def Clear():
    text.delete('1.0','end')

def func2():
    global sender
    t = input_text.get()
    text.insert(tkinter.INSERT,'服务器：'+ t +'  '+str(datetime.now())[:19]+'   ')
    while True:
        sender.send(bytes(t, encoding='utf-8'))
        break



def SendMsg():
    t2 = threading.Thread(target=func2)
    t2.start()



def CloseListen():
    global sender
    sender.close()



win = tkinter.Tk()
win.geometry("500x700")
win.title('服务器端')


ipplace_label = tkinter.Label(win,width=10,text='ip地址：')
ipplace_label.pack()

ipplace_text = tkinter.Entry(win)
ipplace_text.pack()

port_label = tkinter.Label(win,width=10,text='端口号：')
port_label.pack()

port_text = tkinter.Entry(win)
port_text.pack()

button1 = tkinter.Button(win,text='开始监听',bg='pink',width=10,height=1,command=thredt_it)
button1.pack(pady=10)

button4 = tkinter.Button(win,text='停止监听',bg='pink',width=10,height=1,command=CloseListen)
button4.pack(pady=10)

input_text_label = tkinter.Label(win,width=20,text='请输入内容：')
input_text_label.pack()

input_text = tkinter.Entry(win,width=100)
input_text.pack()

button2 = tkinter.Button(win,text='发送',bg='pink',width=10,height=1,command=SendMsg)
button2.pack(pady=10)

text_label = tkinter.Label(win,width=10,text='聊天记录：')
text_label.pack()

text = tkinter.Text(win,width=100,height=20)
text.pack()

button3 = tkinter.Button(win,text='清空聊天记录',bg='pink',width=10,height=1,command=Clear)
button3.pack(pady=10)

button5 = tkinter.Button(win,text='退出',bg='pink',width=10,height=1,command=lambda :win.quit())
button5.pack(pady=10)

win.mainloop()
