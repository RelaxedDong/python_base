# -*- coding: utf-8 -*-

import socket
import sys
import threading



def start_listen():
    con = threading.Condition()
    host = ipplace_text.get()

    PORT = 8888  # Arbitrary non-privileged port
    data = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print('Socket created')
    text.insert(tkinter.INSERT, 'Socket created')
    s.bind((host, PORT))
    s.listen(10)
    text.insert(tkinter.INSERT,'Socket now listening')
    # print('Socket now listening')

    # Function for handling connections. This will be used to create threads
    def clientThreadIn(conn, nick):
        global data
        # infinite loop so that function do not terminate and thread do not end.
        while True:
            # Receiving from client
            try:
                temp = conn.recv(1024)
                if not temp:
                    conn.close()
                    return
                NotifyAll(temp)
                # print(data)
                text.insert(tkinter.INSERT, data)
            except:
                # NotifyAll(nick + " leaves the room!")
                text.insert(tkinter.INSERT, nick + " leaves the room!")
                # print(data)
                text.insert(tkinter.INSERT, data)
                return

        # came out of loop

    def NotifyAll(sss):
        global data
        if con.acquire():
            data = sss
            con.notifyAll()
            con.release()

    def ClientThreadOut(conn, nick):
        global data
        while True:
            if con.acquire():
                con.wait()
                if data:
                    try:
                        conn.send(data)
                        con.release()
                    except:
                        con.release()
                        return

    while 1:
        # wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        text.insert(tkinter.INSERT,'Connected with ' + addr[0] + ':' + str(addr[1]))

        nick = bytes.decode(conn.recv(1024))
        # send only takes string
        # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        NotifyAll(str('Welcome ' + nick + ' to the room!'))
        text.insert(tkinter.INSERT, str('Welcome ' + nick + ' to the room!'))
        text.insert(tkinter.INSERT, data)

        print(data)
        print(str((threading.activeCount() + 1) / 2) + ' person(s)!')
        text.insert(tkinter.INSERT,str((threading.activeCount() + 1) / 2) + ' person(s)!')
        conn.send(bytes(data, encoding='utf-8'))
        threading.Thread(target=clientThreadIn, args=(conn, nick)).start()
        threading.Thread(target=ClientThreadOut, args=(conn, nick)).start()
    s.close()


import tkinter
def thredt_it():
    t = threading.Thread(target=start_listen)
    t.setDaemon(True)
    # 启动
    t.start()

win = tkinter.Tk()
win.geometry("500x700")
win.title('UDPproce2')

ipplace_label = tkinter.Label(win, width=10, text='ip地址：')
ipplace_label.pack()

ipplace_text = tkinter.Entry(win)
ipplace_text.pack()

button1 = tkinter.Button(win, text='启动', bg='pink', width=10, height=1, command=thredt_it)
button1.pack(pady=10)

text_label = tkinter.Label(win, width=10, text='聊天记录：')
text_label.pack()

text = tkinter.Text(win, width=100, height=20)
text.pack()

button3 = tkinter.Button(win, text='清空聊天记录', bg='pink', width=10, height=1, command='')
button3.pack(pady=10)
win.mainloop()