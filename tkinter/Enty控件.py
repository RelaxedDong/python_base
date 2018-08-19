#encoding:utf-8
import tkinter

win = tkinter.Tk()
win.geometry("400x400")
#绑定变量

e = tkinter.Variable()
enty = tkinter.Entry(win,text='hello enty',textvariable=e)
# 写内容：
# e.set('xxx')

#获取内容
# e.get或者enty.get()
button = tkinter.Button(win,text='click me',command=lambda :print(e.get()))
content = e.get()
button.pack()
enty.pack()
import time
time.sleep(2)
label = tkinter.Label(win,text=content)
label.pack()

win.mainloop()


