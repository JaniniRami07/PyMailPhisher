import sys
import os
from lib.colors import style        # Coloring package
from lib.email_generator import generate_email
from lib.mailer import mailer


# Info banner
def info():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
    print(r'''
                      PyMailPhisher
----------------------------------------------------------
Version: 1.0.0
Author : Pr0xy07
Author's Email: proxy07@tutanota.com
Date Published: 20/5/2020''')

    print(style.GREEN('''\n◇ Info: ''') + style.RESET('''
PyMailPhisher is one of a few email phishers out there it
works by generating a phishing html page that then will be
sent as an email to your victim hoping they fall for it!''' ))


    print(style.GREEN('''\n◇ Bugs and Help: ''') + style.RESET('''
If you find any bugs, issues in PyMailPhisher feel free to
raise an issue on the GitHub repository of this tool so
me and the community can help.''' ))

    print(style.GREEN('''\n◇ Contributions and Ideas: ''') + style.RESET('''
Feel free to contact if you are interested in helping me
improve this tool.''' ))

    print(style.RED('''\n◇ Warning: ''') + style.RESET('''
You should only use this app for legal penetration testing
or educational purposes only as I am not responsible for any
damage caused by PyMailPhisher.''' ))


# Main PyMailPhisher fucntion
def main_function():
    print(os.path.isfile('Templates/Generated_Emails'))
    if os.path.isdir('Templates/Generated_Emails') == False:
        os.mkdir('Templates/Generated_Emails')
    else:
        None

    #print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
    print(style.RESET("-- PyMailPhisher Main Menu --"))
    print(style.GREEN('\n[1]') + style.RESET(' Generate a phishing page.'))
    print(style.GREEN('[2]') + style.RESET(' Send a phishing email.'))
    print(style.GREEN('[3]') + style.RESET(' About PyMailPhisher'))
    print(style.GREEN('[4]') + style.RESET(' Exit PyMailPhisher'))
    try:
        mode_option = int(input(style.YELLOW('\n[+]') + style.RESET(' Enter mode ID: ')))
    except:
        print(style.RED('\n[!]') + style.RESET(' Wrong input, exiting...'))
        sys.exit()

    if mode_option == 1:
        # Generate email templates
        generate_email()
    elif mode_option == 2:
        # Send mail
        mailer()
    elif mode_option == 3:
        # Info
        info()
    elif mode_option == 4:
        #exit
        sys.exit()


if __name__ == "__main__":
    main_function()
