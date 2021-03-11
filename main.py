from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=30, height=3, background="grey", foreground="blue")

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''
    
    def clear_screen(self):
        # to clear screen
        # set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)


root = Tk()
main_gui = Calculator(root)
root.mainloop()