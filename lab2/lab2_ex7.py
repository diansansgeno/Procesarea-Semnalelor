#%% ex 7

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 0.1, 1/fs)
x = np.sin(2 * np.pi * 50 * t)

# a decimare
x_dec = x[::4]

# b decimare incepand cu al doilea element
x_dec2 = x[1::4]

plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1); plt.plot(t, x, 'b-o'); plt.title('Original')
plt.subplot(3, 1, 2); plt.plot(t[::4], x_dec, 'r-o'); plt.title('Decimat [::4]')
plt.subplot(3, 1, 3); plt.plot(t[1::4], x_dec2, 'g-o'); plt.title('Decimat [1::4]')
plt.tight_layout()
plt.savefig('decimare.pdf')
plt.show()

# pentru a) se pastreaza forma generala a semnalului
# la b) ptc incepem de la alt esantion, faza se schimba foarte mult, iar frecventa pare diferita din cauza efectului de aliasing