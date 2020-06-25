import os
import json
from lib.colors import style

# Generate a discord email template
def discord():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Discord phishing email--'))
    username = str(input(style.GREEN('[+]') + style.RESET(' Displayed username: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))
    country = str(input(style.GREEN('[+]') + style.RESET(' Login country: ')))
    city = str(input(style.GREEN('[+]') + style.RESET(' Login city: ')))
    ip =  str(input(style.GREEN('[+]') + style.RESET(' Login device IP [Eg: 162.243.110.124]: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Discord.html', 'r') as read_file, \
     open('Templates/Generated_Emails/DiscordTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#USERNAME', username).replace('#URL', url).replace('#COUNTRY', country)
         .replace('#CITY', city).replace('#IP', ip))
