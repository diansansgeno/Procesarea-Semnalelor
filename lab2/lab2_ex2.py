
#%% ex 2

import numpy as np
import matplotlib.pyplot as plt

f = 3.
t = np.linspace(0, 0.1, 10000)
faze = [1, np.pi/4, np.pi/2, 3*np.pi/4]

plt.figure(figsize=(10, 8))
for fz in faze:
    x = np.sin(2 * f * t * np.pi + fz)
    plt.plot(t, x, label=f'Faza = {fz:.2f} radiani')
    
plt.title('Faze Diferite')
plt.xlabel('timp')
plt.ylabel('amplitudine')
plt.legend()
plt.grid(True)
plt.savefig('FazeDif.pdf')
plt.show()

x_nf = np.sin(2 * f * t * np.pi)
z = np.random.normal(0, 1, len(t))

norm_x = np.linalg.norm(x_nf)**2 
norm_z = np.linalg.norm(z)**2

snr_values = [0.1, 1, 10, 100]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, snrr in enumerate(snr_values):
    gamma = np.sqrt(norm_x / (snrr * norm_z))
    x_zgomot = x_nf + gamma * z

    axes[i].plot(t, x_nf, 'k--', alpha=0.4, label='Semnal curat')
    axes[i].plot(t, x_zgomot, 'b-', alpha=0.8, label='Semnal cu zgomot')
    axes[i].set_title(f'SNR = {snrr} (gamma = {gamma:.4f})')
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.savefig('snr.pdf')
plt.show()