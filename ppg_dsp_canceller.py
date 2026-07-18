import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

print("🩸 Optical Physics & Data Science: PPG Motion Artifact Canceller Engine Online 🩸")

# =====================================================================
# 1. HARDWARE HARD-SAMPLING CONFIGURATION
# =====================================================================
fs = 100.0  # Sampling frequency of the photodiode sensor hardware (100 Hz)
duration = 10.0  # Capture timeline observation window (10 seconds)
t = np.arange(int(duration * fs)) / fs

# =====================================================================
# 2. GENERATE CLEAN PHYSIOLOGICAL PPG SIGNAL (Arterial Pulse Wave)
# =====================================================================
heart_rate_bpm = 72.0
cardiac_freq = heart_rate_bpm / 60.0  # 1.2 Hz arterial cycle frequency

# Model normal blood volume pulse waveform profile
clean_ppg = np.sin(2 * np.pi * cardiac_freq * t) 
# Inject a dicrotic notch to simulate back-pressure reflections from aortic valve closure
clean_ppg += 0.3 * np.sin(4 * np.pi * cardiac_freq * t + np.pi/4)

# =====================================================================
# 3. INJECT HARDWARE NOISE ARTIFACTS (Baseline Drift & Motion Sloshing)
# =====================================================================
print("⚠️ Injecting low-frequency venous baseline drift and high-frequency motion artifacts...")

# Baseline drift caused by patient respiration breathing cycles (0.25 Hz slow sway)
respiratory_drift = 1.5 * np.sin(2 * np.pi * 0.25 * t)

# Severe motion artifact noise from patient finger movements/shaking
np.random.seed(42)
motion_artifact = np.random.normal(0, 0.4, len(t))

# Total corrupted signal received by the monitor's front-end analog acquisition card
corrupted_ppg = clean_ppg + respiratory_drift + motion_artifact

# =====================================================================
# 4. IMPLEMENT DIGITAL FILTER SEPARATION PIPELINES
# =====================================================================
print("🎛️ Constructing digital High-Pass Butterworth filter to strip baseline drift...")
# Design a 2nd-order high-pass Butterworth filter to block everything below 0.5 Hz
def butter_highpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

b, a = butter_highpass(cutoff=0.5, fs=fs, order=2)
# Zero-phase forward-backward filter processing prevents timeline distortion spikes
drift_removed_ppg = filtfilt(b, a, corrupted_ppg)

print("⚡ Executing running moving-average window algorithm to smooth out motion jitter...")
# Apply a moving average filter window box to clean the high-frequency pixel fuzz
window_size = 5
window = np.ones(window_size) / window_size
recovered_ppg = np.convolve(drift_removed_ppg, window, mode='same')

# =====================================================================
# 5. DIAGNOSTIC PERFORMANCE WAVEFORM DISPLAY
# =====================================================================
print("📊 Compiling Optical DSP Component Analysis Charts...")
fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True)

# Plot 1: Corrupted raw sensor entry tracking lines
axes[0].plot(t, corrupted_ppg, color='#e74c3c', linewidth=1.2, label="Corrupted Input Waveform (+Drift +Jitter)")
axes[0].set_title("1. Raw Optical Sensor Signal (Obscured by Baseline Drift & Patient Motion Artifacts)", fontsize=11, color="white", weight="bold")

# Plot 2: Intermediate stage: baseline wander canceled out
axes[1].plot(t, drift_removed_ppg, color='#f1c40f', linewidth=1.2, label="High-Pass Output (Drift Attenuated)")
axes[1].set_title("2. Intermediate Stage: Baseline Wander Canceled via Butterworth Filter", fontsize=11, color="white", weight="bold")

# Plot 3: Complete recovered target output stream
axes[2].plot(t, recovered_ppg, color='#2ecc71', linewidth=1.8, label="Recovered Target Pulse (Smooth Baseline)")
axes[2].plot(t, clean_ppg, color='#ffffff', alpha=0.3, linestyle='--', label="Ideal Physical Blueprint Reference")
axes[2].set_title("3. Final Stabilized Post-Processed Output Vitals Waveform", fontsize=11, color="white", weight="bold")
axes[2].set_xlabel("Time Duration Run (Seconds)", fontweight="bold")

# Global layout styling configuration matching your personal dark brand guidelines
plt.suptitle("Clinical Hardware DSP: Real-Time Optical Pulse Oximeter Artifact Cancellation", fontsize=13, fontweight='bold')
plt.tight_layout()

# Force dark-mode template colors across canvas partitions
for ax in axes:
    ax.legend(loc='upper right')
    ax.set_ylabel("Intensity (V)", fontweight="bold")
    ax.set_facecolor('#2d2d35')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#44444e')
plt.gcf().patch.set_facecolor('#1e1e24')

plt.show()
print("🏁 Filter signal cancellation cycle complete.")
