import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # create text box
        self.display = tk.Entry(master, width=25, font=('Arial', 14), bd=8, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create a style for the window~
        style = ttk.Style(root)
        style.theme_use("clam")

        # create buttons for numbers and operations
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'

        ]

        # create buttons using a loop
        for i in range(len(self.buttons)):
            button = tk.Button(master, text=self.buttons[i], width=5, height=2, font=('Arial', 14), bd=5)
            button.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5)
            button.bind('<Button-1>', self.button_click)
            button.config(bg='#cfcfcf', fg='#000000', activebackground='#dcdcdc', activeforeground='#000000')

        # bind enter key to equals button
        master.bind('<Return>', self.button_click)

        # bind escape key to clear button
        master.bind('<Escape>', self.clear_display)

    def button_click(self, event):
        # get text of button that was clicked
        button_text = event.widget.cget('text')

        # handle button click based on text
        if button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.clear_display()
        else:
            self.display.insert('end', button_text)

    def calculate(self):
        try:
            # evaluate the expression in the text box
            result = eval(self.display.get())
            self.display.delete(0, 'end')
            self.display.insert('end', result)
        except:
            # handle errors
            self.display.delete(0, 'end')
            self.display.insert('end', 'Error')

    def clear_display(self, event=None):
        self.display.delete(0, 'end')


root = tk.Tk()
my_calculator = Calculator(root)
root.config(bg='#000000')
root.resizable(False, False)
root.mainloop()