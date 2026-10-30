# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:20:32 2026

@author: Lenovo
"""


import numpy as np
import matplotlib.pyplot as plt
f1, f2, f3 = 5, 20, 75       
fs3 = 200
N3 = 200
t3 = np.arange(N3) / fs3

x3 = (np.cos(2 * np.pi * f1 * t3)
      + 2 * np.cos(2 * np.pi * f2 * t3)
      + 0.5 * np.cos(2 * np.pi * f3 * t3))

freqs = np.arange(1, 101) 
n3 = np.arange(N3)

# X(f) = sum_n x[n] * exp(-2*pi*j*f*n/fs)
E = np.exp(-2j * np.pi * np.outer(freqs, n3) / fs3)
X = E @ x3

plt.figure(figsize=(8, 4))
plt.plot(freqs, np.abs(X), "o-")
plt.xlabel("Frecvența (Hz)")
plt.ylabel("|X(ω)|")
plt.title("Modulul transformatei Fourier")
plt.grid(True)
plt.savefig("ex3_modul_Fourier.pdf")
plt.show()