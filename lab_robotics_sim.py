import numpy as np
import matplotlib.pyplot as plt

print("🤖 Clinical Laboratory Automation: Gantry Stepper Motor Analyzer Active 🤖")

# =====================================================================
# 1. HARDWARE ROBOTICS CONFIGURATION
# =====================================================================
fs = 200.0                      # Internal encoder polling frequency (200 Hz)
duration = 3.0                  # Pipette travel vector execution time (3 seconds)
t = np.arange(int(duration * fs)) / fs

# Target position coordinates inside the immunoassay sample tray (mm)
TARGET_X, TARGET_Y, TARGET_Z = 150.0, 80.0, -50.0
ERROR_THRESHOLD_MM = 2.0        # Maximum allowable spatial divergence before emergency braking

# =====================================================================
# CLINICAL ENCLOSURE ENVIRONMENT SCENARIO CAPTURE
# =====================================================================
try:
    print("\n--- Configure Immunoassay Robotic Gantry Diagnostics ---")
    print("1: Normal Calibrated Path (Smooth sample fluid aspiration)")
    print("2: Mechanical Belt Slip / Stepper Motor Stall Anomaly")
    scenario_choice = input("Select laboratory scenario profile (1 or 2): ").strip()
except ValueError:
    scenario_choice = "1"

# =====================================================================
# 2. RUN CLOSED-LOOP STEPER MOTOR POSITION SIMULATION
# =====================================================================
# Programmatically calculate ideal linear gantry path trajectory lines
commanded_x = np.linspace(0, TARGET_X, len(t))
commanded_y = np.linspace(0, TARGET_Y, len(t))
commanded_z = np.linspace(0, TARGET_Z, len(t))

actual_x = commanded_x.copy()
actual_y = commanded_y.copy()
actual_z = commanded_z.copy()

brake_engaged = False
brake_time = 0.0
spatial_error_history = []

print(f"\n🦾 Commencing high-speed pipette gantry translation matrix loops...")

for idx, current_time in enumerate(t):
    if not brake_engaged:
        # Inject a mechanical belt slip hardware fault starting at second 1.2
        if scenario_choice == "2" and current_time >= 1.2:
            # Actual position begins stalling/drifting behind the commanded pulses
            stall_factor = max(0.0, (current_time - 1.2) / 1.8)
            actual_x[idx] -= stall_factor * 25.0
            actual_y[idx] -= stall_factor * 12.0
            actual_z[idx] += stall_factor * 8.0  # Pipette fails to descend deeply enough
            
        # 3. CLOSED-LOOP ENCODER TRACKING COMPARISON ALGORITHM
        # Compute absolute Euclidean error distance between Commanded and Actual positions
        spatial_error = np.sqrt(
            (commanded_x[idx] - actual_x[idx])**2 +
            (commanded_y[idx] - actual_y[idx])**2 +
            (commanded_z[idx] - actual_z[idx])**2
        )
        spatial_error_history.append(spatial_error)
        
        # Check if divergence breaches structural safety boundaries
        if spatial_error >= ERROR_THRESHOLD_MM:
            brake_engaged = True
            brake_time = current_time
            # Freeze all actual movements instantly at the moment of emergency braking
            actual_x[idx:] = actual_x[idx]
            actual_y[idx:] = actual_y[idx]
            actual_z[idx:] = actual_z[idx]
    else:
        # If brake is locked, path error remains locked at final value
        spatial_error_history.append(spatial_error_history[-1])

# Report operational safety metrics outcomes
if brake_engaged:
    print(f"\n🚨 [CRITICAL STEPPER STALL ALARM TRIP AT {brake_time:.3f}s]")
    print(f"⚠️  Gantry divergence reached {spatial_error_history[-1]:.2f} mm, breaching safe threshold ({ERROR_THRESHOLD_MM} mm).")
    print("🔒 EMERGENCY RECOVERY: Magnetic brakes energized. Fluid pump lines deactivated to prevent crash.")
else:
    print("\n✅ Path execution cleared. Pipette probe reached target sample well coordinates cleanly.")

# =====================================================================
# 3. KINEMATIC DIVERGENT WAVEFORM PLOT VISUALIZATION
# =====================================================================
print("📊 Compiling Lab Robotics Kinematics Analytics Dashboard Display...")
plt.figure(figsize=(11, 6))

plt.plot(t, commanded_x, color='#7f8c8d', linestyle='--', alpha=0.7, label='Commanded Pulse Vector (X)')
plt.plot(t, actual_x, color='#3498db', linewidth=2.5, label='Actual Encoder Position (X)')
plt.plot(t, spatial_error_history, color='#e74c3c', linewidth=2.0, label='Real-Time Spatial Path Error (mm)')

plt.axhline(y=ERROR_THRESHOLD_MM, color='#e74c3c', linestyle=':', label='Max Collision Margin Threshold (2mm)')

if brake_engaged:
    plt.axvline(x=brake_time, color='#e74c3c', linestyle='-', linewidth=2)
    plt.text(brake_time + 0.05, 50, f"EMERGENCY BRAKE\nLOCKDOWN ENGAGED\nTIME: {brake_time:.3f}s", color='#ffffff', 
             fontweight='bold', bbox=dict(facecolor='#e74c3c', alpha=0.8, boxstyle='round,pad=0.4'))

plt.title('Clinical Laboratory Robotics: Closed-Loop Gantry Stepper Motor Tracking & Collision Intercept', fontsize=11, fontweight='bold', pad=15)
plt.xlabel('Kinematic Execution Duration (Seconds)', fontweight='bold')
plt.ylabel('Spatial Motion Field Amplitude (mm)', fontweight='bold')
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc='upper left')

# Embed directly into your custom dark theme profile parameters
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
print("🏁 Robotics kinematics run complete.")
