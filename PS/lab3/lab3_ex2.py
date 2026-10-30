# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:08:02 2026

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

f0 = 5
fs = 1000
N2 = 1000
t = np.arange(N2) / fs       
x = np.cos(2 * np.pi * f0 * t)


# y(t) = x(t) * exp(-2*pi*j*1*t)
y = x * np.exp(-2j * np.pi * 1 * t)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(np.arange(N2), x)
ax[0].set_xlabel("Timp (eșantioane)")
ax[0].set_ylabel("Amplitudine")

ax[1].scatter(y.real, y.imag, c=np.abs(y), cmap="managua", s=4)
ax[1].set_xlabel("Real")
ax[1].set_ylabel("Imaginar")
ax[1].axis("equal")

plt.tight_layout()
plt.savefig("ex2_figura1.pdf")
plt.show()
w_values = [1, 2, f0, 7]    

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

for ax, w in zip(axs.ravel(), w_values):
    z = x * np.exp(-2j * np.pi * w * t)
    ax.scatter(z.real, z.imag, c=np.abs(z), cmap="managua", s=3)
    ax.set_title(f"omega = {w} Hz")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.axis("equal")

plt.tight_layout()
plt.savefig("ex2_figura2.pdf")
plt.show()

fig, ax = plt.subplots()
line, = ax.plot([], [], "b-")
point, = ax.plot([], [], "ro")

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(i):
    line.set_data(y[:i+1].real, y[:i+1].imag)
    point.set_data([y[i].real], [y[i].imag])
    return line, point

ani = FuncAnimation(fig, update, frames=len(y),
                    init_func=init, interval=20, blit=True)
plt.show()
