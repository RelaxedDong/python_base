#encoding:utf-8

import tkinter
def func():
    print('我是哈市')
win = tkinter.Tk()
win.geometry('400x400')
button1 = tkinter.Button(win,text='点击我',bg='pink',width=10,height=1,command=func)
button2 = tkinter.Button(win,text='点击我',bg='pink',width=10,height=1,command=lambda :print('我是大帅哥！'))
button3 = tkinter.Button(win,text='退出',bg='pink',width=10,height=1,command=win.quit)
button1.pack()
button2.pack()
button3.pack()
win.mainloop()