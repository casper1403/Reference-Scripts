import smtplib
import time

""" Script for sending an email"""


FROM = ""         # Mail sender
TO = ""           # Mail receiver
SERVER = "smtp-mail.outlook.com"       # SMTP Server
MAIL_LOGIN = ""
MAIL_PW = ""

def sendMail(SUBJECT,TEXT):
    message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
    server = smtplib.SMTP(SERVER)
    server.starttls()
    server.login(MAIL_LOGIN, MAIL_PW)
    server.sendmail(FROM, TO, message)
    server.quit()
