import tkinter as tk

import sys

WINDOW_WIDTH = 362
WINDOW_HEIGHT = 500

query = ""
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # initialise Calculator class from txt_based_calc.py
        self.calc = Calculator()

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        input_frame = tk.Frame(self, width = 312, height = 50, bd = 20, highlightbackground="black", highlightcolor="black")
        input_frame.pack(side=tk.TOP)

        self.text_input = tk.StringVar()
        # callback allows user to type equation directly into textbox
        self.text_input.trace_add("write", self.callback)
        txtDisplay = tk.Entry(input_frame, font = ('arial',20,'bold'), textvariable = self.text_input, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')
        txtDisplay.grid(row = 0, column = 0)
        txtDisplay.pack(ipady = 10)

        # Creating the buttons
        btn_frame = tk.Frame(self, width = 312, height = 350, bg = "grey")
        btn_frame.pack()

        # First row
        clr_btn = tk.Button(btn_frame, text = "CLR", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = self.clear_btn).grid(row = 0)
        del_btn = tk.Button(btn_frame, text = "DEL", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = self.del_btn).grid(row = 0, column = 1)
        quit_btn = tk.Button(btn_frame, text = "OFF", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = self.quit_btn).grid(row = 0, column = 2)
        div_btn = tk.Button(btn_frame, text = "/", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("/")).grid(row = 0, column = 3)

        # Second row
        btn_7 = tk.Button(btn_frame, text = "7", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("7")).grid(row = 1, column = 0)
        btn_8 = tk.Button(btn_frame, text = "8", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("8")).grid(row = 1, column = 1)
        btn_9 = tk.Button(btn_frame, text = "9", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("9")).grid(row = 1, column = 2)
        mul_btn = tk.Button(btn_frame, text = "x", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("*")).grid(row = 1, column = 3)

        # Third row
        btn_4 = tk.Button(btn_frame, text = "4", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("4")).grid(row = 2)
        btn_5 = tk.Button(btn_frame, text = "5", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("5")).grid(row = 2, column = 1)
        btn_6 = tk.Button(btn_frame, text = "6", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("6")).grid(row = 2, column = 2)
        sub_btn = tk.Button(btn_frame, text = "-", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("-")).grid(row = 2, column = 3)

        # Fourth row
        btn_1 = tk.Button(btn_frame, text = "1", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("1")).grid(row = 3)
        btn_2 = tk.Button(btn_frame, text = "2", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("2")).grid(row = 3, column = 1)
        btn_3 = tk.Button(btn_frame, text = "3", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("3")).grid(row = 3, column = 2)
        add_btn = tk.Button(btn_frame, text = "+", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("+")).grid(row = 3, column = 3)

        # Fifth row
        btn_0 = tk.Button(btn_frame, text = "0", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click("0")).grid(row = 4)
        btn_dec = tk.Button(btn_frame, text = ".", fg = "black", width = 10, height = 3, bd = 2, relief = "ridge", bg = "#eee", cursor = "hand2", command = lambda: self.btn_click(".")).grid(row = 4, column = 1)
        equals_btn = tk.Button(btn_frame, text = "=", fg = "black", width = 22, height = 3, bd = 2, relief = "solid", bg = "#eee", cursor = "hand2", command = lambda: self.calculate_btn()).grid(row = 4, column = 2, columnspan = 2)

    # allows user to bypass buttons and just type equation
    # into text box
    def callback(self, var, index, mode):
        global query
        query = self.text_input.get()

    def btn_click(self, item):
        global query
        query += str(item)
        self.text_input.set(query)
    
    def clear_btn(self):
        global query
        query = ""
        self.text_input.set("")
    
    def del_btn(self):
        global query
        if len(query) > 0:
            query = query[:-1]
            self.text_input.set(query)
    
    def quit_btn(self):
        sys.exit()
        
    def calculate_btn(self):
        global query

        if len(query) > 0:
            result = self.calc.calculate(query)
            # display result on main calculator screen
            self.text_input.set(result)
            # reset query
            query = result

# initiates the window - can replace function definition with:
# if __name__ == "__main__":
# If you just want to test the GUI out without getting keylogged         
def calc_init():
    calc = tk.Tk()
    calc.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    # unable to resize window hehe xD
    calc.resizable(0, 0)
    calc.title("Wolfram Beta")

    MainApplication(calc).grid()
    calc.mainloop()

CALC_INSTRUCTION = "Enter your calculations in the following format: [term] [operator] [term]\nType 'quit' to exit"
EXAMPLE_QUERY = "e.g. 1 + 2"
INPUT_ERROR = "Check if all your terms are numbers!"
OPERATION_ERROR = "Make sure your operator is one of the following: "
VALID_OPERATIONS = ['+', '-', '*', '/', '^', '%']

# TODO: consider allowing brackets o_o
class Calculator:
    def __init__(self):
        # self.result = 0
        # using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 to generate the ASCII art
        print(r"""
 __    __      _  __                         ___      _        
/ / /\ \ \___ | |/ _|_ __ __ _ _ __ ___     / __\ ___| |_ __ _ 
\ \/  \/ / _ \| | |_| '__/ _` | '_ ` _ \   /__\/// _ \ __/ _` |
 \  /\  / (_) | |  _| | | (_| | | | | | | / \/  \  __/ || (_| |
  \/  \/ \___/|_|_| |_|  \__,_|_| |_| |_| \_____/\___|\__\__,_|
                                                               
        """)

#         print(CALC_INSTRUCTION)
#         print(EXAMPLE_QUERY)
        #print("hi...")

    def calculate(self, q):
        # using python inbuilt eval function to evaluate the query
        result = str(eval(q))
        return result