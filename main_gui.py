# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://www.guru99.com/python-dictionary-append.html#6
# https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-geometry-managers/
# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
# def want .place(relx=X%, rely=Y%)
# probably want to define panes within the window. idk how.
# pack can work withing a frame, and within a... widget

#within the frame, I want a grid (?) using *rowconfigure* 
import tkinter as tk
import widget_classes as widget_classes
#import keybind_helper as keybind_helper

def cmd_sfg(sfg, key="c"):
    print("Button pressed...")


def key_downdict(event):
    # switch event.keypress_name, case d... 1
    print(event)
    view.buttons["do"].configure(bg='blue')

def key_updict(event):
    print(event)
    view.buttons["do"].configure(bg=view.main_sfg_bg)

# How do I explicitely pass 'view' into this?
# I think that's all I need now...
# Also need to switch/ case on key_down
def key_down(event):
    # switch event.keypress_name, case d... 1
    print(event)
    view.buttons[3].configure(bg='blue')

def key_up(event):
    print(event)
    view.buttons[3].configure(bg=view.main_sfg_bg)

def close_win(e):
    print("exiting window...")
    window.destroy()

window = tk.Tk()
window.geometry("700x400")
window.bind('q', lambda e: close_win(e))

# might want to edit sfgFrame to have it's own explicit self.tkFrame object... not sure how we can do sfgFrame.pack() but I think it works bc we're passing in tk.Frame in the class defn so it inherets all tk.Frame commands and it just... works?a
sfgFrame1 = widget_classes.sfgFrame(window)
sfgFrame1.pack(side="left")
   #window.bind("a", key_down)
   #window.bind("<KeyRelease-a>", key_up)
   #window.bind("b", key_downdict)
   #window.bind("<KeyRelease-b>", key_updict)

sfgFrame2 = widget_classes.sfgFrame(window)
sfgFrame2.pack(side="right")
print(type(sfgFrame1))
print(type(sfgFrame1.sfgDF))

window.mainloop()
