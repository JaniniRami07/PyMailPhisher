from Modules.UI import *

def pageParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Gmail phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target's name:"))
    pageParser.targetname  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the target email:'))
    pageParser.targetEmail = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the  login city:'))
    pageParser.loginCity   = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
    pageParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the device login browser (EG: Firefox, Chrome, Safari, Opera...): '))
    pageParser.browser = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Date Information"))
    print(style.GREEN('[+]') + style.RESET('Enter the day of te login in numbers (1-31):'))
    pageParser.loginDay = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(r'''
.--------------.---------------.
| [1] Sunday   | [4] Wednesday |
:--------------+---------------:
| [2] Monday   | [5] Thursday  |
:--------------+---------------:
| [3] Tuesday  | [6] Friday    |
:--------------+---------------:
|       [7] Saturday           |
'--------------_---------------' ''')
    print(style.GREEN('[+]') + style.RESET('Enter the number of the day from the table:'))
    pageParser.loginND = str(input(style.CYAN(">>> ") + style.RESET('')))
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday']
    day = int(pageParser.loginND) - 1
    pageParser.loginND = days[day]
    print(style.GREEN('\n[+]') + style.RESET('Enter the year of the login:'))
    pageParser.loginYear = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the time of the login (HH:MMpm/am):'))
    pageParser.loginTime = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the timezone of the login (GMT/UTC/EST...):'))
    pageParser.timezone = str(input(style.CYAN(">>> ") + style.RESET('')))
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
    pageParser.loginMonth = str(input(style.CYAN(">>> ") + style.RESET('')))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = int(pageParser.loginMonth) - 1
    pageParser.loginMonth = months[month]



def pageGenerator_GM():
    pageParser()
    fin = open("Templates/Gmail.html", "rt")
    fout = open("Templates/TempTemplates/GmailTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#NAME', pageParser.targetname).replace('#MONTH', pageParser.loginMonth).replace('#EMAIL', pageParser.targetEmail).replace('#DAY', pageParser.loginDay).replace('#YEAR', pageParser.loginYear).replace('#TIME', pageParser.loginTime).replace('#CITY', pageParser.loginCity).replace('#COUNTRY', pageParser.loginCountry).replace('#URL', pageParser.redirectURL).replace('#ND', pageParser.loginND).replace('#ZONE', pageParser.timezone).replace('#BROWSER', pageParser.browser))
    fin.close()
    fout.close()
