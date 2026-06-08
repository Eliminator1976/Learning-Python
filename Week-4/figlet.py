from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()



if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
        else:
            sys.exit("Font not Found")
    else:
        sys.exit("flag error")

    
elif len(sys.argv) == 1:
    s = input("Input: ")
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print("Output:\n"+figlet.renderText(s))

else:
    sys.exit("invalid usage")
    
        
        

