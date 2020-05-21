from Modules.UI import *
from Modules.pageGen import generatePages_
from Modules.mailGen import Mailer_
def mainFunction():
    while True:
        clear()
        banner()
        menuBanner()
        menuCH = str(input(style.RESET('\nPyMailPhisher') + style.GREEN(' >>> ') + style.RESET('')))
        if menuCH == "1":
            generatePages_()
        elif menuCH == "2":
            Mailer_()
        elif menuCH == "3":
            info()
        elif menuCH == "4":
            clear()
            banner()
            break

if __name__ == "__main__":
    mainFunction()
