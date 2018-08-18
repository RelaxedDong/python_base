# 标签控件,可以显示文本
import tkinter

win = tkinter.Tk()

label = tkinter.Label(win,text='hello world',bg='pink',
                      fg='green',
                      font=('黑体',20),
                      width=20,
                      height=20,
                      wrapleng=100,
                      justify="left",
                      anchor="c")
# wrapleng指定text文本中多宽进行换行
#justify指定换行后的对齐方式
#anchor位置

label.pack()
win.title('我是label')

win.mainloop()



