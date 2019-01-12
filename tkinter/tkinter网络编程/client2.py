import tkinter  # 导入Tkinter模块
from PIL import Image, ImageTk

root = tkinter.Tk()
canvas = tkinter.Canvas(root,
                        width=500,  # 指定Canvas组件的宽度
                        height=600,  # 指定Canvas组件的高度
                        bg='white')  # 指定Canvas组件的背景色
# im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open("test.jpg")
im = ImageTk.PhotoImage(image)

canvas.create_image(250, 200, image=im)  # 使用create_image将图片添加到Canvas组件中
canvas.create_text(302, 77,  # 使用create_text方法在坐标（302，77）处绘制文字
                   text='Use Canvas'  # 所绘制文字的内容
                   , fill='gray')  # 所绘制文字的颜色为灰色
canvas.create_text(300, 75,
                   text='Use Canvas',
                   fill='blue')
canvas.pack()  # 将Canvas添加到主窗口
root.mainloop()