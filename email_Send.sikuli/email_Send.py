from sikuli import *
import logging

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#---------------------------------------------------#
def fSend_Text(mailSubject):
#---------------------------------------------------#

    fromEmail = 'tom.sikuli@gmail.com'
    fromPW = '!tomsikuli!'
    toEmail = '9788843701@messaging.sprintpcs.com'
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = mailSubject
    message = mailSubject
    
    msg.attach(MIMEText(message))   
    
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    
    # secure our email with tls encryption
    mailserver.starttls()
    
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(fromEmail, fromPW)
    
    mailserver.sendmail(fromEmail,toEmail,msg.as_string())
    
    mailserver.quit()

#---------------------------------------------------#
def fSend_Email(mailSubject):
#---------------------------------------------------#

    fromEmail = 'tom.sikuli@gmail.com'
    fromPW = '!tomsikuli!'
    toEmail = 'thinds66@gmail.com'
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    
    file1 = Settings.myLogFile
    file2 = Settings.reportLogFile

    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = mailSubject
    message = 'here is the email'
    
    msg.attach(MIMEText(message))
    
    attachFile = MIMEText(file(file1).read())
    attachFile.add_header('Content-Disposition', 'attachment', filename='main.log')
    msg.attach(attachFile)

    attachFile = MIMEText(file(file2).read())
    attachFile.add_header('Content-Disposition', 'attachment', filename='report.log')
    msg.attach(attachFile)
    
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    
    # secure our email with tls encryption
    mailserver.starttls()
    
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(fromEmail, fromPW)
    
    mailserver.sendmail(fromEmail,toEmail,msg.as_string())
    
    mailserver.quit()