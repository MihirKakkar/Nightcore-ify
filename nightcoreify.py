
#Imports
import wave
import numpy as np

#Collect Audio Sample
def collectAudioSample():
    wr = wave.open('Data\ImperialMarch60.wav', 'r')
    par = list(wr.getparams())
    par[3] = 0  # The number of samples will be set by writeframes.
    par = tuple(par)
    ww = wave.open('nightcoreVersion.wav', 'w')
    ww.setparams(par)
    
    Change_RATE = 1.5
    RATE = wr.getframerate()
    ww.setframerate(RATE*Change_RATE)
    

    ww.close()


collectAudioSample()
