#encoding:utf-8
import tkinter

win = tkinter.Tk()
win.geometry("400x400")
win.title('donghao')

def updata():
    message = ""
    if hoby1.get() == True:
        message+="钱\n"
    if hoby2.get() == True:
        message+="权利\n"
    if hoby3.get() == True:
        message+="人际\n"
    print(message)
        #删除text中的所有内容
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)

hoby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win,text='钱',variable=hoby1,command=updata)

hoby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text='权利',variable=hoby2,command=updata)

hoby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text='人际',variable=hoby3,command=updata)

text = tkinter.Text(win,width=80,height=5)

check1.pack()
check2.pack()
check3.pack()
text.pack()
win.mainloop()


