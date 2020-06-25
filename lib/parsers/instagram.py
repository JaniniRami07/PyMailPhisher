import os
import json
from lib.colors import style

# Generate an instagram email template
def instagram():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for Instagram phishing email--'))
    name = str(input(style.GREEN('[+]') + style.RESET(' Displayed name: ')))
    username = str(input(style.GREEN('[+]') + style.RESET(' Displayed username: ')))
    email = str(input(style.GREEN('[+]') + style.RESET(' Displayed email: ')))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/Instagram.html', 'r') as read_file, \
     open('Templates/Generated_Emails/InstagramTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#NAME', name).replace('#USERNAME', username).replace('#EMAIL', email).replace('#URL', url))
