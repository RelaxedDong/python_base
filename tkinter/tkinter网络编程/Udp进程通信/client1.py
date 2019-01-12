#encoding:utf-8
import tkinter
from socket import *

import threading
import time
from datetime import datetime

s = socket(AF_INET,SOCK_DGRAM)  # 创建 socket 对象



def thredt_it():
    t = threading.Thread(target=func)
    t.setDaemon(True)
    # 启动
    t.start()

def SendMsg():
    t2 = threading.Thread(target=func2)
    t2.start()

def func2():
    global s
    t = input_text.get()
    host = ipplace_text4.get()
    port = port_text6.get()
    s.connect((host, int(port)))
    s.sendto(bytes(t, encoding='utf-8'),(host,int(port)))

def func():
    global s
    host = ipplace_text.get()
    port = port_text.get()
    s.bind((host, int(port)))
    text.insert(tkinter.INSERT, '本机进程启动成功...' + ' ')
    text.insert(tkinter.INSERT, 'host：'+host+'port：'+port)
    while True:
        data, address = s.recvfrom(1024)
        data = bytes.decode(data)
        text.insert(tkinter.INSERT,str(address) + '     :' + str(data))
    s.close()


win = tkinter.Tk()
win.geometry("500x700")
win.title('UDPproce2')


ipplace_label = tkinter.Label(win,width=10,text='ip地址：')
ipplace_label.pack()

ipplace_text = tkinter.Entry(win)
ipplace_text.pack()

port_label = tkinter.Label(win,width=10,text='端口号：')
port_label.pack()

port_text = tkinter.Entry(win)
port_text.pack()

button1 = tkinter.Button(win,text='启动',bg='pink',width=10,height=1,command=thredt_it)
button1.pack(pady=10)

input_text_label = tkinter.Label(win,width=20,text='请输入内容：')
input_text_label.pack()

input_text = tkinter.Entry(win,width=100)
input_text.pack()

button2 = tkinter.Button(win,text='发送',bg='pink',width=10,height=1,command=SendMsg)
button2.pack(pady=10)




ipplace_labe3 = tkinter.Label(win,width=10,text='目标ip：')
ipplace_labe3.pack()

ipplace_text4 = tkinter.Entry(win)
ipplace_text4.pack()

port_labe5 = tkinter.Label(win,width=10,text='目标端口号：')
port_labe5.pack()

port_text6 = tkinter.Entry(win)
port_text6.pack()



text_label = tkinter.Label(win,width=10,text='聊天记录：')
text_label.pack()

text = tkinter.Text(win,width=100,height=20)
text.pack()

button3 = tkinter.Button(win,text='清空聊天记录',bg='pink',width=10,height=1,command=SendMsg)
button3.pack(pady=10)

button5 = tkinter.Button(win,text='退出',bg='pink',width=10,height=1,command=lambda :win.quit())
button5.pack(pady=10)

win.mainloop()
