from tkinter import *
from tkinter import ttk
import string

root = Tk()
root.geometry("300x250+400+200")

root.maxsize(400,300)
root.resizable(False, False)
root.title("3rd exercise")

# UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Helvetica', 11)}

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)


def get_names():
    input_file_name = inputFileName_entry.get()
    print('input file name: ' + input_file_name)
    output_file_name = outputFileName_entry.get()
    print('output file name: ' + output_file_name)
    print('name output has ended')
    root.destroy()
    working_with_files(input_file_name, output_file_name)
    #TODO разобраться с асинхронностью здесь


def working_with_files(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        output_file.writelines([line])
    input_file.close()
    output_file.close()
    print('This program has finished working')


# heading
heading = ttk.Label(root,  text='Member Login')
heading.grid(column=1, row=0, columnspan=2, pady=5, sticky=N)

inputFileNameString = StringVar()
outputFileNameString = StringVar()

inputFileName_label = ttk.Label(root, text="Input file:")
inputFileName_label.grid(column=0, row=1, sticky=W, **paddings)

inputFileName_entry = ttk.Entry(root, textvariable=inputFileNameString, **entry_font)
inputFileName_entry.grid(column=1, columnspan=3, row=1, sticky=E, **paddings)

outputFileName_label = ttk.Label(root, text="Output file:")
outputFileName_label.grid(column=0, row=2, sticky=W, **paddings)

outputFileName_entry = ttk.Entry(root, textvariable=outputFileNameString, **entry_font)
outputFileName_entry.grid(column=1, columnspan=3, row=2, sticky=E, **paddings)


btn = ttk.Button(text="Click", command=get_names)
btn.grid(column=1, columnspan=2, row=3, sticky=S, **paddings)



root.mainloop()


#if __name__ == '__main__':

