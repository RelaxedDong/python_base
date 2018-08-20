#encoding:utf-8
#列表框控件，可以包含一个或者多个文本

# 作用：在listbox控件的小窗体中显示一个字符串
import tkinter

win = tkinter.Tk()
win.geometry("400x400")

#创建一个listbox，添加几个元素


lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
for item in ['good','nice','handsome','cool']:
    #按顺序添加
    lb.insert(tkinter.END,item)

#在开始添加
lb.insert(tkinter.END,['donghao greet','aaa'])

#删除
# lb.delete(1)

# lb.select_set(1,4)

#取消选中
# lb.select_clear()

# print(lb.get(2,4))

#返回当前索引项，不是item元素
# print(lb.curselection())


#判断一个选项是否被选中
print(lb.selection_includes(1))
print(lb.size())

lb.pack()

win.mainloop()










