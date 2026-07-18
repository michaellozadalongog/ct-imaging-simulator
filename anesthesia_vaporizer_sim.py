import numpy as np
import matplotlib.pyplot as plt

print("🧪 Clinical Thermodynamics: Anesthesia Vaporizer Agent Controller Active 🧪")

# =====================================================================
# 1. PHYSICAL HARWARE DESIGN CONSTANTS
# =====================================================================
fs = 20.0                         # Temperature sensor hardware polling rate (20 Hz)
duration = 30.0                   # Surgical window simulation run (30 seconds)
t = np.arange(int(duration * fs)) / fs

TARGET_TEMP_C = 20.0              # Fixed baseline temperature required for stable vapor pressure
AMBIENT_TEMP_C = 22.0             # Initial temperature of the surgical theater room

# Calibrated PID controller tuning coefficients
KP = 4.5                          # Proportional gain
KI = 0.8                          # Integral gain
KD = 0.2                          # Derivative gain

# =====================================================================
# SYSTEM HECOVERY PARAMETER MATRIX CAPTURE
# =====================================================================
try:
    print("\n--- Configure Anesthesia Gas Flow Delivery Scenarios ---")
    print("1: Standard Maintenance Flow Profile (Nominal agent evaporation drop)")
    print("2: High-Volume Trauma Flush (Severe, rapid latent heat vaporization drop)")
    flow_choice = input("Select clinical gas flow scenario (1 or 2): ").strip()
    
    latent_cooling_rate = 1.8 if flow_choice == "2" else 0.4
except ValueError:
    latent_cooling_rate = 0.4

# =====================================================================
# 2. RUN CLOSED-LOOP THERMODYNAMIC PID CONTROL LOOP
# =====================================================================
current_temp = AMBIENT_TEMP_C
temperature_history = []
heater_power_history = []

integral_error = 0.0
prev_error = 0.0

print(f"\n💨 Commencing surgical agent vaporization. Latent cooling gradient: -{latent_cooling_rate} °C/sec...")

for current_time in t:
    # 1. Compute Natural Physical Latent Heat Vaporization Loss
    # Temperature drops based on gas flow extraction velocity, but drifts back toward room ambient
    environmental_drift = (AMBIENT_TEMP_C - current_temp) * 0.02
    current_temp -= (latent_cooling_rate / fs) - (environmental_drift / fs)
    
    # 2. Compute PID Feedback System Error Calculations
    error = TARGET_TEMP_C - current_temp
    integral_error += error * (1.0 / fs)
    derivative_error = (error - prev_error) * fs
    prev_error = error
    
    # 3. Calculate Throttled Heating Element Power Output Response (Watts)
    # Clamp hardware limitations between 0.0W (off) and 100.0W (max capacity heater)
    heater_watts = (error * KP) + (integral_error * KI) + (derivative_error * KD)
    heater_watts = max(0.0, min(100.0, heater_watts))
    
    # Heat energy injection increases mass chamber temperature
    heat_injection_constant = 0.12
    current_temp += (heater_watts * heat_injection_constant) / fs
    
    temperature_history.append(current_temp)
    heater_power_history.append(heater_watts)

# Check for calibration drift warnings
min_temp = min(temperature_history)
if min_temp <= 17.5:
    print(f"\n🚨 [CRITICAL AGENT CONCENTRATION ALERT: Temperature dropped to {min_temp:.2f} °C]")
    print("⚠️  Vapor pressure unstable. Adjust gas flow rate or inspect heating cartridge lines.")
else:
    print("\n✅ Thermodynamic calibration loops verified stable. Agent delivery concentrations clear.")

# =====================================================================
# 3. SPECTRAL DUAL-AXIS TREND VISUALIZATION DISPLAY
# =====================================================================
print("📊 Compiling Vaporizer Performance Waveform Graphs...")
fig, ax1 = plt.subplots(figsize=(11, 6))

color = '#3498db'
ax1.set_xlabel('Surgical Vaporization Running Duration (Seconds)', fontweight='bold')
ax1.set_ylabel('Agent Chamber Temperature (°C)', color=color, fontweight='bold')
line1 = ax1.plot(t, temperature_history, color=color, linewidth=2.5, label='Chamber Temperature (°C)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(y=TARGET_TEMP_C, color='#2ecc71', linestyle='--', alpha=0.7, label='Target Spec Core (20.0 °C)')
ax1.set_ylim(15, 25)
ax1.grid(True, linestyle=':', alpha=0.4)

ax2 = ax1.twinx()
color = '#e67e22'
ax2.set_ylabel('Thermostatic Heater Power Element Load (Watts)', color=color, fontweight='bold')
line2 = ax2.plot(t, heater_power_history, color=color, linewidth=2.0, linestyle=':', label='PID Heater Output (W)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(-5, 105)

lines = line1 + line2 + [plt.Line2D([0], [0], color='#2ecc71', linestyle='--')]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right')

plt.title('Clinical Thermodynamic Systems: Closed-Loop Anesthesia Vaporizer Temperature Control', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()

# Align formatting themes directly into your dark brand style parameters
plt.gcf().patch.set_facecolor('#1e1e24')
plt.gca().set_facecolor('#2d2d35')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().title.set_color('white')
plt.gca().tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color('#44444e')

plt.show()
print("🏁 Thermal cycle run complete.")
