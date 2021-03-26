import re
from os.path import exists
from win_webdriver import getConfig
import pyautogui
from tkinter import *


def getScreenSize() -> str:
    width, height = pyautogui.size()
    return str(width)+"x"+str(height)


def saveSettings(data: dict):

    pass


def displayAvailableBrowsers(browsers: list, winroot: Tk):
    Label(winroot, text="Scegli il browser con cui far partire il programma").pack()

    for browser in browsers:
        if exists(browsers[browser]):
            radioState = NORMAL
            icon = "./icon.png"  # getConfig("icons")[browser]

            # Select the default browser
            if browser == getConfig("default"):
                radioState = ACTIVE

            if not exists(getConfig("icons")[browser]):
                icon = "./icon.png"

            # Normalize image path
            icon = re.sub(r"/\\+/", "/", icon)
            image = PhotoImage(icon).zoom(32, 32)

            Radiobutton(
                winroot,
                image=image,
                text=browser.capitalize(),
                textvariable="browser",
                value=browser,
                state=radioState
            ).pack(anchor=W)


winroot = Tk()
winroot.title("Whatsapp robot")
winroot.geometry("800x800")
displayAvailableBrowsers(getConfig("browsers"), winroot)
winroot.mainloop()
