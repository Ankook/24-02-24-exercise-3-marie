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

inputFileName = StringVar()
outputFileName = StringVar()

inputFileName_label = ttk.Label(root, text="Input file:")
inputFileName_label.grid(column=0, row=0, sticky=W, **paddings)

inputFileName_entry = ttk.Entry(root, textvariable=inputFileName, **entry_font)
inputFileName_entry.grid(column=1, row=0, sticky=E, **paddings)

outputFileName_label = ttk.Label(root, text="Input file:")
outputFileName_label.grid(column=0, row=1, sticky=W, **paddings)

outputFileName_entry = ttk.Entry(root, textvariable=outputFileName, **entry_font)
outputFileName_entry.grid(column=1, row=1, sticky=E, **paddings)


root.mainloop()


if __name__ == '__main__':
    print('Hello!');
