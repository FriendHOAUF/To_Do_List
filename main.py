from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    pass

def save_file():
    pass


def save_As():

    files = [('All File', '*.*'),
             ('Python File', '*.py'),
             ('Text File', '*.txt')]
    
    file = asksaveasfile(filetypes=files, defaultextension=files)

    if file:
        file.write(text_area.get(1.0, END))
        file.close()

def open_file():
    text_file = filedialog.askopenfilename()
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    text_area.insert(END, stuff)
    text_file.close()

def quit():
    root.destroy()


def chack_ception_save():
    global file_saved
    if file_saved:
        file_saved = False
        root.title("*Untitled - Myapp")

""" 
Function wanted
1. check the title of the window 
    - if the end of title name have a ' * ' 
    mean not yet save

"""


root = Tk()
root.geometry("1400x800")
root.title("To-Do List appication")

file_saved = True

w = Label(root, text="Task")
w.pack()

root.bind()

text_area = Text(root)
text_area.pack(fill=BOTH, expand=True)


menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=new_file)
file.add_command(label="Open File", command=open_file)
file.add_command(label="Save File", command=save_file)
file.add_command(label="Save As...", command=save_As)
file.add_separator()
file.add_command(label="Exit", command=quit)

text_area.bind("<<Modified>>", lambda e: chack_ception_save())
text_area.edit_modified(False )

root.bind('<Control-s>', lambda event: chack_ception_save())

root.config(menu=menubar)
mainloop()