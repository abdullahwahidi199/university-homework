from tkinter import *
from tkinter import ttk

window = Tk()
window.title("my homeworks")
notebook = ttk.Notebook(window, width=1000, height=1000)

tab2 = Frame(notebook, bg="#F2EAC7")
tab3 = Frame(notebook, bg="#F2EAC7")

notebook.add(tab2, text="first HW")
notebook.add(tab3, text="second HW")
notebook.pack(expand=1, fill='both')
notebook.pack(expand=TRUE, fill="both")

filepath = open("buitl in functions.py", "r")

content = filepath.read()

label2 = Label(tab2, text=content, bg="#F2EAC7", justify=LEFT)

label2.pack(anchor='w', padx=10, pady=4)


def load():
    n = open(f'{path_entry.get()}', 'r')
    content1 = n.read()

    new_win = Tk()
    new_win_label = Label(new_win, text=content1, justify=LEFT)
    new_win_label.pack()


path_entry = Entry(tab3, width=22)

path_label = Label(tab3, text="due to size bigness enter\nthe file path u want below:", bg="#F2EAC7", )
path_label.pack(anchor='w')
path_entry.pack(anchor='w')

load_button = Button(tab3, text="load file", command=load)
load_button.place(x=35, y=61)

window.mainloop()
