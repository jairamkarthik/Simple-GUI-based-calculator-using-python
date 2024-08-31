from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("270x150")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 18))
    expression_field.grid(columnspan=4, ipadx=70, sticky="nsew")

    gui.grid_columnconfigure(0, weight=1)
    gui.grid_columnconfigure(1, weight=1)
    gui.grid_columnconfigure(2, weight=1)
    gui.grid_columnconfigure(3, weight=1)

    gui.grid_rowconfigure(2, weight=1)
    gui.grid_rowconfigure(3, weight=1)
    gui.grid_rowconfigure(4, weight=1)
    gui.grid_rowconfigure(5, weight=1)
    gui.grid_rowconfigure(6, weight=1)

    button_kwargs = {'fg': 'black', 'bg': 'white', 'height': 1, 'width': 7, 'font': ('Arial', 14)}

    button1 = Button(gui, text=' 1 ', command=lambda: press(1), **button_kwargs)
    button1.grid(row=2, column=0, sticky="nsew")

    button2 = Button(gui, text=' 2 ', command=lambda: press(2), **button_kwargs)
    button2.grid(row=2, column=1, sticky="nsew")

    button3 = Button(gui, text=' 3 ', command=lambda: press(3), **button_kwargs)
    button3.grid(row=2, column=2, sticky="nsew")

    button4 = Button(gui, text=' 4 ', command=lambda: press(4), **button_kwargs)
    button4.grid(row=3, column=0, sticky="nsew")

    button5 = Button(gui, text=' 5 ', command=lambda: press(5), **button_kwargs)
    button5.grid(row=3, column=1, sticky="nsew")

    button6 = Button(gui, text=' 6 ', command=lambda: press(6), **button_kwargs)
    button6.grid(row=3, column=2, sticky="nsew")

    button7 = Button(gui, text=' 7 ', command=lambda: press(7), **button_kwargs)
    button7.grid(row=4, column=0, sticky="nsew")

    button8 = Button(gui, text=' 8 ', command=lambda: press(8), **button_kwargs)
    button8.grid(row=4, column=1, sticky="nsew")

    button9 = Button(gui, text=' 9 ', command=lambda: press(9), **button_kwargs)
    button9.grid(row=4, column=2, sticky="nsew")

    button0 = Button(gui, text=' 0 ', command=lambda: press(0), **button_kwargs)
    button0.grid(row=5, column=0, sticky="nsew")

    plus = Button(gui, text=' + ', command=lambda: press("+"), **button_kwargs)
    plus.grid(row=2, column=3, sticky="nsew")

    minus = Button(gui, text=' - ', command=lambda: press("-"), **button_kwargs)
    minus.grid(row=3, column=3, sticky="nsew")

    multiply = Button(gui, text=' * ', command=lambda: press("*"), **button_kwargs)
    multiply.grid(row=4, column=3, sticky="nsew")

    divide = Button(gui, text=' / ', command=lambda: press("/"), **button_kwargs)
    divide.grid(row=5, column=3, sticky="nsew")

    equal = Button(gui, text=' = ', command=equalpress, **button_kwargs)
    equal.grid(row=5, column=2, sticky="nsew")

    clear = Button(gui, text='Clear', command=clear, **button_kwargs)
    clear.grid(row=5, column=1, sticky="nsew")

    Decimal = Button(gui, text='.', command=lambda: press('.'), **button_kwargs)
    Decimal.grid(row=6, column=0, sticky="nsew")

    gui.mainloop()
