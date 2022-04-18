import tkinter as tk

def close_win(e):
    window.destroy()

window = tk.Tk();
window.bind('q', lambda e: close_win(e))

b1 = tk.Button(window, text="b1")
b1.grid(row=0,column=0, rowspan=2)
b2 = tk.Button(window, text="b2")
b2.grid(row=2,column=0)
b3 = tk.Button(window, text="b3")
b3.grid(row=4,column=0)

b1 = tk.Button(window, text="b1c1")
b1.grid(row=0,column=1)
b2 = tk.Button(window, text="b2c1")
b2.grid(row=1,column=1)
b3 = tk.Button(window, text="b3c1")
b3.grid(row=2,column=1)

b1 = tk.Button(window, text="b1")
b1.grid(row=0,column=3)
b2 = tk.Button(window, text="b2")
b2.grid(row=1,column=3)
b3 = tk.Button(window, text="b3")
b3.grid(row=2,column=3)
#print("asdf")
window.mainloop()
