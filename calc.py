import tkinter as tk
import txt_based_calc as txtc

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # initialise Calculator class from txt_based_calc.py
        calc = txtc.Calculator()

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        operator=""
        text_input = tk.StringVar()

        txtDisplay = tk.Entry(calc, font=('arial',20,'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

    def btn_click(self, item):
        global query
        query += str(item)
        


if __name__ == "__main__":
    calc = tk.Tk()
    MainApplication(calc).grid()
    calc.title("Calculator")
    calc.mainloop()