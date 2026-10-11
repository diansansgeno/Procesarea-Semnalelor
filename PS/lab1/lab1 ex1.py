# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:56:08 2026

@author: Lenovo
"""


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 10000) #axa timpuolui cu linspace

x = np.cos(520 * np.pi * t + np.pi/3)
y = np.cos(280 * np.pi * t - np.pi/3)
z = np.cos(120 * np.pi * t + np.pi/3)


#pentru axele nr reale

plt.figure()
plt.grid(True)

plt.axhline(0, color='purple', label='Axa reală')   
plt.plot(t, x, color='blue', label='x(t)')          
plt.legend()                                      


plt.xlabel('t')
plt.ylabel('f(t)')

plt.savefig('figura 1.pdf', bbox_inches='tight')
plt.show()
plt.close()

#axs este pt fiecare subplot

fig, axs = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

axs[0].plot(t, x, color='blue')
axs[0].set_title(r'$x = \cos(520\pi t + \pi/3)$  (f = 260 Hz)')
axs[0].grid(True)

axs[1].plot(t, y, color='red')
axs[1].set_title(r'$y = \cos(280\pi t - \pi/3)$  (f = 140 Hz)')
axs[1].grid(True)

axs[2].plot(t, z, color='gray')
axs[2].set_title(r'$z = \cos(120\pi t + \pi/3)$  (f = 60 Hz)')
axs[2].set_xlabel('t [s]')
axs[2].grid(True)

plt.tight_layout()
fig.savefig('figura 2.pdf', bbox_inches='tight')
plt.show()

plt.close(fig)

#pentru semnalul esantionat la 200 de hz

fs = 200  #frecv esant
Ts = 1 / fs  #timp esant

t_n = np.arange(0, 0.03 + Ts, Ts)   #axa de timp esant noua

x_n = np.cos(520 * np.pi * t_n + np.pi/3)
y_n = np.cos(280 * np.pi * t_n - np.pi/3)
z_n = np.cos(120 * np.pi * t_n + np.pi/3)

fig2, axs2 = plt.subplots(3, 1, figsize=(10, 8))
fig2.suptitle(f'(c) Semnale Eșantionate la fs = {fs} Hz')

axs2[0].stem(t_n, x_n, basefmt=" ", linefmt='turquoise', markerfmt='bo')
axs2[0].set_ylabel('x[n]')
axs2[0].grid(True)
axs2[0].set_title('Esantioane x[n]')

axs2[1].stem(t_n, y_n, basefmt=" ", linefmt='salmon', markerfmt='ro')
axs2[1].set_ylabel('y[n]')
axs2[1].grid(True)
axs2[1].set_title('Esantioane y[n]')

axs2[2].stem(t_n, z_n, basefmt=" ", linefmt='lime', markerfmt='go')
axs2[2].set_ylabel('z[n]')
axs2[2].set_xlabel('t [s]')
axs2[2].grid(True)
axs2[2].set_title('Esantioane z[n]')

#obs de la laborator: desi sunt semnale diferite, esantionarea aceaste le face sa se sincronizeze

plt.tight_layout()
fig2.savefig('figura 3.pdf', bbox_inches='tight')
plt.show()

plt.close(fig2)