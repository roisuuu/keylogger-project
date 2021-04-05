from tkinter import *

calc = Tk()
calc.title("Calculator")
operator=""
text_input = StringVar()

txtDisplay = Entry(calc, font=('arial',20,'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

calc.mainloop()
