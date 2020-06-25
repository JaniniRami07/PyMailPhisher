import os
import json
from lib.colors import style

# Generate a snapchat email template
def snapchat():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Snapchat phishing email--'))
    username = str(input(style.GREEN('[+]') + style.RESET(' Displayed username: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    device = str(input(style.GREEN('[+]') + style.RESET(' Login device [Eg: Windows, Iphone...]: ')))
    ip =  str(input(style.GREEN('[+]') + style.RESET(' Login device IP [Eg: 162.243.110.124]: ')))
    country = str(input(style.GREEN('[+]') + style.RESET(' Login country: ')))
    day = str(input(style.GREEN('[+]') + style.RESET(' Login day [in numbers]: ')))
    year = str(input(style.GREEN('[+]') + style.RESET(' Login year: ')))
    time = str(input(style.GREEN('[+]') + style.RESET(' Login time [HH:MM]: ')))
    timezone = str(input(style.GREEN('[+]') + style.RESET(' Login timezone [Eg: GMT, ETC...]: ')))
    month = str(input(style.GREEN('[+]') + style.RESET(' Login month [eg: June]: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Snapchat.html', 'r') as read_file, \
     open('Templates/Generated_Emails/SnapchatTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#USERNAME', username).replace('#URL', url).replace('#DEVICE', device)
         .replace('#IP', ip).replace('#COUNTRY', country).replace('#DAY', day).replace('#YEAR', year)
         .replace('#TIME', time).replace('#ZONE', timezone).replace('#MONTH', month))
