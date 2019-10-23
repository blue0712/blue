import tkinter
import tkinter.font

counter = 1


def button1():
    global counter
    print("button clicked %d times")
    label1.config(text='button clicked %d times' % counter)
    counter += 1


counters = [1]

def button2():
    label2.config(text='button clicked %d times' % counters[0])
    counters[0] += 1


top = tkinter.Tk()
for font in tkinter.font.families():
    print(font)
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
label1 = tkinter.Label(top, text='hello TK', padx=10,
                       pady=10, bg='#0F0', font=myFont1)
label2 = tkinter.Label(top, text='hello pycharm', bg='#F00',
                       font=myFont1)
button1 = tkinter.Button(top, text='click me', font=myFont1,
                         command=button1)
button2 = tkinter.Button(top, text='click me2', font=myFont1,
                         command=button2)
label1.pack()
label2.pack()
button1.pack()
button2.pack()
top.mainloop()
