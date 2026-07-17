import numpy as np
import matplotlib.pyplot as plt

print("📡 Vital Signs Optical Physics & Telemetry RF Interference Engine Online 📡")

# =====================================================================
# SYSTEM DESIGN CONFIGURATION
# =====================================================================
fs = 100.0          # Sampling rate of the patient monitor sensor (100 Hz)
duration = 5.0      # Data window capture time (5 seconds)
t = np.arange(int(duration * fs)) / fs

# Part 1 Constants: Beer-Lambert Law Optical Absorption Coefficients
AC_HEART_RATE_BPM = 72.0
SPO2_TARGET = 98.0  # Target blood oxygen saturation percentage

# Part 2 Constants: Hospital WiFi Telemetry Network Packet Constraints
TOTAL_PACKETS = int(duration * 10)  # 10 network packets transmitted per second
packet_timeline = np.linspace(0, duration, TOTAL_PACKETS)

# =====================================================================
# CLINICAL ENVIRONMENT CAPTURE
# =====================================================================
try:
    print("\n--- Configure Local Hospital Wireless & Patient Environment ---")
    print("1: Normal Hospital Floor (Low ambient RF Noise / Stable WiFi)")
    print("2: Heavy Interference Zone (High military radar bleed-through / Congested APs)")
    network_choice = input("Select clinical environment profile (1 or 2): ")
    
    rf_noise_amplitude = 0.8 if network_choice == "2" else 0.1
    drop_threshold = 0.45 if network_choice == "2" else 0.95
except ValueError:
    print("❌ Input Validation Error: Defaulting to stable baseline conditions.")
    rf_noise_amplitude = 0.1
    drop_threshold = 0.95

# =====================================================================
# PART 1: PHOTOPLETHYSMOGRAM (PPG) OPTICAL PHYSICS ENGINE
# =====================================================================
print("\n🩸 Modeling arterial pulse hemodynamics via the Beer-Lambert Law...")
# Generate a synthetic arterial pressure pulse wave
cardiac_frequency = AC_HEART_RATE_BPM / 60.0
pulse_wave = 0.5 * (1.0 + np.sin(2 * np.pi * cardiac_frequency * t))
# Add a dicrotic notch to simulate aortic valve closure back-pressure
pulse_wave += 0.15 * np.exp(-100 * ((t % (1/cardiac_frequency)) - 0.25)**2)

# Apply empirical absorption constants for Red (660nm) and Infrared (940nm) light
# Deoxygenated hemoglobin absorbs more Red; Oxygenated absorbs more Infrared
red_dc, red_ac = 1.2, 0.08 * (pulse_wave * (100.0 - SPO2_TARGET) / 10.0)
ir_dc, ir_ac = 1.5, 0.12 * (pulse_wave * SPO2_TARGET / 100.0)

# Total light intensity reaching the photodiode receptor
ppg_red_signal = red_dc - red_ac
ppg_ir_signal = ir_dc - ir_ac

# Reverse calculate SpO2 out of the signal to verify optical calibration accuracy
R = (red_ac / red_dc) / (ir_ac / ir_dc)
calculated_spo2 = 110 - 25 * R  # Standard linear calibration approximation curve
final_spo2 = np.mean(calculated_spo2)

print(f"✨ Optical Sensor Calibration: Calculated SpO2 Level: {final_spo2:.1f}%")

# =====================================================================
# PART 2: TELEMETRY RF WIRELESS INTERFERENCE MODEL
# =====================================================================
print("📡 Simulating RF packet transmission streams across hospital access points...")
np.random.seed(42)

# Generate a random probability vector modeling data transmission stability
network_noise_profile = np.random.uniform(0.0, 1.0, TOTAL_PACKETS)
packet_delivery_status = np.ones(TOTAL_PACKETS)

# Force packet drops where ambient RF noise overrides network reception limits
packet_delivery_status[network_noise_profile > drop_threshold] = 0.0
total_dropped = np.count_nonzero(packet_delivery_status == 0.0)
packet_loss_percentage = (total_dropped / TOTAL_PACKETS) * 100

print(f"📶 Real-Time Network Telemetry Analysis: Packet Loss: {packet_loss_percentage:.1f}%")

if packet_loss_percentage >= 15.0:
    print("\n--- 🚨 CENTRAL STATION NETWORK ALERT ---")
    print(f"⚠️ SYSTEM TIMEOUT: Patient Monitor lost connection packet threshold ({packet_loss_percentage:.1f}% Loss).")
    print("🛠️ ACTION REQUIRED: Clear local 2.4/5GHz spectrum blockages or swap wireless antenna assembly.")

# =====================================================================
# VISUAL SYSTEM WAVEFORM DISPLAY
# =====================================================================
print("\n📊 Compiling Vital Signs Control Layout Performance Dashboard...")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7))

# Plot 1: Optical PPG Physics Signal
ax1.plot(t, ppg_ir_signal, color='#e74c3c', linewidth=2, label='Infrared Absorption (940nm)')
ax1.plot(t, ppg_red_signal, color='#c0392b', linewidth=1.5, linestyle=':', label='Red Light Absorption (660nm)')
ax1.set_title(f"1. Optical PPG Sensor Hemodynamics Profile (Calculated Oxygen Saturation: {final_spo2:.1f}%)", fontweight='bold', color='white')
ax1.set_ylabel("Photodiode Intensity", fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='upper right')

# Plot 2: Wireless Network Packet Stream
markerline, stemlines, baseline = ax2.stem(packet_timeline, packet_delivery_status, linefmt='b-', markerfmt='bo', basefmt='w-')
plt.setp(markerline, 'color', '#3498db', 'markersize', 5)
plt.setp(stemlines, 'color', '#3498db', 'linewidth', 1)

# Highlight dropped indices visually
dropped_indices = np.where(packet_delivery_status == 0.0)[0]
if len(dropped_indices) > 0:
    ax2.scatter(packet_timeline[dropped_indices], np.zeros_like(dropped_indices), color='#e74c3c', s=45, zorder=5, label='Dropped Data Packet')
    ax2.legend(loc='lower right')

ax2.set_title(f"2. 608-614MHz Telemetry RF Transmission Pipeline ({packet_loss_percentage:.1f}% Total Packet Loss)", fontweight='bold', color='white')
ax2.set_xlabel("Time Duration (Seconds)", fontweight='bold')
ax2.set_ylabel("Packet Status (1=OK, 0=Drop)", fontweight='bold')
ax2.set_ylim(-0.2, 1.2)
ax2.grid(True, linestyle=':', alpha=0.3)

# Apply unified dark theme brand rules
for ax in [ax1, ax2]:
    ax.set_facecolor('#2d2d35')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#44444e')
plt.gcf().patch.set_facecolor('#1e1e24')

plt.tight_layout()
plt.show()
