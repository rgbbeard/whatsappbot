from functools import partial
from os.path import exists
from win_webdriver import *
import pyautogui
from tkinter import *


def getScreenSize() -> str:
    width, height = pyautogui.size()
    return str(width)+"x"+str(height)


def saveSettings():
    pass


def openAction(browser: str = "", col: int = 0):
    saveSettings()
    print(col)
    # openBrowser(browser)


def minimizeWindow(winroot: Tk):
    winroot.wm_state("iconic")


def closeWindow(winroot: Tk):
    winroot.destroy()


def displayActionsBar(winroot: Tk):
    # Minimize window button
    min = Button(
        winroot,
        width="4",
        text="-",
        bg="#f90",
        fg="#fff",
        justify="center",
        relief="flat",
        command=partial(minimizeWindow, winroot)
    )
    min.grid(row=0, column=0, padx=5, sticky="w")

    # Close window button
    cls = Button(
        winroot,
        width="4",
        text="x",
        bg="#d00",
        fg="#fff",
        justify="center",
        relief="flat",
        command=partial(closeWindow, winroot)
    )
    cls.grid(row=0, column=0, padx=5)


def displayAvailableBrowsers(browsers: list, winroot: Tk):
    Label(
        winroot, text="Scegli il browser con cui far partire il programma",
        font="20"
    ).grid(row=1)

    col = 0

    for browser in browsers:
        if exists(browsers[browser]):
            browserName = browser
            text = browser.capitalize()
            buttonState = "#0cc"
            buttonStateColor = "#fff"

            # Select the default browser
            if browser in getConfig("default"):
                buttonState = "#cc0"
                buttonStateColor = "#fff"

            Button(
                winroot,
                width="10",
                height="2",
                text=text,
                justify="center",
                bg=buttonState,
                fg=buttonStateColor,
                font="10",
                activebackground="#05e",
                relief="flat",
                command=partial(openAction, browserName, col)
            ).grid(row=2, column=col, padx=5)

            col += 1


winroot = Tk()
winroot.wm_attributes('-fullscreen', 'true')

displayActionsBar(winroot)
displayAvailableBrowsers(getConfig("browsers"), winroot)

winroot.mainloop()
