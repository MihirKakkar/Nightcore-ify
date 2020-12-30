#Imports
import wave
import numpy as np
from menu import *

def changeAudioSample():

    # Collect Audio Sample
    wr = wave.open('Data\papercut.wav', 'r')
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

changeAudioSample()

