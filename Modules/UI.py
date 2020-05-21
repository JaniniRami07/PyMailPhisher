import os
import sys

class style():
    BLACK = lambda x: '\033[30m' + str(x)
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)
    UNDERLINE = lambda x: '\033[4m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print('''
─▀▀▌───────▐▀▀
─▄▀░◌░░░░░░░▀▄	 PyMailPhisher v.1.0
▐░░◌░▄▀██▄█░░░▌	    Author:Proxy07
▐░░░▀████▀▄░░░▌
═▀▄▄▄▄▄▄▄▄▄▄▄▀

    ''')


def pagesList():
    print('''
    .------------------------.-------------------------.
    | [1] Facebook Template  | [5] LinkedIn Template   |
    :------------------------+-------------------------:
    | [2] Instagram Template | [6] Gmail Template      |
    :------------------------+-------------------------:
    | [3] Twitter Template   | [7] Discord Template    |
    :------------------------+-------------------------:
    | [4] Snapchat Template  | [8] 000WebHost Template |
    :------------------------+-------------------------:
    |             [9] Back to main menu.               |
    '--------------------------------------------------'
        ''')

def menuBanner():
    clear()
    banner()
    print(style.RESET("-- PyMailPhisher Main Menu --"))
    print(style.GREEN('\n[1]') + style.RESET(' Generate a phishing page.'))
    print(style.GREEN('[2]') + style.RESET(' Send a phishing email.'))
    print(style.GREEN('[3]') + style.RESET(' About PyMailPhisher'))
    print(style.GREEN('[4]') + style.RESET(' Exit PyMailPhisher'))


def smtpList():
    print(style.RESET("-- SMTP Servers --"))
    print(style.GREEN('\n[1]') + style.RESET(' Gmail'))
    print(style.GREEN('[2]') + style.RESET(' Outlook'))
    print(style.GREEN('[3]') + style.RESET(' Yahoo'))
    print(style.GREEN('[4]') + style.RESET(' Hotmail\n'))


def info():
    clear()
    banner()
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
    input(style.YELLOW('\n[*]') + style.RESET(' Press anything to return back to main menu.'))
