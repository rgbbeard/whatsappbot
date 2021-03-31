from functools import partial
from os.path import exists
from tkinter import StringVar
from win_webdriver import *
from win_gui_class import *
from win_system import *


def openAction(browser: str = ""):
    openBrowser(browser)


w = Window(
    windowName="Whatsapp Robot",
    windowPosition=WINDOW_CENTERED
)

obj = w.window

Separator(obj, side="top")

jsonData: dict = {}


def getData(var):
    jsonData[len(jsonData)] = var.get()
    print(jsonData)
    print(type(jsonData))


tkinter.Button(
    obj,
    text="Salva impostazioni",
    justify="center",
    relief="flat",
    # command=partial(getData)
).pack(pady=5, padx=4)

w.init()
