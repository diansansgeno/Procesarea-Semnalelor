# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:52 2026

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

A = 1.0
phi = 0.0
f0 = 5.0     
f1 = 13.0      
f2 = 3.0        
fs = 20.0       
T = 0.3         

t = np.linspace(0, T, 2000)
n = np.arange(0, int(T*fs)+1)
ts = n/fs

x0 = A*np.cos(2*np.pi*f0*t + phi)
x1 = A*np.cos(2*np.pi*f1*t + phi)
x2 = A*np.cos(2*np.pi*f2*t + phi)

s0 = A*np.cos(2*np.pi*f0*ts + phi)
s1 = A*np.cos(2*np.pi*f1*ts + phi)
s2 = A*np.cos(2*np.pi*f2*ts + phi)

# verificare numerică
print("max |s0-s1| =", np.max(np.abs(s0-s1)))
print("max |s0-s2| =", np.max(np.abs(s0-s2)))

plt.figure(figsize=(9, 8))

plt.subplot(4,1,1)
plt.plot(t, x0, label='original f0=5 Hz')
plt.plot(ts, s0, 'yo', label='eșantioane fs=20 Hz')
plt.legend(); plt.grid(True)
plt.title('Semnal original, fs > Nyquist')

plt.subplot(4,1,2)
plt.plot(t, x1, label='f1=13 Hz')
plt.plot(ts, s1, 'ro', label='eșantioanele lui f1')
plt.legend(); plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t, x2, label='f2=3 Hz')
plt.plot(ts, s2, 'go', label='eșantioanele lui f2')
plt.legend(); plt.grid(True)

plt.subplot(4,1,4)
plt.plot(ts, s0, 'yo-', label='eșantioane f0=5 Hz')
plt.plot(ts, s1, 'ro--', label='eșantioane f1=13 Hz')
plt.plot(ts, s2, 'go:', label='eșantioane f2=3 Hz')
plt.legend(); plt.grid(True)
plt.xlabel('timp [s]')

plt.tight_layout()
plt.savefig('ex3_fara_aliasing.pdf')
plt.show()