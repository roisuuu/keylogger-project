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
        self.result = 0
        # using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 to generate the ASCII art
        print(r"""
 __    __      _  __                         ___      _        
/ / /\ \ \___ | |/ _|_ __ __ _ _ __ ___     / __\ ___| |_ __ _ 
\ \/  \/ / _ \| | |_| '__/ _` | '_ ` _ \   /__\/// _ \ __/ _` |
 \  /\  / (_) | |  _| | | (_| | | | | | | / \/  \  __/ || (_| |
  \/  \/ \___/|_|_| |_|  \__,_|_| |_| |_| \_____/\___|\__\__,_|
                                                               
        """)

        print(CALC_INSTRUCTION)
        print(EXAMPLE_QUERY)

    # checks if query is valid, then passes query onto another function
    def parse_query(self):
        while True:
            q = input("Enter query: ")

            if q == 'quit':
                print("Bye...")
                sys.exit()

            query_arr = q.split()
            if len(query_arr) != 3:
                print(CALC_INSTRUCTION)
            elif not helper.is_num(query_arr[0]) or not helper.is_num(query_arr[2]):
                print(INPUT_ERROR)
            elif not query_arr[1] in VALID_OPERATIONS:
                print(OPERATION_ERROR, end=" ")
                print(VALID_OPERATIONS)
            else:
                break
        
        return query_arr

    def calculate(self, q_arr):
        x = helper.num(q_arr[0])
        y = helper.num(q_arr[2])
        op = q_arr[1]

        if op == '+':
            return helper.add(x, y)
        elif op == '-':
            return helper.subtract(x, y)
        elif op == '/':
            return helper.divide(x, y)
        elif op == '*':
            return helper.multiply(x, y)
        elif op == '%':
            return helper.mod(x, y)
        elif op == '^':
            return helper.exp(x, y)

    # constant loop until program ends
    # takes in a string and performs the operation
    def driver(self):
        while True:
            q_arr = self.parse_query()
            self.result = self.calculate(q_arr)
            print(f"{q_arr[0]} {q_arr[1]} {q_arr[2]} = {self.result}")
