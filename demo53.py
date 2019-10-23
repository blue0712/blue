import tkinter
import tkinter.font


def func1(ev):
    label1.config(text="cursor enter into region")

counters = [1]
def func2(ev):
    label1.config(text="cursor leave  %d times region"% counters[0])
    counters[0] += 1


top = tkinter.Tk()
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label1 = tkinter.Label(top, text="display status", font=myFont1)
button1 = tkinter.Button(top, text="region", font=myFont1,
                         padx=30, pady=30, bg='#C0FFEE')
button1.bind('<Leave>', func2)
button1.bind('<Enter>', func1)
label1.pack()
button1.pack()
top.mainloop()
