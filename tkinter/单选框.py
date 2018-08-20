#encoding:utf-8
import tkinter

win = tkinter.Tk()
win.geometry("400x400")

#绑定变量
#一组单选框要绑定同一变量
r = tkinter.StringVar()
def update():
    print(r.get())
radio1 = tkinter.Radiobutton(win,text='one',value='good',variable=r,
                             command=update)
radio2 = tkinter.Radiobutton(win,text='two',value='nice',variable=r,
                             command=update)


radio1.pack()
radio2.pack()

win.mainloop()


