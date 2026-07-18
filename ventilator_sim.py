import numpy as np
import matplotlib.pyplot as plt

print("🫁 Critical Care Fluid Mechanics: Ventilator Solenoid Loop Engaged 🫁")

# =====================================================================
# 1. HARDWARE SYSTEM DESIGN CONFIGURATION
# =====================================================================
fs = 100.0                      # Transducer hardware polling frequency (100 Hz)
breath_duration = 5.0           # Single breath cycle length (5 seconds)
t = np.arange(int(breath_duration * fs)) / fs

TARGET_PRESSURE_CMH2O = 30.0    # Peak safe inspiratory target limit
PID_KP = 0.08                   # Proportional gain constant
PID_KI = 0.02                   # Integral error correction factor

# =====================================================================
# CLINICAL LUNG CONDITION CAPTURE
# =====================================================================
try:
    print("\n--- Configure Patient Lung Pathophysiology Matrix ---")
    print("1: Normal Healthy Lung Compliance (Elasticity)")
    print("2: Severe Acute Respiratory Distress Syndrome (Stiff ARDS Lungs)")
    scenario_choice = input("Select clinical scenario profile (1 or 2): ").strip()
    
    # Stiff lungs increase pressure generation exponentially
    lung_compliance = 15.0 if scenario_choice == "2" else 50.0
    airway_resistance = 15.0 if scenario_choice == "2" else 5.0
except ValueError:
    lung_compliance = 50.0
    airway_resistance = 5.0

# =====================================================================
# 2. RUN CLOSED-LOOP PNEUMATIC PID VALVE SIMULATION
# =====================================================================
airway_pressure_history = []
valve_aperture_history = []
integral_error = 0.0

print(f"\n💨 Starting ventilation cycle. Compliance Matrix: {lung_compliance} mL/cmH2O...")

for current_time in t:
    # Determine lifecycle stage: Inspiration (first 2 seconds) vs Expiration (last 3 seconds)
    if current_time <= 2.0:
        # 1. Calculate Target Physiological Flow Waveform Blueprint
        target_flow = 400.0 * np.sin(np.pi * current_time / 2.0)  # mL/s flow rate
        
        # 2. Compute Circuit Back-Pressure (Equation of Motion for Respiratory System)
        # Pressure = (Volume / Compliance) + (Flow * Resistance)
        simulated_volume = 400.0 * (1.0 - np.cos(np.pi * current_time / 2.0)) / (np.pi * 0.5)
        raw_airway_pressure = (simulated_volume / lung_compliance) + ((target_flow / 1000.0) * airway_resistance)
        
        # 3. Apply Feedback Loop: PID Solenoid Adjustments
        error = TARGET_PRESSURE_CMH2O - raw_airway_pressure
        integral_error += error * (1.0 / fs)
        valve_correction = (error * PID_KP) + (integral_error * PID_KI)
        
        # Clamp valve mechanical thresholds between 0% (closed) and 100% (fully open)
        valve_aperture = max(0.0, min(100.0, 50.0 + valve_correction))
        actual_pressure = raw_airway_pressure * (valve_aperture / 50.0)
        
    else:
        # Expiration Cycle: Solenoid shuts down, passive recoil drops pressure down to PEEP
        valve_aperture = 0.0
        decay_constant = 5.0
        actual_pressure = 5.0 + (airway_pressure_history[-1] - 5.0) * np.exp(-decay_constant * (current_time - 2.0))

    airway_pressure_history.append(actual_pressure)
    valve_aperture_history.append(valve_aperture)

# Check for Barotrauma Alert Flags
peak_pressure = max(airway_pressure_history)
if peak_pressure >= 35.0:
    print(f"\n🚨 [CRITICAL BAROTRAUMA ALARM: Airway Pressure reached {peak_pressure:.1f} cmH2O]")
    print("🛠️ SAFETY ACTION REQUIRED: Check circuit circuit paths for high-pressure line blockages.")

# =====================================================================
# 3. COMPILING GRAPH PERFORMANCE VISUALIZATION
# =====================================================================
print("📊 Compiling Pneumatic Solenoid Flow Diagnostic Curve Graphs...")
fig, ax1 = plt.subplots(figsize=(11, 6))

color = '#2ecc71'
ax1.set_xlabel('Ventilator Breath Timeline (Seconds)', fontweight='bold')
ax1.set_ylabel('Airway Circuit Pressure (cmH2O)', color=color, fontweight='bold')
line1 = ax1.plot(t, airway_pressure_history, color=color, linewidth=2.5, label='Airway Pressure Profile')
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(y=TARGET_PRESSURE_CMH2O, color='#e74c3c', linestyle='--', alpha=0.6, label='Safe Target Maximum (30 cmH2O)')
ax1.grid(True, linestyle=':', alpha=0.5)

ax2 = ax1.twinx()
color = '#9b59b6'
ax2.set_ylabel('Solenoid Valve Aperture Opening (%)', color=color, fontweight='bold')
line2 = ax2.plot(t, valve_aperture_history, color=color, linewidth=2.5, linestyle=':', label='Valve Throttle Aperture')
ax2.tick_params(axis='y', labelcolor=color)

lines = line1 + line2 + [plt.Line2D([0], [0], color='#e74c3c', linestyle='--')]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')

plt.title('Clinical Hardware Dynamics: Closed-Loop Ventilator Solenoid Pressure Control', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()

# Align formatting themes with KapoleiBioForge dark-mode brand layout profiles
plt.gcf().patch.set_facecolor('#1e1e24')
plt.gca().set_facecolor('#2d2d35')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().title.set_color('white')
plt.gca().tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color('#44444e')

plt.show()
print("🏁 Breath loop simulation complete.")
