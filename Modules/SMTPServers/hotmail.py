import time
import codecs
import smtplib
import getpass
from multiprocessing import Process

from Modules.UI import *
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def hotmailServer():
    clear()
    banner()
    print(style.GREEN('[+]') + style.RESET('-- SMTP Hotmail Configuration --'))
    sender = str(input(style.GREEN('[+]') + style.RESET(' Enter the sender email: ')))
    password = getpass.getpass(style.GREEN('[+]') + style.RESET(" Enter the sender's email password: "))
    receiver = str(input(style.GREEN('[+]') + style.RESET(' Enter the receiver email: ')))
    subject = str(input(style.GREEN('[+]') + style.RESET(' Enter the email subject: ')))
    print('''
    .------------------------.-------------------------.
    | [1] Facebook Template  | [5]  LinkedInTemplate   |
    :------------------------+-------------------------:
    | [2] Instagram Template | [6] Gmail Template      |
    :------------------------+-------------------------:
    | [3] Twitter Template   | [7] Discord Template    |
    :------------------------+-------------------------:
    | [4] Snapchat Template  | [8] 000WebHost Template |
    '--------------------------------------------------'
        ''')
    pages = ['Facebook', 'Instagram', 'Twitter', 'Snapchat', 'LinkedIn', 'Gmail', 'Discord', '000WebHost']
    template = str(input(style.GREEN('[+]') + style.RESET(' Enter the email number of the email template from the table: ')))
    template = int(template) - 1
    template = pages[template]
    file = 'Templates/TempTemplates/{}Template.html'.format(template.title())
    if path.exists(file):
        print('')
    else:
        print(style.RED('[!]') + style.RESET(' Email template does not exist, generate one first!'))

    print(style.GREEN('[+]') + style.RESET(' Sending email to {} ...').format('receiver'))

    msg  = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    file = 'Templates/TempTemplates/{}Template.html'.format(template.title())
    Rtemplate_ = open(file)
    body = MIMEText(Rtemplate_.read(), 'html')
    msg.attach(body)

    mail = smtplib.SMTP('smtp.live.com', 465)
    mail.ehlo()
    mail.starttls()

    mail.login(sender, password)
    mail.sendmail(sender, receiver, msg.as_string())
    mail.quit()
    print(style.GREEN('[+]') + style.RESET(" The phishing email has been sent successfully!"))
