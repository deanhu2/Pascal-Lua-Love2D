import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()
root.state('zoomed')
#setup full sized window

#defined styles
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
style.map("C.TBar",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

#functions for menu
def hello():
    print ("hello!")

#menu definition
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_command(label="Save as...", command=hello)
filemenu.add_command(label="Close", command=hello)
menubar.add_cascade(label="File", menu=filemenu)


#toolbar setup
toolbar = Frame(root)
b = ttk.Button(toolbar, text="new", style="C.TButton", width=6, command=hello)
b.pack(side=LEFT, padx=2, pady=2)
b = ttk.Button(toolbar, text="open", style="C.TButton", width=6, command=hello)
b.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


#tabbed panes
n = ttk.Notebook(root)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
n.add(f1, text='One')
n.pack()

#colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.config(menu=menubar)
root.mainloop()
