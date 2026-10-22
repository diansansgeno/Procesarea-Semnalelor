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

#%% ex 3
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

# a
fs_a = 8000
N_a = 1600
t_a = np.arange(N_a) / fs_a
x_a = np.cos(2 * np.pi * 400 * t_a)

print("Semnalul a")
sd.play(x_a, fs_a)
sd.wait()

wavfile.write('semnal_a.wav', fs_a, x_a.astype(np.float32))

fs_read, x_read = wavfile.read('semnal_a.wav')
print(f"Rata esantionare: {fs_read} Hz, Esantioane: {len(x_read)}")

#b
fs_b = 8000 
T_b = 3     
t_b = np.arange(0, T_b, 1/fs_b)
x_b = np.cos(2 * np.pi * 800 * t_b)

print("Semnalul (b)")
sd.play(x_b, fs_b)
sd.wait()

#c
fs_c = 10000 
T_c = 0.05   
t_c = np.arange(0, T_c, 1/fs_c)
f_c = 240  
x_c = 2 * np.mod(t_c * f_c, 1) - 1 

print("Semnalul (c)")
sd.play(x_c, fs_c)
sd.wait()

# d
fs_d = 100000          
f_d  = 300             
T_d  = 3 / f_d         
t_d = np.arange(0, T_d, 1/fs_d)
x_d = np.sign(np.sin(2 * np.pi * f_d * t_d))

print("Semnalul (d)")
sd.play(x_d, fs_d)
sd.wait()

print("success")

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

#%% ex 5

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100
t = np.linspace(0, 0.5, fs // 2, endpoint=False)

sig1 = np.sin(2 * np.pi * 440 * t)
sig2 = np.sin(2 * np.pi * 880 * t)

semnal_concat = np.concatenate((sig1, sig2))
t_concat = np.linspace(0, 1.0, len(semnal_concat), endpoint=False)

sd.play(semnal_concat, fs)
sd.wait()

plt.figure(figsize=(10, 4))
plt.plot(t_concat, semnal_concat, color='orange')
plt.xlim(0, 0.55) 
plt.title('Concatenate')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.tight_layout()
plt.savefig('Concatenate.pdf')
plt.show()

#3 jumatate din timp este ocupat de primul semnal iar cel de al doilea semnal ocupa restul de 0.5 secunde

#pe grafic se obserrva ca la 0.5 frecventa se dubleaza, asa cum ar trebui pentru ca am ales semnalul 2 = 2* semnal 1

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