#%% ex 6

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 0.02, 1/fs) 

x1 = np.sin(2 * np.pi * (fs/2) * t)
x2 = np.sin(2 * np.pi * (fs/4) * t)
x3 = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3, 1, figsize=(8, 6))
axs[0].stem(t, x1); axs[0].set_title('f = fs/2')
axs[1].stem(t, x2); axs[1].set_title('f = fs/4')
axs[2].stem(t, x3); axs[2].set_title('f = 0 Hz')
plt.tight_layout()
plt.savefig('3 semnale.pdf')
plt.show()