import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt

print("🫀 Electrical Systems Engineering: ECG Digital Signal Processing Engine Online 🫀")

# =====================================================================
# 1. HARDWARE SAMPLING CONFIGURATION
# =====================================================================
fs = 500.0  # Sampling frequency of the ECG hardware module (500 Hz)
duration = 3.0  # Capture timeline window (3 seconds)
t = np.arange(int(duration * fs)) / fs

# =====================================================================
# 2. GENERATE CLEAN BIOLOGICAL ECG SIGNAL (P-QRS-T Complex)
# =====================================================================
clean_ecg = np.zeros_like(t)
# Simulate 3 heartbeats over a 3-second window (~60 BPM rhythm)
for beat_time in [0.5, 1.5, 2.5]:
    idx = int(beat_time * fs)
    
    # Model the QRS Complex (High amplitude ventricular depolarization spike)
    qrs_width = int(0.04 * fs)
    qrs_t = np.linspace(-1, 1, qrs_width * 2)
    qrs_wave = 1.5 * np.exp(-150 * qrs_t**2)
    clean_ecg[idx - qrs_width : idx + qrs_width] += qrs_wave
    
    # Model the T Wave (Ventricular repolarization swell)
    t_width = int(0.12 * fs)
    t_t = np.linspace(-1, 1, t_width * 2)
    t_wave = 0.25 * np.exp(-15 * t_t**2)
    clean_ecg[idx + int(0.2*fs) - t_width : idx + int(0.2*fs) + t_width] += t_wave
    
    # Model the P Wave (Atrial depolarization mound)
    p_width = int(0.08 * fs)
    p_t = np.linspace(-1, 1, p_width * 2)
    p_wave = 0.15 * np.exp(-25 * p_t**2)
    clean_ecg[idx - int(0.15*fs) - p_width : idx - int(0.15*fs) + p_width] += p_wave

# =====================================================================
# 3. INJECT ELECTROMAGNETIC HUM NOISE (60Hz Powerline Interference)
# =====================================================================
print("⚠️ Injecting 60Hz wall-power AC electromagnetic interference hum...")
noise_frequency = 60.0  # 60 Hz hum standard for US power grids
noise_amplitude = 0.6   # Severe noise amplitude masking the signal baseline
powerline_noise = noise_amplitude * np.sin(2 * np.pi * noise_frequency * t)

# Corrupted signal hitting the patient monitor acquisition board
corrupted_ecg = clean_ecg + powerline_noise

# =====================================================================
# 4. DESIGN AND APPLY DIGITAL IIR NOTCH FILTER
# =====================================================================
print("🎛️ Designing mathematical infinite impulse response (IIR) notch filter...")
# Design parameter constraints: Center frequency to strip, and Quality Factor (Q)
# A higher Q-factor ensures a tighter notch so we don't distort neighbor cardiac data
quality_factor = 30.0
b, a = iirnotch(w0=noise_frequency, Q=quality_factor, fs=fs)

print("⚡ Running zero-phase forward-backward filter processing...")
# Use filtfilt to avoid phase-shifting the signal waveform (crucial for medical accuracy)
filtered_ecg = filtfilt(b, a, corrupted_ecg)

# =====================================================================
# 5. DIAGNOSTIC PERFORMANCE WAVEFORM DISPLAY
# =====================================================================
print("📊 Compiling DSP Waveform Analysis Chart...")
fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True)

# Plot 1: Clean biological baseline reference
axes[0].plot(t, clean_ecg, color='#2ecc71', linewidth=1.8, label="Pure Biometric Cardiac Rhythm")
axes[0].set_title("1. Baseline Cardiac Signal (Target Output)", fontsize=11, color="white", weight="bold")
axes[0].grid(True, linestyle=':', alpha=0.4)

# Plot 2: Noisy corrupted stream
axes[1].plot(t, corrupted_ecg, color='#e74c3c', linewidth=1.2, label="Corrupted Stream (+60Hz Hum)")
axes[1].set_title("2. Raw Hardware Acquisition Input (Obscured by 60Hz Power-Line Hum)", fontsize=11, color="white", weight="bold")
axes[1].grid(True, linestyle=':', alpha=0.4)

# Plot 3: Recovered filtered signal output
axes[2].plot(t, filtered_ecg, color='#3498db', linewidth=1.8, label="Recovered ECG (Notch Applied)")
axes[2].set_title("3. Post-Processed DSP Output (60Hz Hum Attenuated via IIR Notch Filter)", fontsize=11, color="white", weight="bold")
axes[2].set_xlabel("Time Duration (Seconds)", fontweight="bold")
axes[2].grid(True, linestyle=':', alpha=0.4)

# Global layout styling configuration to match dark control suite guidelines
plt.suptitle("Clinical Hardware DSP: Real-Time 60Hz Electromagnetic Hum Attenuation", fontsize=13, fontweight='bold')
plt.tight_layout()

# Force dark-mode template colors
for ax in axes:
    ax.legend(loc='upper right')
    ax.set_ylabel("Amplitude (mV)", fontweight="bold")
    ax.set_facecolor('#2d2d35')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#44444e')
plt.gcf().patch.set_facecolor('#1e1e24')

plt.show()
print("🏁 Filter cycle analysis complete.")

