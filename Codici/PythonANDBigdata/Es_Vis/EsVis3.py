import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Impostiamo il seed per la riproducibilità dei dati casuali
np.random.seed(0)

# Generiamo un segnale sinusoidale con rumore aggiunto
t = np.linspace(0, 10, 500)  # Vettore temporale da 0 a 10 secondi con 500 punti
segnale_pulito = np.sin(2 * np.pi * t)  # Segnale sinusoidale senza rumore
rumore = np.random.normal(0, 0.5, t.shape)  # Rumore gaussiano con deviazione standard 0.5
segnale_noisy = segnale_pulito + rumore  # Segnale con rumore aggiunto

# Calcoliamo la trasformata di Fourier del segnale rumoroso
fft_vals = np.fft.fft(segnale_noisy)
frequenze = np.fft.fftfreq(len(t), t[1] - t[0])

# Creiamo una figura con due sottotrame (subplot)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Prima sottotrama: segnale nel dominio del tempo
ax1.plot(t, segnale_noisy, label='Segnale con rumore', color='blue')
ax1.plot(t, segnale_pulito, label='Segnale originale', color='red', linestyle='--')
ax1.set_title('Segnale nel dominio del tempo')
ax1.set_xlabel('Tempo [s]')
ax1.set_ylabel('Ampiezza')
ax1.legend()
ax1.grid(True)

# Seconda sottotrama: modulo della trasformata di Fourier nel dominio delle frequenze
ax2.plot(frequenze, np.abs(fft_vals), color='green')
ax2.set_title('Spettro di frequenza del segnale')
ax2.set_xlabel('Frequenza [Hz]')
ax2.set_ylabel('Ampiezza')
ax2.set_xlim(0, 5)  # Limitiamo l'asse x per focalizzarci sulle basse frequenze
ax2.grid(True)

# Miglioriamo la disposizione dei subplot
plt.tight_layout()
plt.show()
