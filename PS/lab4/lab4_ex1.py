# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:30 2026

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def dft(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    X = np.empty(N, dtype=complex)
    n = np.arange(N)
    for k in range(N):
        X[k] = np.sum(x * np.exp(-2j * np.pi * k * n / N))
    return X

def fft_rec(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    if N <= 1:
        return x
    even = fft_rec(x[0::2])
    odd  = fft_rec(x[1::2])
    k = np.arange(N // 2)
    tw = np.exp(-2j * np.pi * k / N) * odd
    return np.concatenate([even + tw, even - tw])

N_values = [128, 256, 512, 1024, 2048, 4096, 8192]
t_dft, t_fft, t_np = [], [], []

for N in N_values:
    x = np.random.randn(N)
    
    start = time.perf_counter()
    _ = dft(x)
    t_dft.append(time.perf_counter() - start)

    start = time.perf_counter()
    _ = fft_rec(x)
    t_fft.append(time.perf_counter() - start)

    start = time.perf_counter()
    _ = np.fft.fft(x)
    t_np.append(time.perf_counter() - start)
    
plt.figure()
plt.plot(N_values, t_dft, 'o-', label='DFT implementat')
plt.plot(N_values, t_fft, 's-', label='FFT implementat')
plt.plot(N_values, t_np, '^-', label='numpy.fft')
plt.xscale('log')
plt.yscale('log')  
plt.xlabel('N')
plt.ylabel('timp [s]')
plt.grid(True, which='both')
plt.legend()
plt.savefig('ex1_timp_DFT_FFT.pdf')
plt.show()