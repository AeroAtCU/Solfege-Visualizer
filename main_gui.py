#https://stackoverflow.com/questions/27215326/tkinter-keypress-keyrelease-events
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
ALL_SOLFEGE = set(["do", "re", "mi", "fa", "so", "la", "ti", "di", "ri", "fi", "si", "li", "ra", "me", "se", "le", "te"])
VALID_KEYS = set(["d", "d", "i", "e", "r", "m", "f", "s", "l", "t"])
GLOBAL_STATE = { "keys": set() }


# No matter what, I need to pass information into the keypress function.
def kd(event, sfgFrame):
    sfgFrame.sfgDF["do"]["tkButton"].configure(bg=sfgFrame.sfgDF["do"]["activecolor"])

def ku(event, sfgFrame):
    sfgFrame.sfgDF["do"]["tkButton"].configure(bg=sfgFrame.sfgDF["do"]["bgcolor"])

# I think that's all I need now...
def close_win(e):
    print("exiting window...")
    window.destroy()

window = tk.Tk()
window.geometry("700x400")
window.bind('q', lambda e: close_win(e))
window.bind('j', lambda e: close_win(e))

# Create and display some sfg widgets
sfgFrame1 = widget_classes.sfgFrame(window)
sfgFrame2 = widget_classes.sfgFrame(window)
sfgFrame1.pack(side="left")
sfgFrame2.pack(side="right")


# okay, this allows me to send info to the function now alongwith the event
window.bind("c", lambda event: kd(event=event, sfgFrame=sfgFrame2))
window.bind("<KeyRelease-c>", lambda event: ku(event=event, sfgFrame=sfgFrame2))

# window.bind("b", key_downdict)
window.bind("b", lambda e: key_updict(e))
window.bind("<KeyRelease-b>", lambda e: key_updict(e))


def key_press_event(event):
    GLOBAL_STATE["keys"].add(event.keysym)
    print(f"Key pressed: {GLOBAL_STATE}")

    refresh_solfege_ui()


def key_release_event(event):
    print(f"Key released: {GLOBAL_STATE}")
    GLOBAL_STATE["keys"].remove(event.keysym)

    refresh_solfege_ui()


def refresh_solfege_ui():
    active_solfege = get_solfege_from_keys_down(GLOBAL_STATE["keys"])
    inactive_solfege = ALL_SOLFEGE - active_solfege

    for solfege in active_solfege:
        sfgFrame1.sfgDF[solfege]["tkButton"].configure(bg=sfgFrame1.sfgDF[solfege]["activecolor"])

    for solfege in inactive_solfege:
        sfgFrame1.sfgDF[solfege]["tkButton"].configure(bg=sfgFrame1.sfgDF[solfege]["bgcolor"])


def get_solfege_from_keys_down(keys):
    """
    Translate from some number of keys down to solfege strings
    """
    ret = set()

    if set(["i", "d"]).issubset(keys):
        ret.add("di")
    elif set(["d"]).issubset(keys):
        ret.add("do")

    if set(["r", "e"]).issubset(keys):
        ret.add("ra")
    elif set(["r"]).issubset(keys):
        ret.add("re")

    print(f"the solfeges down are: {ret}")
    return ret

for k in VALID_KEYS:
    window.bind(k, key_press_event)
    window.bind(f"<KeyRelease-{k}>", key_release_event)

# To access the buttons: sfgFrame.sfgDF.sfg_dict["do"]
window.mainloop()
