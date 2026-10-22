

#%% ex1

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 10000)
A = 2.
f = 5.
x = A * np.sin(2 * f * t * np.pi + np.pi / 4)
y = A * np.cos(2 * f * t * np.pi + np.pi / 4 - np.pi/2)

fix, (ax1, ax2) = plt.subplots(2, 1, figsize = (10, 8))

ax1.plot(t, x, color = 'purple')
ax1.set_title('sinus')
ax1.grid(True)
ax2.plot(t,  y, color = 'magenta')
ax2.set_title('cosinus')
ax2.grid(True)

plt.tight_layout()
plt.savefig('CosSinIdentice.pdf')
plt.show()