import os
import json
from lib.colors import style

# Generate a facebook email template
def facebook():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Facebook phishing email--'))
    name = str(input(style.GREEN('[+]') + style.RESET(' Displayed name: ')))
    email = str(input(style.GREEN('[+]') + style.RESET(' Displayed email: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    city = str(input(style.GREEN('[+]') + style.RESET(' Login city: ')))
    country = str(input(style.GREEN('[+]') + style.RESET(' Login country: ')))
    day = str(input(style.GREEN('[+]') + style.RESET(' Login day [in numbers]: ')))
    year = str(input(style.GREEN('[+]') + style.RESET(' Login year: ')))
    time = str(input(style.GREEN('[+]') + style.RESET(' Login time [HH:MM pm/am]: ')))
    month = str(input(style.GREEN('[+]') + style.RESET(' Login month [eg: June]: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Facebook.html', 'r') as read_file, \
     open('Templates/Generated_Emails/FacebookTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#NAME', name).replace('#CITY', city).replace('#URL', url).replace('#EMAIL', email).replace('#COUNTRY' , country)
                              .replace('#DAY', day).replace('#YEAR', year).replace('#TIME', time).replace('#MONTH', month))
