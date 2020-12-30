# Imports
import tkinter as tk
from tkinter import filedialog
import os
import wave
import numpy as np

# GUI creation
window = tk.Tk()
window.geometry("500x200")
window.title('Nightcoreify')
title = tk.Label(text="Insert a WAV file.")
title.pack()

def filePick():
    # Limit to just WAV files
    file = filedialog.askopenfile(parent=window, mode='rb', title='Choose a WAV file', filetypes=[("WAV File", "*.wav")])
    if file:
        dataw = file.read()
        print("Converting %d bytes from this file...." % len(dataw))
        wr = wave.open(file.name, 'r')
        par = list(wr.getparams())
        par[3] = 0  
        par = tuple(par)

        # Output file write
        ww = wave.open('nightcoreVersion.wav', 'w')
        ww.setparams(par)
        
        # Speed change by X1.5
        Change_RATE = 1.5
        RATE = wr.getframerate()
        ww.setframerate(RATE*Change_RATE)
        
        # Pitch change by 200Hz
        fr = 100 # Sound processing in fractions at a time
        sz = wr.getframerate()//fr  
        c = int(wr.getnframes()/sz)  
        pitchshift = 200//fr  

        for i in range(c):

            # Split data into left and right channel
            data = np.frombuffer(wr.readframes(sz), dtype=np.int16)
            left, right = data[0::2], data[1::2]  

            # Use Fast Fourier Transform to get frequencies
            lf, rf = np.fft.rfft(left), np.fft.rfft(right)
            lf, rf = np.roll(lf, pitchshift), np.roll(rf, pitchshift)
            lf[0:pitchshift], rf[0:pitchshift] = 0, 0

            # Inverser Fourier 
            nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
            ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
            
            #Output
            ww.writeframes(ns.tobytes())
        wr.close()
        ww.close()
        os.startfile('nightcoreVersion.wav')

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


