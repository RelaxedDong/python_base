#encoding:utf-8

import tkinter

win = tkinter.Tk()
win.geometry("400x400")

lbv = tkinter.StringVar()
#与browse相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)

lb.pack()
for item in ['good','nice','handsome','cool']:
    #按顺序添加
    lb.insert(tkinter.END,item)

#当前列表选项
print(lbv.get())


#设置列表选项
# lbv.set(('1','2','3'))


def muPrint(event):
    print('**************')
    #返回下标
    print(lb.curselection())
    #返回值
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>",muPrint)






win.mainloop()


