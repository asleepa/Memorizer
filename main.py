# Memorizer
# Created by asleepa

import tkinter as tk
from pynput import mouse

# Change to false if you want the window size to automatically expand according to the line length.
# The line length can currently fit 10 numbers.
staticSize = True

winText = "200!! gg"
labelFont = ("Courier", 32)

lineIndex = 0

with open("numbers.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

def nextLine(_ = None):
    global lineIndex
    lineIndex += 1

    if (label.cget("text") == winText):
        lineIndex = 0

    label.config(text = lineIndex < len(lines) and lines[lineIndex] or winText)

window = tk.Tk()
window.title("Memorizer")
window.configure(bg = "black")
window.resizable(width = True, height = False)
window.attributes("-topmost", True)

if staticSize:
    window.geometry("300x100")
    window.minsize(width = 500, height = 100)

label = tk.Label(window, text = lines[0], font = labelFont, fg = "white", bg = "black")
label.pack(padx = 100, pady = 20)

def click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        window.after(ms = 0, func = nextLine)

listener = mouse.Listener(on_click = click)
listener.daemon = True
listener.start()

window.mainloop()
