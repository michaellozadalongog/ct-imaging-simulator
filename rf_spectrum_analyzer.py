import numpy as np
import matplotlib.pyplot as plt

print("📡 KapoleiBioForge Telecommunications Engine: RF Spectrum Analyzer Active 📡")

# =====================================================================
# 1. HARDWARE COMMUNICATIONS CONFIGURATION
# =====================================================================
fs = 2000.0                      # Sampling frequency of the RF digital receiver (2 kHz)
duration = 4.0                   # Continuous signal window sweep time (4 seconds)
t = np.arange(int(duration * fs)) / fs

# Target telemetry transmission parameters (WMTS Band Channel Model)
CARRIER_FREQ_HZ = 150.0          # Down-converted telemetry intermediate carrier signal
target_amplitude = 2.0           # Pure baseline transmission output signal power

# =====================================================================
# CLINICAL HOSPITAL SPECTRUM SCENARIO CAPTURE
# =====================================================================
try:
    print("\n--- Configure Local Oahu Wireless Environment Metrics ---")
    print("1: Standard Ward (Optimal line-of-sight to wireless access points)")
    print("2: Concrete Isolation Unit (High multipath signal path-loss fading)")
    print("3: Severe Military Radar Bleed-Through (Active high-power radar interference)")
    environment_choice = input("Select local spectrum scenario profile (1, 2, or 3): ").strip()
except ValueError:
    environment_choice = "1"

# Generate the pure biological patient telemetry data modulated onto carrier wave
pure_signal = target_amplitude * np.sin(2 * np.pi * CARRIER_FREQ_HZ * t)

# =====================================================================
# 2. INJECT COMPLEX ENVIRONMENTAL SPECTRUM CONSTRAINTS
# =====================================================================
np.random.seed(808) # Hawaiian area code seed configuration

# Set up baseline white Gaussian background thermal tracking noise
thermal_noise = np.random.normal(0, 0.15, len(t))
attenuation_factor = 1.0
radar_pulse_noise = np.zeros_like(t)

if environment_choice == "2":
    # Scenario 2: Structural concrete walls attenuate signal amplitude by 65% (Path-Loss Fading)
    attenuation_factor = 0.35
elif environment_choice == "3":
    # Scenario 3: High-power intermittent pulse radar bursts cutting across patient channels
    for burst_center in [1.0, 2.2, 3.5]:
        pulse_mask = (t >= burst_center) & (t <= burst_center + 0.15) # 150ms radar bursts
        radar_pulse_noise[pulse_mask] = np.random.normal(0, 2.5, np.sum(pulse_mask))

# Compile corrupted antenna raw bitstream transmission feed
received_signal = (pure_signal * attenuation_factor) + thermal_noise + radar_pulse_noise

# =====================================================================
# 3. COMPUTE SIGNAL-TO-NOISE RATIO (SNR) METRICS IN DECIBELS
# =====================================================================
print("\n📡 Processing incoming channel data stream blocks...")

# Calculate Mean Signal Power vs Mean Noise Power
signal_power = np.mean((pure_signal * attenuation_factor) ** 2)
noise_power = np.mean((thermal_noise + radar_pulse_noise) ** 2)

# SNR_dB = 10 * log10(Signal_Power / Noise_Power)
calculated_snr_db = 10 * np.log10(signal_power / noise_power)

print("\n--- 📶 WIRELESS TELEMETRY SPECTRUM STATUS LOG ---")
print(f"📊 Extracted Signal Power Matrix: {signal_power:.4f} W")
print(f"💥 Background Interference Power: {noise_power:.4f} W")
print(f"📡 Operational Signal-to-Noise Ratio: {calculated_snr_db:.2f} dB")

# Clinical Telemetry Boundary Assessment (Industry threshold requires SNR > 12 dB)
if calculated_snr_db <= 12.0:
    print("\n--- 🚨 CRITICAL TELEMETRY PACKET DISCONNECT DISPATCH ---")
    if environment_choice == "2":
        print("⚠️ FAILURE DIAGNOSIS: Structural attenuation breach. Install localized directional repeater AP array.")
    elif environment_choice == "3":
        print("⚠️ FAILURE DIAGNOSIS: External spectrum override. Reroute monitoring track to secondary backup WMTS channel.")
else:
    print("\n📶 Operational Channel Clearance Verified: Telemetry pipeline tracking loops stabilized.")

# =====================================================================
# 4. SPECTRAL SIGNAL PERFORMANCE WAVEFORM DISPLAY
# =====================================================================
print("\n📊 Compiling RF Signal Analytics Dashboard Display...")
plt.figure(figsize=(11, 6))

plt.plot(t, received_signal, color='#3498db', linewidth=1.0, label='Raw Receiver Antenna Feed Stream')
plt.plot(t, pure_signal * attenuation_factor, color='#2ecc71', linewidth=2.0, label='Extracted Modulated Data Carrier')

if environment_choice == "3":
    plt.fill_between(t, -4, 4, where=(radar_pulse_noise != 0), color='#e74c3c', alpha=0.15, label='Military Radar Blast Burst Zone')

plt.title(f'Clinical Telemetry RF Analysis: Wireless Channel Performance (Calculated SNR: {calculated_snr_db:.2f} dB)', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Receiver Data Frame Sampling Run (Seconds)', fontweight='bold')
plt.ylabel('Antenna Voltage Signal Amplitude (mV)', fontweight='bold')
plt.ylim(-4.5, 4.5)
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc='upper right')

# Seamless integration into KapoleiBioForge dark theme parameters
plt.gcf().patch.set_facecolor('#1e1e24')
plt.gca().set_facecolor('#2d2d35')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().title.set_color('white')
plt.gca().tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color('#44444e')

plt.tight_layout()
plt.show()
print("🏁 RF analysis cycle timeline finalized.")
