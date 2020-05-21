from Modules.UI import *

def pageParser():
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Facebook phishing page--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target name that will be displayed on the email:"))
    pageParser.targetName  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the target email:'))
    pageParser.targetEmail = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the  login city:'))
    pageParser.loginCity   = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
    pageParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Date Information"))
    print(style.GREEN('[+]') + style.RESET('Enter the day of te login in numbers:'))
    pageParser.loginDay = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the year of the login:'))
    pageParser.loginYear = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the time of the login (HH:MM pm/am):'))
    pageParser.loginTime = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(r'''
.--------------.---------------.
| [1] January  | [7] July      |
:--------------+---------------:
| [2] February | [8] August    |
:--------------+---------------:
| [3] March    | [9] September |
:--------------+---------------:
| [4] April    | [10] October  |
:--------------+---------------:
| [5] May      | [11] November |
:--------------+---------------:
| [6] June     | [12] December |
'--------------'---------------' ''')
    print(style.GREEN('[+]') + style.RESET('Enter the login month in numbers:'))
    pageParser.loginMonth = str(input(style.GREEN('>>> ') + style.RESET('')))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = int(pageParser.loginMonth) - 1
    pageParser.loginMonth = months[month]




def pageGenerator_FB():
    pageParser()
    fin = open("Templates/Facebook.html", "rt")
    fout = open("Templates/TempTemplates/FacebookTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#NAME', pageParser.targetName).replace('#MONTH', pageParser.loginMonth).replace('#DAY', pageParser.loginDay).replace('#YEAR', pageParser.loginYear).replace('#TIME', pageParser.loginTime).replace('#CITY', pageParser.loginCity).replace('#COUNTRY', pageParser.loginCountry).replace('#EMAIL', pageParser.targetEmail).replace('#URL', pageParser.redirectURL))
    fin.close()
    fout.close()
