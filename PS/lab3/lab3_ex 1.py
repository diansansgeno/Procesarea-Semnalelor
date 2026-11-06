# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
k = np.arange(N)

F = np.exp(-2j * np.pi * np.outer(k, n) / N) / np.sqrt(N)

labels = [f"Linia {i}" for i in range(N)]

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(n, F.real.T, "o-", label=labels)
ax[0].set_title("Partea reala a matricei Fourier")
ax[0].set_xlabel("n")
ax[0].grid()
ax[0].legend(ncol=4, fontsize=8)

ax[1].plot(n, F.imag.T, "o-", label=labels)
ax[1].set_title("Partea imaginara a matricei Fourier")
ax[1].set_xlabel("n")
ax[1].grid()
ax[1].legend(ncol=4, fontsize=8)

plt.tight_layout()
plt.savefig("Matricea Fourier.pdf")
plt.show()



I = F.conj().T @ F

print("Matricea Fourier F:")
print(np.round(F, 3))

print("\nF^H * F:")
print(np.round(I, 3))

print("\nNorma F^H F - I:", np.linalg.norm(I - np.eye(N)))