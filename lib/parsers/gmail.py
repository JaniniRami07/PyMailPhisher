import os
import json
from lib.colors import style

# Generate a gmail email template
def gmail():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Google Gmail phishing email--'))
    name = str(input(style.GREEN('[+]') + style.RESET(' Displayed name: ')))
    email = str(input(style.GREEN('[+]') + style.RESET(' Displayed email: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    device = str(input(style.GREEN('[+]') + style.RESET(' Login device [Eg: Windows, Iphone...]: ')))
    browser = str(input(style.GREEN('[+]') + style.RESET(' Login browser [Eg: FireFox, Safari...]: ')))
    city = str(input(style.GREEN('[+]') + style.RESET(' Login city: ')))
    country = str(input(style.GREEN('[+]') + style.RESET(' Login country: ')))
    day = str(input(style.GREEN('[+]') + style.RESET(' Login day [In numbers]: ')))
    day_name = str(input(style.GREEN('[+]') + style.RESET(' Login day of the week: ')))
    year = str(input(style.GREEN('[+]') + style.RESET(' Login year: ')))
    time = str(input(style.GREEN('[+]') + style.RESET(' Login time [HH:MMpm/am]: ')))
    timezone = str(input(style.GREEN('[+]') + style.RESET(' Login timezone [Eg: GMT, ETC...]: ')))
    month = str(input(style.GREEN('[+]') + style.RESET(' Login month [eg: June]: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Gmail.html', 'r') as read_file, \
     open('Templates/Generated_Emails/GmailTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#NAME', name).replace('#EMAIL', email).replace('#URL', url).replace('#MONTH', month)
         .replace('#DEVICE', device).replace('#BROWSER', browser).replace('#CITY', city).replace('#COUNTRY', country)
         .replace('#DAY', day).replace('#YEAR', year).replace('#TIME', time).replace('#ZONE', timezone).replace('#ND', day_name))
