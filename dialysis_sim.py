import numpy as np
import matplotlib.pyplot as plt

print("🩸 Clinical Fluid Mechanics: Hemodialysis Peristaltic Pump Simulation Engine Online 🩸")

# =====================================================================
# 1. HARDWARE SYSTEM DESIGN CONFIGURATION
# =====================================================================
fs = 100.0                       # Sampling rate of the machine's internal pressure transducers (100 Hz)
duration = 15.0                  # Timeline tracking observation window (15 seconds)
t = np.arange(int(duration * fs)) / fs

PUMP_SPEED_RPM = 45.0            # Speed of the peristaltic roller pump assembly
ARTERIAL_LIMIT_MMHG = -250.0     # Maximum allowable vacuum/negative pressure before collapse
VENOUS_LIMIT_MMHG = 300.0        # Maximum allowable positive back-pressure before line rupture

# =====================================================================
# CLINICAL HARDWARE SCENARIO CAPTURE
# =====================================================================
try:
    print("\n--- Configure Hemodialysis Extrusion Failure Matrix ---")
    print("1: Normal Stable Dialysis Circuit Session")
    print("2: Severe Inflow Kink (Arterial Access Blockage)")
    print("3: High-Density Dialyzer Clotting (Venous Back-Pressure Spike)")
    scenario_choice = input("Select clinical simulation scenario (1, 2, or 3): ").strip()
except ValueError:
    scenario_choice = "1"

# =====================================================================
# 2. GENERATE CYCLICAL PERISTALTIC COMPRESSION WAVEFORMS
# =====================================================================
# Twin-roller pump generates 2 pressure pulses per mechanical revolution
pulse_frequency = (PUMP_SPEED_RPM / 60.0) * 2.0
base_pulsation = 15 * np.sin(2 * np.pi * pulse_frequency * t)

# Establish physiological baseline pressures inside the blood circuit loops
# Arterial line holds a slight vacuum; Venous line holds positive forward-flow pressure
arterial_baseline = -50.0 + base_pulsation
venous_baseline = 120.0 + base_pulsation

# =====================================================================
# 3. INJECT PROGRESSIVE HYDRAULIC PATHWAY FAULTS
# =====================================================================
arterial_pressure = arterial_baseline.copy()
venous_pressure = venous_baseline.copy()

alarm_triggered = False
alarm_time = 0.0
alarm_reason = ""

# Simulate progressive structural pathway failure vectors starting at second 4
for idx, current_time in enumerate(t):
    if current_time >= 4.0:
        progression_factor = min(1.0, (current_time - 4.0) / 6.0) # Peaks after 6 seconds of runtime
        
        if scenario_choice == "2":
            # Scenario 2: Arterial line kinks, creating a dangerous vacuum drop
            arterial_pressure[idx] += progression_factor * -250.0
            venous_pressure[idx] += progression_factor * -80.0  # Venous drops because fluid supply stops
        elif scenario_choice == "3":
            # Scenario 3: Dialyzer clots up, causing blood to back up massively into the venous sensor
            venous_pressure[idx] += progression_factor * 260.0
            arterial_pressure[idx] += progression_factor * 20.0

    # 4. EVALUATE EMERGENCY OVERRIDE SENSOR THRESHOLDS
    if not alarm_triggered:
        if arterial_pressure[idx] <= ARTERIAL_LIMIT_MMHG:
            alarm_triggered = True
            alarm_time = current_time
            alarm_reason = "🚨 CRITICAL ARTERIAL VACUUM FAILURE: Access Line Kinked/Collapsed."
        elif venous_pressure[idx] >= VENOUS_LIMIT_MMHG:
            alarm_triggered = True
            alarm_time = current_time
            alarm_reason = "🚨 CRITICAL VENOUS OVERPRESSURE: Dialyzer Filter Clotted/Occluded."

# =====================================================================
# 5. DIAGNOSTIC PERFORMANCE WAVEFORM DISPLAY
# =====================================================================
print("\n📊 Compiling Dialysis Circuit Hydraulic Trend Graphs...")
plt.figure(figsize=(11, 6))

plt.plot(t, venous_pressure, color='#3498db', linewidth=2, label='Venous Return Line Pressure')
plt.plot(t, arterial_pressure, color='#e67e22', linewidth=2, label='Arterial Draw Line Pressure')

# Overlay strict industry safety boundary thresholds
plt.axhline(y=VENOUS_LIMIT_MMHG, color='#e74c3c', linestyle='--', alpha=0.7, label='Venous High-Pressure Safety Boundary')
plt.axhline(y=ARTERIAL_LIMIT_MMHG, color='#e74c3c', linestyle='-.', alpha=0.7, label='Arterial Vacuum Limit Safety Boundary')

# If safety parameters were breached, execute visual lockout highlight indicators
if alarm_triggered:
    print(f"\n{alarm_reason}")
    print(f"🔒 SAFETY ACTION ENGAGED AT {alarm_time:.2f}s: Internal venous line clamps fired. Peristaltic motor stopped.")
    plt.axvline(x=alarm_time, color='#e74c3c', linestyle='-', linewidth=2.5)
    plt.text(alarm_time + 0.2, 50, f"SAFETY INTERCEPT\nTIME: {alarm_time:.2f}s\nMOTOR LOCKED DOWN", color='#ffffff', 
             fontweight='bold', bbox=dict(facecolor='#e74c3c', alpha=0.8, boxstyle='round,pad=0.5'))

plt.title('Clinical Fluid Dynamics: Hemodialysis Peristaltic Circuit Waveform Diagnostics', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Operational Session Timeline (Seconds)', fontweight='bold')
plt.ylabel('Fluid Circuit Pressure Metrics (mmHg)', fontweight='bold')
plt.ylim(-350, 420)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper right')

# Match your personal dark theme brand guidelines
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
print("🏁 Circuit wave cycle tracing complete.")
