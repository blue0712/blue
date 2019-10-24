import tkinter
import tkinter.font

formattedString = "value=%d"


def func1(scale):
    label1.config(text=formattedString % (int(scale) * 2))


top = tkinter.Tk()
value = tkinter.IntVar()
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label1 = tkinter.Label(top, text=formattedString % 0, font=myFont1)
scale1 = tkinter.Scale(top, label='var', font=myFont1,
                       orient='h', from_=0, to=100, command=func1)
label1.pack()
scale1.pack()
top.minsize(850, 500)
top.maxsize(850, 500)
top.mainloop()