import tkinter
import tkinter.font


def display(ev):
    label1.config(text=entry1.get())


top = tkinter.Tk()
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label1 = tkinter.Label(top, text='Display something',
                       font=myFont1)
entry1 = tkinter.Entry(top, font=myFont1)
entry1.insert(0, 'input something here...')
button1 = tkinter.Button(top, text='submit',
                         font=myFont1)
button1.bind('<Button-1>', display)
entry1.bind('<Return>', display)
label1.pack()
entry1.pack()
button1.pack()
top.minsize(850, 500)
top.maxsize(850, 500)
top.mainloop()