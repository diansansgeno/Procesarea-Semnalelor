# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:51 2026

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

A =1
phi = 0
f0 = 5
fs_sub = 8
T = 0.03

t_cont = np.linspace(0, T, 2000)
n = np.arange(0, int(T * fs_sub) + 1)
t_s = n  / fs_sub

x0 = A * np.cos(2*np.pi*f0*t_cont + phi)
x1 = A * np.cos(2*np.pi*(f0 + fs_sub)*t_cont + phi)
x2 = A * np.cos(2*np.pi*(fs_sub - f0)*t_cont + phi)

s0 = A * np.cos(2*np.pi*f0*t_s + phi)
s1 = A * np.cos(2*np.pi*(f0 + fs_sub)*t_s + phi)
s2 = A * np.cos(2*np.pi*(fs_sub - f0)*t_s + phi)

plt.figure(figsize=(8, 8))
plt.subplot(4, 1, 1)
plt.plot(t_cont, x0, label='semnal original f0=5 Hz')
plt.plot(t_s, s0, 'yo', label='eșantioane')
plt.legend(); plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t_cont, x1, label='f1=13 Hz')
plt.plot(t_s, s1, 'yo', label='aceleași eșantioane')
plt.legend(); plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t_cont, x2, label='f2=3 Hz')
plt.plot(t_s, s2, 'yo', label='aceleași eșantioane')
plt.legend(); plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t_cont, x0, label='original')
plt.plot(t_cont, x2, '--', label='alias 3 Hz')
plt.plot(t_s, s0, 'yo')
plt.legend(); plt.grid(True)
plt.tight_layout()
plt.savefig('ex2_aliasing.pdf')

plt.show()