# import tkinter

# window = tkinter.Tk()
# window.title("YUN DAE HEE")
# window.geometry("640x400+100+100")
# window.resizable(False, False)

# frame = tkinter.Frame(window)

# scrollbar = tkinter.Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")

# listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
# for line in range(1, 1001):
#     listbox.insert(line, str(line) + "/1000")
# listbox.pack(side="left")

# scrollbar["command"] = listbox.yview

# frame.pack()

# window.mainloop()

import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def getSquareRoot():
    x1 = entry1.get()

    label1 = tk.Label(root, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text="출력하기", command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
