from tkinter import *
from tkinter import messagebox

myGui = Tk()

def hello():
    b = a.get()
    myLabel3 = Label(text = b, fg = 'red', bg = 'yellow', font = 10)
    myLabel3.pack()

def dele():
    myLabel1 = Label(text = 'deleted', fg = 'red', bg = 'yellow', font = 10)
    myLabel1.pack()

def newfi():
    myLabel1 = Label(text = 'clicked on new file', fg = 'red', bg = 'yellow', font = ('roman', 24, 'italic'))
    myLabel1.pack()

def mbox():
    messagebox.showinfo(title='Save', message = 'are you sure to save?')

def mquit():
    mess = messagebox.askyesno(title = 'Quit', message = 'Are you sure to quit?')
    if mess == 1:
        myGui.destroy()


a = StringVar()
myGui.title('Hello')
myGui.geometry('500x500+100+100')

myLabel1 = Label(text = 'label one', fg = 'red', bg = 'yellow', font = ('arial', 24, 'italic')).pack()
myButton1 = Button(text = 'Enter', fg = '#2f363d', bg = '#9EC129', command = hello, font = ('times', 24, 'bold')).pack()
myButton2 = Button(text = 'Delete', fg = '#0D0000', bg = '#8B0000', command = dele, font = 20).pack()
text = Entry(textvariable = a).pack()

mymenu = Menu()
listone = Menu()
listtwo = Menu()

listone.add_command(label = 'New File', command = newfi)
listone.add_command(label = 'Open File')
listone.add_command(label = 'Save File', command = mbox)
listone.add_command(label = 'Quit', command = mquit)

listtwo.add_command(label = 'undo')
listtwo.add_command(label = 'redo')

mymenu.add_cascade(label = 'File', menu = listone)
mymenu.add_cascade(label = 'Edit', menu = listtwo)
mymenu.add_cascade(label = 'Format')
mymenu.add_cascade(label = 'Run')

myGui.config(menu = mymenu)



myGui.mainloop()