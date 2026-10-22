# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:19:40 2026

@author: Lenovo
"""

#%% ex 3
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

# a
fs_a = 8000
N_a = 1600
t_a = np.arange(N_a) / fs_a
x_a = np.cos(2 * np.pi * 400 * t_a)

print("Semnalul a")
sd.play(x_a, fs_a)
sd.wait()

wavfile.write('semnal_a.wav', fs_a, x_a.astype(np.float32))

fs_read, x_read = wavfile.read('semnal_a.wav')
print(f"Rata esantionare: {fs_read} Hz, Esantioane: {len(x_read)}")

#b
fs_b = 8000 
T_b = 3     
t_b = np.arange(0, T_b, 1/fs_b)
x_b = np.cos(2 * np.pi * 800 * t_b)

print("Semnalul (b)")
sd.play(x_b, fs_b)
sd.wait()

#c
fs_c = 10000 
T_c = 0.05   
t_c = np.arange(0, T_c, 1/fs_c)
f_c = 240  
x_c = 2 * np.mod(t_c * f_c, 1) - 1 

print("Semnalul (c)")
sd.play(x_c, fs_c)
sd.wait()

# d
fs_d = 100000          
f_d  = 300             
T_d  = 3 / f_d         
t_d = np.arange(0, T_d, 1/fs_d)
x_d = np.sign(np.sin(2 * np.pi * f_d * t_d))

print("Semnalul (d)")
sd.play(x_d, fs_d)
sd.wait()

print("success")