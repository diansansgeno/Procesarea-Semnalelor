import os
import numpy as np
import matplotlib.pyplot as plt

try:
    import kagglehub
except ImportError:
    raise ImportError("Ruleaza: pip install kagglehub")

cale_dataset = kagglehub.dataset_download("lampubhutia/bullettrain-timeseries-data")
cale_train = os.path.join(cale_dataset, "Train.csv")

if not os.path.isfile(cale_train):
    for radacina, _, fisiere in os.walk(cale_dataset):
        if "Train.csv" in fisiere:
            cale_train = os.path.join(radacina, "Train.csv")
            break


def citeste_semnal(path):
    with open(path, "r", encoding="utf-8") as f:
        linii = [l.strip() for l in f if l.strip()]

    sep = ","
    if ";" in linii[0] and linii[0].count(";") > linii[0].count(","):
        sep = ";"

    rows = []
    for linie in linii:
        parts = linie.split(sep)
        vals = []
        for p in parts:
            p = p.strip()
            if p == "":
                continue
            try:
                vals.append(float(p))
            except ValueError:
                vals.append(np.nan)
        if len(vals) > 0 and np.any(np.isfinite(vals)):
            rows.append(vals)

    maxcol = max(len(r) for r in rows)
    arr = np.full((len(rows), maxcol), np.nan)
    for i, r in enumerate(rows):
        arr[i, :len(r)] = r

    for j in range(arr.shape[1] - 1, -1, -1):
        col = arr[:, j]
        if np.sum(np.isfinite(col)) > 0.9 * len(col):
            return col[np.isfinite(col)].astype(float)

    raise ValueError("Nu am gasit o coloana numerica in fisier.")


x = citeste_semnal(cale_train)
N = len(x)
print("Numar esantioane N =", N)
t_h = np.arange(N)

# a
fs_hz = 1.0 / 3600.0
fs_cph = 1.0

print("\n(a) Frecventa de esantionare:")
print("fs =", fs_hz, "Hz")
print("fs =", fs_cph, "esantion/ora")

# c
f_max = fs_hz / 2.0
print("\n(c) Frecventa maxima Nyquist:")
print("f_max =", f_max, "Hz")
print("Perioada minima =", 1.0 / f_max, "s =", 1.0 / f_max / 3600.0, "h")

# d
dc = np.mean(x)
print("\nMedia semnalului / componenta DC =", dc)

X = np.fft.fft(x)
f_hz = np.fft.fftfreq(N, d=3600.0)

X_half = X[:N // 2]
f_half_hz = f_hz[:N // 2]
mag_half = np.abs(X_half)

eps = 1e-12
mask_f = f_half_hz > 0
f_plot = f_half_hz[mask_f]
m_plot = mag_half[mask_f] + eps

fig1 = plt.figure(figsize=(10, 5))
plt.loglog(f_plot, m_plot)
plt.xlabel("Frecventa [Hz], scara log")
plt.ylabel("|X(f)|, scara log")
plt.title("Spectrul de amplitudine, jumatatea utila (log-log)")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
fig1.savefig("01_spectru_loglog_Hz.pdf", bbox_inches="tight")
plt.show()

fig2 = plt.figure(figsize=(10, 5))
plt.semilogx(f_plot, m_plot)
plt.xlabel("Frecventa [Hz], scara log")
plt.ylabel("|X(f)|, scara liniara")
plt.title("Spectrul de amplitudine, jumatatea utila (semilogx)")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
fig2.savefig("02_spectru_semilogx_Hz.pdf", bbox_inches="tight")
plt.show()

Xr = np.fft.rfft(x)
fr_cph = np.fft.rfftfreq(N, d=1.0)
mag_r = np.abs(Xr)

mask_cph = fr_cph > 0
fr_plot = fr_cph[mask_cph]
mr_plot = mag_r[mask_cph] + eps

fig3 = plt.figure(figsize=(10, 5))
plt.loglog(fr_plot, mr_plot)
plt.xlabel("Frecventa [cicluri/ora], scara log")
plt.ylabel("|X(f)|, scara log")
plt.title("Spectrul in cicluri/ora (log-log)")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
fig3.savefig("03_spectru_loglog_cph.pdf", bbox_inches="tight")
plt.show()

# e
print("\n(e) Componenta continua:")
print("X[0] =", X[0])
print("N * mean(x) =", N * dc)

x_fara_dc = x - dc


# f
def varfuri_principale(x, n=4, perioada_min_h=4.0, perioada_max_h=2000.0):
    N = len(x)
    t = np.arange(N)
    coef = np.polyfit(t, x, 1)
    trend = np.polyval(coef, t)
    xd = x - trend
    xd = xd - np.mean(xd)

    X = np.fft.rfft(xd)
    f = np.fft.rfftfreq(N, d=1.0)
    mag = np.abs(X)

    fmin = 1.0 / perioada_max_h
    fmax = 1.0 / perioada_min_h
    idx = np.where((f >= fmin) & (f <= fmax))[0]
    idx = idx[(idx > 0) & (idx < len(mag) - 1)]

    local = idx[(mag[idx] > mag[idx - 1]) & (mag[idx] > mag[idx + 1])]
    local = local[np.argsort(mag[local])[::-1]]

    alese = []
    for i in local:
        if all(abs(f[i] - f[j]) > 2.0 / N for j in alese):
            alese.append(i)
        if len(alese) == n:
            break

    return f[alese], mag[alese]


f_princ, mag_princ = varfuri_principale(x, n=4)

print("\n(f) Primele frecvente principale dupa eliminarea DC si a tendintei:")
for f_cph, m in zip(f_princ, mag_princ):
    perioada_h = 1.0 / f_cph
    f_hz_i = f_cph / 3600.0
    print("f = {:.8f} cph = {:.6e} Hz, perioada = {:.3f} h, |X| = {:.3e}".format(
        f_cph, f_hz_i, perioada_h, m
    ))

t = np.arange(N)
coef = np.polyfit(t, x, 1)
trend = np.polyval(coef, t)
xd = x - trend
xd = xd - np.mean(xd)
Xd = np.fft.rfft(xd)
fd = np.fft.rfftfreq(N, d=1.0)
magd = np.abs(Xd)

mask_d = fd > 0
fd_plot = fd[mask_d]
magd_plot = magd[mask_d] + eps

fig4 = plt.figure(figsize=(10, 5))
plt.loglog(fd_plot, magd_plot)
for f_cph, m in zip(f_princ, mag_princ):
    plt.plot(f_cph, m, "ro")
    plt.annotate("{:.2f} h".format(1.0 / f_cph), (f_cph, m),
                 textcoords="offset points", xytext=(6, 4), fontsize=9)
plt.xlabel("Frecventa [cicluri/ora], scara log")
plt.ylabel("|X(f)|, scara log")
plt.title("Spectru dupa eliminarea DC si a tendintei, cu varfuri marcate (log-log)")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
fig4.savefig("04_spectru_detrend_varfuri.pdf", bbox_inches="tight")
plt.show()

# g
def estimeaza_faza_saptamanala(x, week=168):
    N = len(x)
    phase = np.arange(N) % week

    profil = np.full(week, np.nan)
    for h in range(week):
        selectie = x[phase == h]
        if len(selectie) > 0:
            profil[h] = np.mean(selectie)

    if np.any(~np.isfinite(profil)):
        good = np.isfinite(profil)
        profil[~good] = np.interp(
            np.where(~good)[0],
            np.where(good)[0],
            profil[good]
        )

    k = np.ones(7) / 7.0
    ext = np.r_[profil[-3:], profil, profil[:3]]
    profil_s = np.convolve(ext, k, mode="same")[3:-3]

    win = 48
    medii = np.array([
        np.mean([profil_s[(i + j) % week] for j in range(win)])
        for i in range(week)
    ])

    start_weekend = int(np.argmin(medii))
    return (start_weekend + win) % week


faza_luni = estimeaza_faza_saptamanala(x)
print("\n(g) Faza estimata pentru luni:", faza_luni)

start = 1001
while start < N and start % 168 != faza_luni:
    start += 1

if start + 30 * 24 > N:
    start = max(1001, N - 30 * 24)

print("Index start pentru o luna de trafic:", start)

fig5 = plt.figure(figsize=(12, 4))
plt.plot(np.arange(30 * 24), x[start:start + 30 * 24])
plt.xlabel("Timp [h]")
plt.ylabel("Numar masini")
plt.title("O luna de trafic, incepand aproximativ de luni")
plt.grid(True)
plt.tight_layout()
fig5.savefig("05_o_luna_trafic.pdf", bbox_inches="tight")
plt.show()

# h
# Data absoluta nu se poate determina doar din semnal.
# Se pot estima faza zilei si faza saptamanii.
# Pentru data calendaristica este nevoie de o referinta externa.

# i
def filtru_trece_jos_fft(x, fc_cph):
    N = len(x)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(N, d=1.0)
    X[f > fc_cph] = 0
    return np.fft.irfft(X, n=N)


fc_cph = 1.0 / 6.0
x_filtrat = filtru_trece_jos_fft(x - np.mean(x), fc_cph=fc_cph) + np.mean(x)

fig6 = plt.figure(figsize=(12, 5))
plt.plot(t_h[:2000], x[:2000], label="semnal brut", alpha=0.6)
plt.plot(t_h[:2000], x_filtrat[:2000], label="filtrat, fc = 1/6 cph", linewidth=2)
plt.xlabel("Timp [h]")
plt.ylabel("Numar masini")
plt.title("Semnal brut si semnal filtrat trece-jos")
plt.legend()
plt.grid(True)
plt.tight_layout()
fig6.savefig("06_brut_vs_filtrat.pdf", bbox_inches="tight")
plt.show()

fig7 = plt.figure(figsize=(12, 5))
plt.semilogy(t_h[:2000], x[:2000] + 1, label="semnal brut + 1", alpha=0.6)
plt.semilogy(t_h[:2000], x_filtrat[:2000] + 1, label="filtrat + 1", linewidth=2)
plt.xlabel("Timp [h]")
plt.ylabel("Numar masini + 1, scara log")
plt.title("Comparatie semilog (Y) a semnalului brut si filtrat")
plt.legend()
plt.grid(True, which="both", ls=":")
plt.tight_layout()
fig7.savefig("07_brut_vs_filtrat_semilog.pdf", bbox_inches="tight")
plt.show()