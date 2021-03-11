from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

root = Tk()
main_gui = Calculator(root)
root.mainloop()