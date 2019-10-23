import tkinter
import tkinter.font


def motion(ev):
    message1.config(text=textBody % (ev.x, ev.y))


top = tkinter.Tk()
textBody = "move to [%d,%d]"
myFont1 = tkinter.font.Font(family='Lucida Sans',
                            size=30)
message1 = tkinter.Message(top, text=textBody % (0, 0),
                           font=myFont1)
message1.pack()
top.bind('<Motion>', motion)
top.minsize(850, 500)
top.maxsize(850, 500)
top.mainloop()
