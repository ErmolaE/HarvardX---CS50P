import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    f = choice(figlet.getFonts())
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in figlet.getFonts():
            f = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

s = input()
figlet.setFont(font=f)
print(figlet.renderText(s))