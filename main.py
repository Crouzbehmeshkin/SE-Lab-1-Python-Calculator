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
    
    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state='disabled')


    def solve_equation(self, termslist):
        newlist = []
        index = 0
        while index < len(newlist):
            if newlist[index] == '+' or newlist[index] == '-':
                if newlist[index] == '+':
                    finallist.append(Decimal(finallist.pop()) + Decimal(newlist[index+1]))
                    index += 1
                if newlist[index] == '-':
                    finallist.append(Decimal(finallist.pop()) - Decimal(newlist[index + 1]))
                    index += 1
            else:
                finallist.append(newlist[index])
            index += 1
        index = 0
        finallist = []
        while index < len(termslist):
            if termslist[index] == '*' or termslist[index] == '/':
                if termslist[index] == '*':
                    newlist.append(Decimal(newlist.pop()) * Decimal(termslist[index+1]))
                    index += 1
                if termslist[index] == '/':
                    newlist.append(Decimal(newlist.pop()) / Decimal(termslist[index + 1]))
                    index += 1
            else:
                newlist.append(termslist[index])
            index += 1        
        if len(finallist) != 1:
            return self.solve_equation(finallist)
        else:
            return str(finallist[0])

    def find_terms(self, termslist, equation):
        index = 0
        while equation is not None:
            if len(equation) == index:
                termslist.append(equation[:index])
                return termslist
            if equation[index] == '*' or equation[index] == "/" or equation[index] == "+" or equation[index] == "-":
                if index == 0:
                    termslist.append(equation[index])
                    equation = equation[(index+1):]
                else:
                    termslist.append(equation[:index])
                    equation = equation[index:]
                index = -1
            index += 1

    def evaluate(self, equation):
        termslist = []
        termslist = self.find_terms(termslist, equation)
        answer = self.solve_equation(termslist)
        return answer


root = Tk()
main_gui = Calculator(root)
root.mainloop()