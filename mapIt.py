# Web Scraper project
# Gets a street address from command line arguments or clipboard, then opens
# google maps page for that address

# shebang line actually necessary?

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])

else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
