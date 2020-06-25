import json
import sys
import os
import time
import smtplib
import getpass
from lib.colors import style
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sending email
def send_mail(name, smtp_server, port):
    print(style.GREEN('[+]') + style.RESET(f'-- SMTP {name} Configuration --'))
    sender = str(input(style.GREEN('\n[+]') + style.RESET(' Sender email: ')))
    password = getpass.getpass(style.GREEN('[+]') + style.RESET(" Sender email password: "))
    receiver = str(input(style.GREEN('[+]') + style.RESET(' Receiver email: ')))
    subject = str(input(style.GREEN('[+]') + style.RESET(' Email subject: ')))

    files = os.listdir('Templates/Generated_Emails')
    print(style.GREEN(style.RESET('\nGenerated Files:')))
    for file in files:
        print(style.RESET(f'- {file}'))
    template = str(input(style.GREEN('\n[+]') + style.RESET('Generated file name [Eg: FacebookTemplate.html]: ')))
    template_path = f'Templates/Generated_Emails/{template}'
    if not os.path.exists(template_path):
        print(style.RED('\n[!]') + style.RESET(' File does not exist, exiting...'))
        sys.exit()
    else:
        None
    print(style.GREEN('\n[+]') + style.RESET(f' Sending email to {receiver} ...'))

    # sending the email with mime
    msg  = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    read_template = open(template_path)
    body = MIMEText(read_template.read(), 'html')
    msg.attach(body)
    mail = smtplib.SMTP(smtp_server, port)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, password)
    mail.sendmail(sender, receiver, msg.as_string())
    mail.quit()
    print(style.GREEN('[+]') + style.RESET(" The phishing email has been sent successfully!"))


# Choosing the smtp server
def mailer():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
    print(style.RESET("        -- Choose a SMTP server --\n"))
    print(style.GREEN('\n[1]') + style.RESET(' Gmail'))
    print(style.GREEN('[2]') + style.RESET(' Outlook'))
    print(style.GREEN('[3]') + style.RESET(' Yahoo'))
    print(style.GREEN('[4]') + style.RESET(' Hotmail'))
    try:
        smtp_server= int(input(style.YELLOW('\n[+]') + style.RESET(' Enter mode ID: ')))
    except:
        print(style.RED('\n[!]') + style.RESET(' Wrong input, exiting...'))
        sys.exit()

    gmail_config =   ['Gmail', 'smtp.gmail.com', 587]
    outlook_config = ['Outlook', 'smtp-mail.outlook.com', 587]
    hotmail_config = ['Hotmail', 'smtp.live.com', 465]
    yahoo_config = ['Yahoo', 'smtp.mail.yahoo.com', 456]

    print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
    if smtp_server == 1:
        name = gmail_config[0]
        smtp_server = gmail_config[1]
        port = gmail_config[2]
        send_mail(name, smtp_server, port)
