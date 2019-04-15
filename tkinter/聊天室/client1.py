# -*- coding: utf-8 -*-
import socket
import threading

inString = ''
outString = ''
nick = ''
mysock = ''

def SendMsg():
    global mysock
    DealOut(mysock)

def DealOut(s):
    global nick, outString
    while True:
        # outString = input()
        # outString = nick + ': ' + outString
        outString = str(nick + ': ' + input_text.get())
        s.send(bytes(outString, encoding='utf-8'))


def DealIn(s):
    global inString
    while True:
            try:
                inString = s.recv(1024)
                if not inString:
                    break
                if outString != inString:
                    print(inString)

            except:
                break



# sock.close()
def start_send():
    # nick = input("input your nickname: ")
    nick = nickname_text.get()

    # ip = input("input the server's ip adrress: ")

    ip = ipplace_text.get()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 8888))
    global mysock
    mysock = sock
    sock.send(bytes(nick, encoding='utf-8'))

    # thin = threading.Thread(target=DealIn, args=(sock,))
    # thin.start()
    # thout = threading.Thread(target=DealOut, args=(sock,))
    # thout.start()


import tkinter
def thredt_it():
    t = threading.Thread(target=start_send)
    t.setDaemon(True)
    # 启动
    t.start()

win = tkinter.Tk()
win.geometry("500x300")
win.title('UDPproce2')


nickname_label = tkinter.Label(win, width=10, text='输入昵称：')
nickname_label.pack()

nickname_text = tkinter.Entry(win)
nickname_text.pack()


ipplace_label = tkinter.Label(win, width=10, text='ip地址：')
ipplace_label.pack()
ipplace_text = tkinter.Entry(win)
ipplace_text.pack()


button1 = tkinter.Button(win, text='进入聊天室', bg='pink', width=10, height=1, command=SendMsg)
button1.pack(pady=10)

input_text_label = tkinter.Label(win,width=20,text='请输入内容：')
input_text_label.pack()

input_text = tkinter.Entry(win,width=100)
input_text.pack()

button2 = tkinter.Button(win,text='发送',bg='pink',width=10,height=1,command=DealOut)
button2.pack(pady=10)


win.mainloop()