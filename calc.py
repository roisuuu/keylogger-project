import tkinter as tk
import txt_based_calc as txtc

WINDOW_WIDTH = 362
WINDOW_HEIGHT = 500

query = ""
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # initialise Calculator class from txt_based_calc.py
        self.calc = txtc.Calculator()

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        input_frame = tk.Frame(self, width = 312, height = 50, bd = 20, highlightbackground="black", highlightcolor="black")
        input_frame.pack(side=tk.TOP)

        self.text_input = tk.StringVar()
        txtDisplay = tk.Entry(input_frame, font = ('arial',20,'bold'), textvariable = self.text_input, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')
        txtDisplay.grid(row = 0, column = 0)
        txtDisplay.pack(ipady = 10)

        # Creating the buttons
        btn_frame = tk.Frame(self, width = 312, height = 350, bg = "grey")
        btn_frame.pack()

        # First row
        clr_btn = tk.Button(btn_frame, text = "CLR", fg = "black", width = 32, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = self.clear_btn).grid(row = 0)
        # relief = solid for equals button?
        div_btn = tk.Button(btn_frame, text = "/", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("/")).grid(row = 0, column = 1)

    def btn_click(self, item):
        global query
        print(query)
        query += str(item)
        self.text_input.set(query)
    
    def clear_btn(self):
        global query
        query = ""
        self.text_input.set("")
        
    def calculate_btn(self):
        global query

        result = self.calc.calculate(query)
        # display result on main calculator screen
        self.text_input.set(result)
        # reset query
        query = ""
        
if __name__ == "__main__":
    calc = tk.Tk()
    calc.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    # unable to resize window hehe xD
    calc.resizable(0, 0)
    calc.title("Calculator")

    MainApplication(calc).grid()
    calc.mainloop()