import tkinter as tk
import widget_classes as widget_classes

# Would be nice to replace this with data from sfgDF but it's nbd
ALL_SOLFEGE = set(["do", "re", "mi", "fa", "so", "la", "ti", "di", "ri", "fi", "si", "li", "ra", "me", "se", "le", "te"])

# Every key that will be used goes in here
VALID_KEYS = set(["d", "i", "e", "r", "m", "f", "s", "l", "t"])

# Hold all currently held down keys
GLOBAL_STATE = { "keys": set() }


def key_press_event(event, sfgFrame):
    GLOBAL_STATE["keys"].add(event.keysym)
    print(f"Key pressed: {GLOBAL_STATE}")

    refresh_solfege_ui(sfgFrame)


def key_release_event(event, sfgFrame):
    print(f"Key released: {GLOBAL_STATE}")
    GLOBAL_STATE["keys"].remove(event.keysym)

    refresh_solfege_ui(sfgFrame)


def refresh_solfege_ui(sfgFrame):
    active_solfege = get_solfege_from_keys_down(GLOBAL_STATE["keys"])
    inactive_solfege = ALL_SOLFEGE - active_solfege

    for solfege in active_solfege:
        sfgFrame.sfgDF[solfege]["tkButton"].configure(bg=sfgFrame.sfgDF[solfege]["activecolor"])

    for solfege in inactive_solfege:
        sfgFrame.sfgDF[solfege]["tkButton"].configure(bg=sfgFrame.sfgDF[solfege]["bgcolor"])


def get_solfege_from_keys_down(keys):
    # What I want i guess is to only ever have one down at a time?
    """
    Translate from some number of keys down to solfege strings
    """
    ret = set()

   #if set(["d", "i"]).issubset(keys):
   #    ret = set(["di", "re"])
   #if set(["d"]).issubset(keys):
   #    ret = set("do")

        
    if set(["d", "i"]).issubset(keys):
        return set(["di", "ra"])
    elif set(["d"]).issubset(keys):
        return set(["do"])

    if set(["r", "i"]).issubset(keys):
        return set(["ri", "me"])
    elif set(["r"]).issubset(keys):
        return set(["re"])

    elif set(["m"]).issubset(keys):
        return set(["mi"])

    if set(["f", "i"]).issubset(keys):
        return set(["fi", "se"])
    elif set(["f"]).issubset(keys):
        return set(["fa"])

    if set(["s", "i"]).issubset(keys):
        return set(["si", "le"])
    elif set(["s"]).issubset(keys):
        return set(["so"])

    if set(["l", "i"]).issubset(keys):
        return set(["li", "te"])
    elif set(["l"]).issubset(keys):
        return set(["la"])

    elif set(["t"]).issubset(keys):
        return set(["ti"])
   #if set(["i", "d"]).issubset(keys):
   #    ret.add("di")
   #elif set(["d"]).issubset(keys):
   #    ret.add("do")

   #if set(["r", "e"]).issubset(keys):
   #    ret.add("ra")
   #elif set(["r"]).issubset(keys):
   #    ret.add("re")

    print(f"the solfeges down are: {ret}")
    return ret
