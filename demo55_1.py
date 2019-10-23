import tkinter
import tkinter.font

def funcX():
    if sel1.get() == 1:
        label.config(text="pixel4")
    elif sel1.get() == 2:
        label.config(text='iphone11ProMax')


top = tkinter.Tk()
sel1 = tkinter.IntVar()
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label = tkinter.Label(top, text='your choice is:', font=myFont1)
label.pack()
r1 = tkinter.Radiobutton(top, text="Google", font=myFont1, value=1,
                         variable=sel1, command=funcX)
r2 = tkinter.Radiobutton(top, text="Apple", font=myFont1, value=2,
                         variable=sel1, command=funcX)
r1.pack()
r2.pack()
top.minsize(850, 500)
top.maxsize(850, 500)
top.mainloop()