import eel # framework
# import json # pmi storage
import os # get username: windows, unix only
# import setup # local python file


@eel.expose
def username_to_js():
    suffix: str = ""
    if os.getlogin():
        suffix = ", {}".format(os.getlogin())
    return "Welcome{}!".format(suffix)

# initialise 127.0.0.1:8000 for eel
eel.init('web')
eel.start('zoom_id.html', mode='chrome')
