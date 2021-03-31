import os
import webbrowser
from win_system import getConfig

# Verify that the script is running on windows
if "nt" not in os.name:
    exit()


def openBrowser(selectedBrowser: str = getConfig("default")):
    if selectedBrowser == "":
        selectedBrowser = "edge"

    # Open the browser
    path = str(getConfig("browsers")[selectedBrowser]).replace("\\", "/")

    browser = webbrowser.get(path+" %s")
    browser.open("web.whatsapp.com")
    return browser
