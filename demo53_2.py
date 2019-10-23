import tkinter
import tkinter.font


def func1(ev):
    label1.config(text=f"cursor enter into region from [{ev.x}/{ev.y}]")
    print(type(ev), ev)


def func2(ev):
    label1.config(text=f"cursor leave region from[{ev.x}/{ev.y}]")


def func3(ev):
    label1.config(text='left single')


def func4(ev):
    label1.config(text="scroll double")


def func5(ev):
    label1.config(text='right drag')

def func6(ev):
    label1.config(text='left double')

top = tkinter.Tk()
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label1 = tkinter.Label(top, text="display status", font=myFont1)
button1 = tkinter.Button(top, text="region", font=myFont1,
                         padx=30, pady=30, bg='#C0FFEE')
button2 = tkinter.Button(top, text="listen to event", font=myFont1,
                         padx=10, pady=10, bg='#C0EEFF')
button1.bind('<Leave>', func2)
button1.bind('<Enter>', func1)
button2.bind('<Button-1>', func3)
button2.bind('<Double-2>', func4)
button2.bind('<B3-Motion>', func5)
button2.bind('<Double-1>', func6)
label1.pack()
button1.pack()
button2.pack()
top.minsize(850, 500)
top.maxsize(850, 500)
top.mainloop()