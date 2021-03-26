import os
import json
from subprocess import *

# Verify that the script is running on windows
if "nt" not in os.name:
    exit()


def getConfig(configName: str):
    config = open("config.json", "r").read()
    config = json.loads(config)
    if configName in config:
        return config[configName]
    else:
        return None


def openBrowser(selectedBrowser: str = getConfig("default")):
    if selectedBrowser == "":
        selectedBrowser = "firefox"

    # Open the browser
    browser = Popen(
        [
            getConfig("browsers")[selectedBrowser],
            "web.whatsapp.com/"
        ],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE
    )

    browserError = browser.returncode
