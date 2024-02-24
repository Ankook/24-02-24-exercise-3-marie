import tkinter as tk
from tkinter import ttk
import string
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x250+400+200")

        self.maxsize(400, 300)
        self.resizable(False, False)
        self.title("3rd exercise")

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        def get_names():
            input_file_name = input_file_name_entry.get()
            print('input file name: ' + input_file_name)
            output_file_name = output_file_name_entry.get()
            print('output file name: ' + output_file_name)
            print('name output has ended')
            self.destroy()
            working_with_files(input_file_name, output_file_name)
            # TODO разобраться с асинхронностью здесь

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

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 15))

        # heading
        heading = ttk.Label(self, text='Entering names', style='Heading.TLabel')
        heading.grid(column=1, row=0, columnspan=2, pady=5, sticky=tk.N)

        input_file_name_string = tk.StringVar()
        output_file_name_string = tk.StringVar()

        #input label
        input_file_name_label = ttk.Label(self, text="Input file:")
        input_file_name_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        #input entry
        input_file_name_entry = ttk.Entry(self, textvariable=input_file_name_string, **entry_font)
        input_file_name_entry.grid(column=1, columnspan=3, row=1, sticky=tk.E, **paddings)

        #output label
        output_file_name_label = ttk.Label(self, text="Output file:")
        output_file_name_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        #output_entry
        output_file_name_entry = ttk.Entry(self, textvariable=output_file_name_string, **entry_font)
        output_file_name_entry.grid(column=1, columnspan=3, row=2, sticky=tk.E, **paddings)

        #submit button
        btn = ttk.Button(text="Click", command=get_names)
        btn.grid(column=1, columnspan=2, row=3, sticky=tk.S, **paddings)


if __name__ == '__main__':
    app = App()
    app.mainloop()

