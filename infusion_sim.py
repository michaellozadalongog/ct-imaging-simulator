import numpy as np
import matplotlib.pyplot as plt

print("💧 Infusion Pump Fluid Dynamics & Occlusion Simulation Engine Online 💧")

# =====================================================================
# SYSTEM DESIGN CONFIGURATION (Mechanical & Fluid Constants)
# =====================================================================
BASE_RADIUS_MM = 2.0         # Normal internal radius of standard IV PVC tubing
TUBE_LENGTH_M = 1.5          # Standard length of a clinical IV administration set
VOLUMETRIC_FLOW_ML_H = 250.0 # Target medication delivery rate (mL/hour)
MOTOR_EFFICIENCY = 0.85      # Stepper motor mechanical efficiency factor
SENSOR_LIMIT_PSI = 10.0      # Maximum safe pressure threshold before alarm trip

# Fluid Viscosity Constants (Pascal-seconds at body temperature)
VISCOSITY_SALINE = 0.0007    # Thin intravenous fluid/saline
VISCOSITY_BLOOD = 0.0035     # Thick whole blood / packed red cells

# Convert Flow Rate to standard SI Units (m^3 / second)
# 1 mL/h = 2.77778e-10 m^3/s
flow_rate_m3_s = VOLUMETRIC_FLOW_ML_H * 2.77778e-10

# =====================================================================
# CLINICAL PARAMETER CAPTURE
# =====================================================================
try:
    print("\n--- Configure Infusion Configuration Profiles ---")
    print("1: Standard Intravenous Saline (0.0007 Pa·s)")
    print("2: High-Viscosity Whole Blood Transfusion (0.0035 Pa·s)")
    fluid_choice = input("Select fluid viscosity profile (1 or 2): ")
    fluid_viscosity = VISCOSITY_BLOOD if fluid_choice == "2" else VISCOSITY_SALINE
    
    kink_percent = float(input("Enter severe IV line kink restriction percentage (0 to 90%): "))
    kink_percent = max(0.0, min(90.0, kink_percent)) # Clamp safety boundaries
except ValueError:
    print("❌ Input Validation Error: Defaulting to standard saline with a 60% partial kink profile.")
    fluid_viscosity = VISCOSITY_SALINE
    kink_percent = 60.0

print(f"\n🌊 Viscosity Set: {fluid_viscosity} Pa·s | Tubing Kink Profile: {kink_percent}% Restriction")

# =====================================================================
# DYNAMIC OPERATIONAL SIMULATION LOOP
# =====================================================================
time_steps = 60 # Model 60 seconds of real-time operational pumping timeline
time_history = []
pressure_psi_history = []
motor_torque_history = []
alarm_triggered = False
alarm_time = 0

print("\n⚙️ Commencing Infusion Fluid Delivery Cycle...")

for current_time in range(1, time_steps + 1):
    
    # Simulate a dynamic physical occlusion timeline: 
    # Tubing begins kinking progressively starting at second 15, reaching peak at second 25
    if current_time < 15:
        current_kink = 0.0
    elif current_time <= 25:
        # Linear progression from 0% up to the chosen restriction maximum
        current_kink = ((current_time - 15) / 10.0) * kink_percent
    else:
        current_kink = kink_percent
        
    # Calculate altered tube inner radius in meters based on the current kink deformation
    effective_radius_m = (BASE_RADIUS_MM * (1.0 - (current_kink / 100.0))) / 1000.0
    
    # 1. APPLY FLUID MECHANICS THEORY: The Hagen-Poiseuille Equation
    # Delta P = (8 * Viscosity * Length * FlowRate) / (pi * Radius^4)
    pressure_pascals = (8 * fluid_viscosity * TUBE_LENGTH_M * flow_rate_m3_s) / (np.pi * (effective_radius_m ** 4))
    
    # Convert Pascals to standard clinical diagnostic unit: PSI (1 Pascal = 0.000145038 PSI)
    pressure_psi = pressure_pascals * 0.000145038
    
    # 2. BRIDGING FLUID DYNAMICS TO ELECTROMECHANICAL TORQUE
    # As back-pressure builds, the stepper motor experiences resistance torque load (Newton-meters)
    # Torque = (Pressure * Displacement Volume per step) / Efficiency
    # Approximating standard Alaris-style linear peristaltic finger displacement volumes
    displacement_volume = 1.2e-7 
    torque_nm = (pressure_pascals * displacement_volume) / MOTOR_EFFICIENCY
    
    # 3. EVALUATE SENSOR THRESHOLD CRITERIA
    if pressure_psi >= SENSOR_LIMIT_PSI and not alarm_triggered:
        alarm_triggered = True
        alarm_time = current_time
        print(f"\n🚨 [CRITICAL OCCLUSION ALARM ENGAGED AT {current_time}s!]")
        print(f"⚠️ Internal Line Back-Pressure: {pressure_psi:.2f} PSI exceeds maximum safety threshold ({SENSOR_LIMIT_PSI} PSI)")
        print(f"⚡ Stepper Motor Counter-Torque load peaked: {torque_nm*1000:.2f} mNm. Motor stalled to prevent line burst.\n")

    time_history.append(current_time)
    pressure_psi_history.append(pressure_psi)
    motor_torque_history.append(torque_nm * 1000) # Convert to milli-Newton-meters for readable graphing

print("🏁 Operational cycle tracking finalized.")

# =====================================================================
# THE VISUAL MECHANICAL DIAGNOSTIC PLOT
# =====================================================================
print("📊 Compiling Electromechanical Flow Waveform Diagnostics Chart...")
fig, ax1 = plt.subplots(figsize=(11, 6))

# Primary Axis: Fluid Line Pressure Accumulation Data Plotting
color = '#e67e22'
ax1.set_xlabel('Operational Infusion Runtime (Seconds)', fontweight='bold')
ax1.set_ylabel('IV Line Back-Pressure (PSI)', color=color, fontweight='bold')
line1 = ax1.plot(time_history, pressure_psi_history, color=color, linewidth=2.5, label='Internal Line Pressure (PSI)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(y=SENSOR_LIMIT_PSI, color='#e74c3c', linestyle='--', alpha=0.7, label='Piezoelectric Sensor Alarm Trip Boundary')
ax1.grid(True, linestyle=':', alpha=0.6)

# Secondary Axis: Stepper Motor Counter-Torque Load Data Plotting
ax2 = ax1.twinx()
color = '#9b59b6'
ax2.set_ylabel('Stepper Motor Resistance Load (mNm)', color=color, fontweight='bold')
line2 = ax2.plot(time_history, motor_torque_history, color=color, linewidth=2.5, linestyle=':', label='Motor Torque Feedback (mNm)')
ax2.tick_params(axis='y', labelcolor=color)

# Structural highlighting indicators if an occlusion breach occurred
if alarm_triggered:
    ax1.axvline(x=alarm_time, color='#e74c3c', linestyle='-', alpha=0.5)
    ax1.text(alarm_time - 0.5, SENSOR_LIMIT_PSI * 0.4, 'Occlusion Alarm\nTrigger Point', color='#ffffff', 
             fontweight='bold', horizontalalignment='right', bbox=dict(facecolor='#e74c3c', alpha=0.8, boxstyle='round,pad=0.5'))

# Combine labels into a clean unified plot legend tracker box
lines = line1 + line2 + [plt.Line2D([0], [0], color='#e74c3c', linestyle='--')]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.title('Clinical Hardware Dynamics: Infusion Pump Line Occlusion Pressure & Motor Torque Profile', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()

# Match your personal dark theme brand guidelines
plt.gcf().patch.set_facecolor('#1e1e24')
plt.gca().set_facecolor('#2d2d35')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().title.set_color('white')
plt.gca().tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color('#44444e')

plt.show()
