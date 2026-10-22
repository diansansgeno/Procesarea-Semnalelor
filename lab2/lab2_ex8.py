
#%% ex 8

import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi/2, np.pi/2, 500)
sin_real = np.sin(alpha)

# aprox Taylor (sin(a) = a)
taylor = alpha

# aproximare Pade
pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

axs[0].plot(alpha, sin_real, 'k-', label='sin(a)')
axs[0].plot(alpha, taylor, 'r--', label='Taylor')
axs[0].plot(alpha, pade, 'b--', label='Pade')
axs[0].legend(); axs[0].set_title('Aproximari')

# grafic eroare Taylor
axs[1].plot(alpha, np.abs(sin_real - taylor))
axs[1].set_title('Eroare Taylor')

# grafic eroare Pade (scara logaritmica pe Oy)
axs[2].semilogy(alpha, np.abs(sin_real - pade))
axs[2].set_title('Eroare Pade (log)')

plt.tight_layout()
plt.savefig('Pade si Taylor.pdf')
plt.show()