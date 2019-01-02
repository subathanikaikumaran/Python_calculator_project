from tkinter import *


expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
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


def off():
    btn_0.config(state=DISABLED)
    btn_1.config(state=DISABLED)
    btn_2.config(state=DISABLED)
    btn_3.config(state=DISABLED)
    btn_4.config(state=DISABLED)
    btn_5.config(state=DISABLED)
    btn_6.config(state=DISABLED)
    btn_7.config(state=DISABLED)
    btn_8.config(state=DISABLED)
    btn_9.config(state=DISABLED)
    btn_point.config(state=DISABLED)
    btn_equal.config(state=DISABLED)
    btn_plus.config(state=DISABLED)
    btn_minus.config(state=DISABLED)
    btn_multiply.config(state=DISABLED)
    btn_divide.config(state=DISABLED)


def on():
    btn_0.config(state=NORMAL)
    btn_1.config(state=NORMAL)
    btn_2.config(state=NORMAL)
    btn_3.config(state=NORMAL)
    btn_4.config(state=NORMAL)
    btn_5.config(state=NORMAL)
    btn_6.config(state=NORMAL)
    btn_7.config(state=NORMAL)
    btn_8.config(state=NORMAL)
    btn_9.config(state=NORMAL)
    btn_point.config(state=NORMAL)
    btn_equal.config(state=NORMAL)
    btn_plus.config(state=NORMAL)
    btn_minus.config(state=NORMAL)
    btn_multiply.config(state=NORMAL)
    btn_divide.config(state=NORMAL)


def cls():
    cal.destroy()


if __name__ == "__main__":
    cal = Tk()
    cal.title("Calculator Program")  # GUI window title
    cal.geometry("265x155")  # GUI window size
    equation = StringVar()
    expression_field = Entry(cal, textvariable=equation).grid(columnspan=4, ipadx=70)  # create text box
    equation.set("0")
    # buttons for numbers and operaters
    btn_on = Button(cal, text=' ON ', command=on, fg='white', bg='maroon', height=1, width=7)
    btn_on.grid(row=1, column=0)
    btn_off = Button(cal, text=' OFF ', command=off, fg='white', bg='maroon', height=1, width=7)
    btn_off.grid(row=1, column=1)
    btn_clr = Button(cal, text='Clear', command=clear, fg='white', bg='maroon', height=1, width=7)
    btn_clr.grid(row=1, column=2)
    btn_esc = Button(cal, text=' Exit ', command=lambda: cls(), fg='black', bg='yellow', height=1, width=7)
    btn_esc.grid(row=1, column=3)

    """
    Lambda is a tool for building functions, or more precisely, for building function objects. 
    That means that Python has two tools for building functions: def and lambda.
    """

    btn_7 = Button(cal, text=' 7 ', command=lambda: press(7), fg='white', bg='dark green', height=1, width=7)
    btn_7.grid(row=2, column=0)
    btn_8 = Button(cal, text=' 8 ', command=lambda: press(8),  fg='white', bg='dark green', height=1, width=7)
    btn_8.grid(row=2, column=1)
    btn_9 = Button(cal, text=' 9 ', command=lambda: press(9), fg='white', bg='dark green', height=1, width=7)
    btn_9.grid(row=2, column=2)
    btn_divide = Button(cal, text=' / ', command=lambda: press("/"), fg='black', bg='yellow', height=1, width=7)
    btn_divide.grid(row=2, column=3)

    btn_4 = Button(cal, text=' 4 ', command=lambda: press(4), fg='white', bg='dark green', height=1, width=7)
    btn_4.grid(row=3, column=0)
    btn_5 = Button(cal, text=' 5 ', command=lambda: press(5), fg='white', bg='dark green', height=1, width=7)
    btn_5.grid(row=3, column=1)
    btn_6 = Button(cal, text=' 6 ', command=lambda: press(6), fg='white', bg='dark green', height=1, width=7)
    btn_6.grid(row=3, column=2)
    btn_multiply = Button(cal, text=' * ', command=lambda: press("*"), fg='black', bg='yellow', height=1, width=7)
    btn_multiply.grid(row=3, column=3)

    btn_1 = Button(cal, text=' 1 ', command=lambda: press(1), fg='white', bg='dark green', height=1, width=7)
    btn_1.grid(row=4, column=0)
    btn_2 = Button(cal, text=' 2 ', command=lambda: press(2), fg='white', bg='dark green', height=1, width=7)
    btn_2.grid(row=4, column=1)
    btn_3 = Button(cal, text=' 3 ', command=lambda: press(3), fg='white', bg='dark green', height=1, width=7)
    btn_3.grid(row=4, column=2)
    btn_minus = Button(cal, text=' - ', command=lambda: press("-"), fg='black', bg='yellow', height=1, width=7)
    btn_minus.grid(row=4, column=3)

    btn_0 = Button(cal, text=' 0 ', command=lambda: press(0), fg='white', bg='dark green', height=1, width=7)
    btn_0.grid(row=5, column=0)
    btn_point = Button(cal, text=' . ', command=lambda: press("."), fg='white', bg='dark green', height=1, width=7)
    btn_point.grid(row=5, column=1)
    btn_equal = Button(cal, text=' = ', command=equal_press, fg='white', bg='dark green', height=1, width=7)
    btn_equal.grid(row=5, column=2)
    btn_plus = Button(cal, text=' + ', command=lambda: press("+"), fg='black', bg='yellow',  height=1, width=7)
    btn_plus.grid(row=5, column=3)

    cal.mainloop()  # start the GUI
