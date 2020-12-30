# Imports
import tkinter as tk
from tkinter import filedialog
import os

window = tk.Tk()
window.geometry("500x200")
window.title('Nightcoreify')
title = tk.Label(text="Insert a WAV file.")
title.pack()

def filePick():
    file = filedialog.askopenfile(parent=window,mode='rb',title='Choose a WAV file', filetypes=[("WAV File", "*.wav")])
    if file:
        data = file.read()
        file.close()
        print("I got %d bytes from this file." % len(data))

button = tk.Button(
    command=filePick,
    text="Click me to pick!",
    width=400,
    height=200,
    bg="green",
    fg="black",
)
button.pack()
window.mainloop()

