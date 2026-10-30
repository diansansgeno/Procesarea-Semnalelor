# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:01:49 2026

@author: Lenovo
"""



import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
k = np.arange(N)

F = np.exp(-2j * np.pi * np.outer(k, n) / N) / np.sqrt(N)

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

for i in range(N):
    ax[0].plot(n, F[i].real, "o-", label=f"Linia {i}")
    ax[1].plot(n, F[i].imag, "o-", label=f"Linia {i}")

ax[0].set_title("Partea reala a matricei Fourier")
ax[1].set_title("Partea imaginara a matricei Fourier")

for a in ax:
    a.set_xlabel("n")
    a.grid()
    a.legend(ncol=4, fontsize=8)

plt.tight_layout()
plt.savefig("Matricea Fourier.pdf")

I = F.conj().T @ F

print("Matricea Fourier F:")
print(np.round(F, 3))

print("\nF^H * F:")
print(np.round(I, 3))

print("\nNorma F^H F - I:",
      np.linalg.norm(I - np.eye(N)))

