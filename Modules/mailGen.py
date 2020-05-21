from Modules.UI import *
from Modules.SMTPServers.gmail import gmailServer
from Modules.SMTPServers.outlook import outlookServer
from Modules.SMTPServers.yahoo import yahooServer
from Modules.SMTPServers.hotmail import hotmailServer

def Mailer_():
    while True:
        clear()
        banner()
        smtpList()
        chooseServer = str(input(style.RESET('PyMailPhisher') + style.GREEN(' >>> ') + style.RESET('')))
        servers = [gmailServer, outlookServer, yahooServer, hotmailServer]
        server = int(chooseServer) - 1
        servers[server]()
        clear()
        banner()
        print(style.GREEN('[+]') + style.RESET('The email has been sent successfully!'))
        input(style.YELLOW('[*]') + style.RESET('Press anything to continue.'))
        break
