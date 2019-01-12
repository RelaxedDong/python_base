#encoding:utf-8
import socket               # 导入 socket 模块
import tkinter
import threading
from datetime import datetime

s = socket.socket()  # 创建 socket 对象


def func():
    host = ipplace_text.get()
    port = port_text.get()
    s.connect((host, int(port)))
    recv = bytes.decode(s.recv(1024))
    text.insert(tkinter.INSERT,  '服务器：'+recv +'  '+ str(datetime.now())[:19] + '   ')
    while True:
        message = bytes.decode(s.recv(1024))
        if not message:
            break
        text.insert(tkinter.INSERT, '服务器：'+message + '   ' + str(datetime.now())[:19] + '   ')
    s.close()

def CloseListen():
    s.close()

def func2():
    t = input_text.get()
    text.insert(tkinter.INSERT,'客户端：'+ t +'   '+str(datetime.now())[:19]+'   ')
    s.send(bytes(t, encoding='utf-8'))

def thredt_it():
    t = threading.Thread(target=func)
    # 启动
    t.start()

def SendMsg():
    t2 = threading.Thread(target=func2)
    t2.start()

def Clear():
    text.delete('1.0', 'end')

win = tkinter.Tk()
win.geometry("500x700")
win.title('客户端')
ipplace_label = tkinter.Label(win,width=10,text='ip地址：')
ipplace_label.pack()

ipplace_text = tkinter.Entry(win)
ipplace_text.pack()

port_label = tkinter.Label(win,width=10,text='端口号：')
port_label.pack()

port_text = tkinter.Entry(win)
port_text.pack()

button1 = tkinter.Button(win,text='连接',bg='pink',width=10,height=1,command=thredt_it)
button1.pack(pady=10)

button4 = tkinter.Button(win,text='断开连接',bg='pink',width=10,height=1,command=CloseListen)
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

