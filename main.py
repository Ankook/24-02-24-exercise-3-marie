from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x250+400+200")

root.maxsize(400,300)
root.resizable(False, False)

# UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Helvetica', 11)}

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

userName = StringVar()

username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=W, **paddings)

username_entry = ttk.Entry(root, textvariable=userName, **entry_font)
username_entry.grid(column=1, row=0, sticky=E, **paddings)
#TOO RENAME COLOUMNS

root.mainloop()


if __name__ == '__main__':
    print('Hello!');
