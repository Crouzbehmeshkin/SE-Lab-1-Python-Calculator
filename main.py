from tkinter import *
from decimal import Decimal

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
    
    def click(self, text, write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on screen,
        # if None, should not be written on screen
        if self.equation_evaluated:
            self.clear_screen()
        self. equation_evaluated = False
        if write is None:
            # only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                # replace the unicode value of division ./. with python division symbol / using regex
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                answer = self.evaluate(self.equation)
                self.clear_screen()
                self.insert_screen(answer, newline=True)
                self. equation_evaluated = True
            elif text == u"\u232B":
                self.clear_screen()
        else:
            # add text to screen
            self.insert_screen(text)

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
        
        finallist = []
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