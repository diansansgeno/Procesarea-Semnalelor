# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:56 2026

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, x = wavfile.read('vocala_a.wav')
if x.ndim > 1:
    x = x[:, 0]
x = x.astype(float)
x = x / (np.max(np.abs(x)) + 1e-12)

N = len(x)
L = max(32, int(0.01 * N))
hop = L // 2

frames = []
start = 0
while start + L <= N:
    frames.append(x[start:start + L])
    start += hop

fereastra = np.hanning(L)
fft_list = []
for fr in frames:
    X = np.fft.rfft(fr * fereastra)
    fft_list.append(np.abs(X))

S = np.array(fft_list).T
S_db = 20 * np.log10(S + 1e-12)

frecvente = np.linspace(0, fs / 2, S.shape[0])
timp = np.arange(S.shape[1]) * hop / fs

plt.figure(figsize=(12, 5))
plt.pcolormesh(timp, frecvente, S_db, shading='auto', cmap='magma')
plt.ylim(0, 5000)
plt.xlabel('timp [s]')
plt.ylabel('frecventa [Hz]')
plt.title('Spectrograma manuala')
plt.colorbar(label='magnitudine [dB]')
plt.tight_layout()
plt.savefig('ex6_spectrograma_vocala_A.pdf')
plt.show()