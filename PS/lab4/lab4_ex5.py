# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:55 2026

@author: Lenovo
"""

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

fs = 44100          

durata = 2.0    
    
vocale = ['a', 'e', 'i', 'o', 'u']

input("Apasă Enter și spune vocala 'a'...")
for v in vocale:
    print(f"Inregistrez vocala '{v}'...")
    audio = sd.rec(int(durata * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    write(f'vocala_{v}.wav', fs, audio)
    print(f"Salvat: vocala_{v}.wav")