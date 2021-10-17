from tkinter import *
import re

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""


def clr():
    global expression
    expression = ""
    equation.set("")


def callback(input):
    if re.match('[\d\*\/\.\+\-]+', input):
        print(input)
        return True

    elif input == "":
        print(input)
        return True

    else:
        print(input)
        return False


gui = Tk()


gui.configure(background="white")
gui.title("Calculator")
gui.geometry("350x180")
equation = StringVar()
reg = gui.register(callback)
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
expression_field.config(validate='key', validatecommand =(reg, '%P'))

button1 = Button(gui, text=' 1 ', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(1), highlightbackground='#3E4149')
button1.grid(row=2, column=0)

button2 = Button(gui, text=' 2 ', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(2), highlightbackground='#3E4149')
button2.grid(row=2, column=1)

button3 = Button(gui, text='3', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(3), highlightbackground='#3E4149')
button3.grid(row=2, column=2)

button4 = Button(gui, text='4', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(4), highlightbackground='#3E4149')
button4.grid(row=3, column=0)

button5 = Button(gui, text='5', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(5), highlightbackground='#3E4149')
button5.grid(row=3, column=1)

button6 = Button(gui, text='6', fg='black', bg='red', height=1, width=7
                 , command=lambda: press(6), highlightbackground='#3E4149')
button6.grid(row=3, column=2)

button7 = Button(gui, text='7', fg='black', bg='red', height=1, width=7,
                 command=lambda: press(7), highlightbackground='#3E4149')
button7.grid(row=4, column=0)

button8 = Button(gui, text='8', fg='black', bg='red', height=1, width=7,
                 command=lambda: press(8), highlightbackground='#3E4149')
button8.grid(row=4, column=1)

button9 = Button(gui, text='9', fg='black', bg='red', height=1, width=7,
                 command=lambda: press(9), highlightbackground='#3E4149')
button9.grid(row=4, column=2)

button0 = Button(gui, text='0', fg='black', bg='red', height=1, width=7,
                 command=lambda: press(0), highlightbackground='#3E4149')
button0.grid(row=5, column=0)

plus = Button(gui, text=' + ', fg='black', bg='red', height=1, width=7,
              command=lambda: press('+'), highlightbackground='#3E4149')
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='black', bg='red', height=1, width=7,
               command=lambda: press('-'), highlightbackground='#3E4149')
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', fg='black', bg='red', height=1, width=7,
                  command=lambda: press('*'), highlightbackground='#3E4149')
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', fg='black', bg='red', height=1, width=7,
                command=lambda: press('/'), highlightbackground='#3E4149')
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='black', bg='red', height=1, width=7,
               command=equal_press, highlightbackground='#3E4149')
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='black', bg='red', height=1, width=7,
               command=clr, highlightbackground='#3E4149')
clear.grid(row=5, column=1)

Decimal = Button(gui, text='.', fg='black', bg='red', height=1, width=7,
                 command=lambda: press('.'), highlightbackground='#3E4149')
Decimal.grid(row=6, column=0)

gui.mainloop()
