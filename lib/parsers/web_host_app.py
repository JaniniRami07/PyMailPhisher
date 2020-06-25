import os
import json
from lib.colors import style

# Generate a 000WebHostApp email template
def web_host_app():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))   # Clear the terminal
    print(style.YELLOW('--Fill the folowing credentials for 000WebHostApp phishing email--'))
    url = str(input(style.GREEN('[+]') + style.RESET(' Phishing URL: ')))

    if not url.startswith('http://') or not url.startswith('http://'):
        url = f"http://{url}"
    else:
        None
    with open('Templates/000WebHost.html', 'r') as read_file, \
     open('Templates/Generated_Emails/000WebHostTemplate.html', 'w') as write_file:
     for line in read_file:
         write_file.write(line.replace('#URL', url))
