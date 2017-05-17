from Tkinter import *

master = Tk()

def makeentry(parent, caption, width=None):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

parent = master
user = makeentry(parent, "First City:", 30)
password = makeentry(parent, "Second City:", 30)
content = StringVar()

text = content.get()
content.set(text)
mainloop()
