import os
import json
from lib.colors import style

# Generate an twitter email template
def twitter():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Twitter phishing email--'))
    username = str(input(style.GREEN('[+]') + style.RESET(' Displayed username: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    city = str(input(style.GREEN('[+]') + style.RESET(' Login city: ')))
    country = str(input(style.GREEN('[+]') + style.RESET(' Login country: ')))
    browser = str(input(style.GREEN('[+]') + style.RESET(' Login browser [Eg: FireFox, Safari...]: ')))
    device = str(input(style.GREEN('[+]') + style.RESET(' Login device [Eg: Windows, Iphone...]: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Twitter.html', 'r') as read_file, \
     open('Templates/Generated_Emails/TwitterTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#USERNAME', username).replace('#CITY', city).replace('#URL', url)
                              .replace('#COUNTRY' , country).replace('#DEVICE',device ).replace('#BROWSER', browser))
