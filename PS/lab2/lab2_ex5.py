# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:21:28 2026

@author: Lenovo
"""

#%% ex 5

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100
t = np.linspace(0, 0.5, fs // 2, endpoint=False)

sig1 = np.sin(2 * np.pi * 440 * t)
sig2 = np.sin(2 * np.pi * 880 * t)

semnal_concat = np.concatenate((sig1, sig2))
t_concat = np.linspace(0, 1.0, len(semnal_concat), endpoint=False)

sd.play(semnal_concat, fs)
sd.wait()

plt.figure(figsize=(10, 4))
plt.plot(t_concat, semnal_concat, color='orange')
plt.xlim(0, 0.55) 
plt.title('Concatenate')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.tight_layout()
plt.savefig('Concatenate.pdf')
plt.show()

#3 jumatate din timp este ocupat de primul semnal iar cel de al doilea semnal ocupa restul de 0.5 secunde

#pe grafic se obserrva ca la 0.5 frecventa se dubleaza, asa cum ar trebui pentru ca am ales semnalul 2 = 2* semnal 1