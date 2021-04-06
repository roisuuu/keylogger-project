import helper
import sys

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

    # constant loop until program ends
    # takes in a string and performs the operation
    # [UNUSED DUE TO GUI CALCULATOR]
    # def driver(self):
    #     while True:
    #         q_arr = self.parse_query()
    #         self.result = self.calculate(q_arr)
    #         print(f"{q_arr[0]} {q_arr[1]} {q_arr[2]} = {self.result}")
