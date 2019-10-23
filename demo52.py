import tkinter
import tkinter.font

top = tkinter.Tk()
for font in tkinter.font.families():
    print(font)
myFont1 = tkinter.font.Font(family='Lucida Sans',size=30)
myFont2 = tkinter.font.Font(family='Times New Roman',size=10)

label1 = tkinter.Label(top, text='hello TK', padx=10,
                       pady=10, bg='#0F0', font=myFont1)
label2 = tkinter.Label(top, text='hello pycharm', bg='#F00',
                       font=myFont2)
button1 = tkinter.Button(top, text='click me', font=myFont1)
button2 = tkinter.Button(top, text='click me2', font=myFont2)
label1.pack()
label2.pack()
button1.pack()
button2.pack()
top.mainloop()