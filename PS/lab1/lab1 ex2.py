# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:00:41 2026

@author: Lenovo
"""


import numpy as np
import matplotlib.pyplot as plt

fs_a = 8000  #nr esant pe secunda
N_a = 1600  #nr de esantioane
t_a = np.arange(N_a) / fs_a  #timp esant

x_a = np.cos(2 * np.pi * 400 * t_a)

plt.figure(figsize=(10, 3))
plt.plot(t_a, x_a, color='blue')
plt.title('(a) Semnal sinusoidal 400 Hz, 1600 eșantioane')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.savefig('figura 3.pdf', bbox_inches='tight')

plt.show()



fs_b = 8000 #nr, esant per sec
T_b = 3     
t_b = np.arange(0, T_b, 1/fs_b)

x_b = np.cos(2 * np.pi * 800 * t_b)

plt.figure(figsize=(10, 3))
plt.plot(t_b, x_b, color='pink')
plt.title('(b) Semnal sinusoidal 800 Hz, durata 3 secunde')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.savefig('figura 4.pdf', bbox_inches='tight')

plt.show()


fs_c = 10000 #nr, esant per sec
T_c = 0.05   
t_c = np.arange(0, T_c, 1/fs_c)
f_c = 240  #frecv esant

x_c = 2 * np.mod(t_c * f_c, 1) - 1 #sawtooth conform wiki

plt.figure(figsize=(10, 3))
plt.plot(t_c, x_c, color='green')
plt.title('(c) Semnal sawtooth 240 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.savefig('figura 5.pdf', bbox_inches='tight')

plt.show()


fs_d = 100000          # esantionare mare pentru tranz
f_d  = 300             # frecv
T_d  = 3 / f_d         # perioade

t_d = np.arange(0, T_d, 1/fs_d)

x_d = np.sign(np.sin(2 * np.pi * f_d * t_d))

plt.figure(figsize=(10, 3))
plt.plot(t_d, x_d, color='purple', drawstyle='steps-post', linewidth=2)
plt.title('(d) Semnal de tip square, 300 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.ylim(-1.2, 1.2)
plt.grid(True)
plt.savefig('figura 6.pdf', bbox_inches='tight')

plt.show()



I_e = np.random.rand(128, 128)

plt.figure(figsize=(5, 5))
plt.imshow(I_e, cmap='managua') #am gasit managua in lista de valori posibile dupa ce am incercat cu 'green' si nu a mers si managua mi a placut cel mai mult
plt.title('(e) Semnal 2D aleator (128x128)')
plt.colorbar()
plt.savefig('figura 7.pdf', bbox_inches='tight')

plt.show()




I_f = np.zeros((128, 128))

y, x = np.ogrid[-64:64, -64:64]
masca_cerc = x**2 + y**2 <= 40**2
I_f[masca_cerc] = 1

plt.figure(figsize=(5, 5))
plt.imshow(I_f, cmap='managua_r') #managua_r il face sa arate ca un soare :)
plt.title('(f) Semnal 2D personalizat (Cerc)')
plt.savefig('figura 8.pdf', bbox_inches='tight')

plt.show()