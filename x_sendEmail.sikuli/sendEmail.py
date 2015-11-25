from sikuli import *
import logging
import csv
import myTools

# example take from here --> https://docs.python.org/2/library/email-examples.html

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Send_Email():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # Open a plain text file for reading.
    fp = open(Settings.myLogFile, 'rb')
    # Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Log File'
    msg['From'] = "thinds66@gmail.com"
    msg['To'] = "thinds66@yahoo.com"
    
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.gmail.com')
    s.sendmail(me, [you], msg.as_string())
    s.quit()
