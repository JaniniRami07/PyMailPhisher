import os
import json
from lib.colors import style

# Generate a linkedIn email template
def linkedIn():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for LinkedIn phishing email--'))
    username = str(input(style.GREEN('[+]') + style.RESET(' Displayed username: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    device = str(input(style.GREEN('[+]') + style.RESET(' Login device [Eg: Windows, Iphone...]: ')))
    browser = str(input(style.GREEN('[+]') + style.RESET(' Login browser [Eg: FireFox, Safari...]: ')))
    city = str(input(style.GREEN('[+]') + style.RESET(' Login city: ')))
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
    with open('Templates/LinkedIn.html', 'r') as read_file, \
     open('Templates/Generated_Emails/LinkedInTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#USERNAME', username).replace('#URL', url).replace('#DEVICE', device)
         .replace('#BROWSER', browser).replace('#CITY', city).replace('#COUNTRY', country).replace('#DAY', day)
         .replace('#YEAR', year) .replace('#TIME', time).replace('#ZONE', timezone).replace('#MONTH', month))
