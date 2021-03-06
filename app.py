import eel
# import json
import tkinter
import os


@eel.expose
def username_to_js():
    if os.getlogin != "null" and os.getlogin():
        return "Welcome, {}!".format(os.getlogin())


# initialise 127.0.0.1:8000 for eel
eel.init('web')
eel.start('zoom_id.html', mode='chrome')
