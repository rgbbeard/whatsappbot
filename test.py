from win_gui_class import *

w = Window(windowSize=WINDOW_FULLSCREEN)
obj = w.window

label = tkinter.Label(
    obj,
    text="Lorem ipsum"
)
render(label)

w.init()
