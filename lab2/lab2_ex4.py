#%% ex 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

t = np.linspace(0, 1, 10000)
x = np.sin(2 * np.pi * 5 * t)
y = sawtooth(2 * np.pi * 5 * t)
suma = x + y

fig, axs = plt.subplots(3, 1, figsize=(8, 6))
axs[0].plot(t, x, 'b'); axs[0].set_title('Sinus')
axs[1].plot(t, y, 'r'); axs[1].set_title('Sawtooth')
axs[2].plot(t, suma, 'g'); axs[2].set_title('Suma')
plt.tight_layout()
plt.savefig('SSS.pdf')
plt.show()