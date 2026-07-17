import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# SYSTEM DESIGN CONFIGURATION (Thermodynamic Constants)
# =====================================================================
MAX_ANODE_HU = 200000.0       # Maximum thermal limit of the Anode Target (Heat Units)
MAX_HOUSING_HU = 1500000.0    # Maximum thermal limit of the Protective Oil Housing
ANODE_COOLING_RATE = 0.04     # Newton's Law Cooling Coefficient (Anode to Housing)
HOUSING_COOLING_RATE = 0.005  # Newton's Law Cooling Coefficient (Housing to Room Air)

# Initial baseline temperatures at room equilibrium
anode_temp = 0.0   # Heat units present
housing_temp = 0.0 # Heat units present

time_history = []
anode_history = []
housing_history = []

print("⚡ X-Ray Tube Thermodynamic Simulation Engine Online ⚡")

# =====================================================================
# CLINICAL INPUT CAPTURE
# =====================================================================
try:
    print("\n--- Configure Scanner Radiographic Exposure Parameters ---")
    kv = float(input("Enter Tube Voltage (kV, e.g., 120): "))
    ma = float(input("Enter Tube Current (mA, e.g., 300): "))
    seconds = float(input("Enter Single Exposure Duration (s, e.g., 2): "))
    slices = int(input("Enter Total Trauma Sequence Slices (e.g., 40): "))
except ValueError:
    print("❌ Critical Input Validation Error: Defaulting to standard 120kV trauma protocols.")
    kv, ma, seconds, slices = 120.0, 300.0, 2.0, 40

# Compute incoming heat load per exposure slice using standard radiographic formulas
# Generator constant for high-frequency 3-Phase systems is 1.45
heat_per_slice = kv * ma * seconds * 1.45
print(f"🔥 Calculated Thermal Load per Slice Exposure: {heat_per_slice:,.1f} HU")

# =====================================================================
# THE DYNAMIC PHYSICS SIMULATION LOOP
# =====================================================================
current_time = 0
lockout_engaged = False
lockout_start_time = 0
lockout_duration = 0

print("\n🚀 Commencing Continuous CT Scan Acquisition Sequence...")

# Simulate 300 seconds of operational and cooling tracking timelines
for current_time in range(1, 301):
    
    # 1. Evaluate Exposure Event Constraints
    # Fire an exposure every 3 seconds if slices remain and system isn't locked out
    if slices > 0 and (current_time % 3 == 0) and not lockout_engaged:
        anode_temp += heat_per_slice
        slices -= 1
        print(f"[⏱️ Time: {current_time}s] Slice Fired! Remaining Backlog: {slices} | Anode Heat: {anode_temp:,.1f} HU")
    
    # 2. Apply Dual-Compartment Thermodynamics (Newton's Law of Cooling)
    # Anode loses heat directly into the surrounding cooling oil bath housing
    anode_to_housing_transfer = anode_temp * ANODE_COOLING_RATE
    anode_temp -= anode_to_housing_transfer
    housing_temp += anode_to_housing_transfer
    
    # Housing expels accumulated heat out into ambient environment room air
    housing_dissipation = housing_temp * HOUSING_COOLING_RATE
    housing_temp -= housing_dissipation
    
    # Safety boundary clamping to prevent zero-state mathematical drops
    anode_temp = max(anode_temp, 0.0)
    housing_temp = max(housing_temp, 0.0)
    
    # 3. Handle System Thermal Threshold Safety Logic
    # Trigger System Lockout if Anode exceeds safety margins (85% of Maximum Capacity)
    if anode_temp >= (0.85 * MAX_ANODE_HU) and not lockout_engaged:
        lockout_engaged = True
        lockout_start_time = current_time
        print(f"\n❌ [🚨 ERROR: THERMAL LOCKOUT ENGAGED AT {current_time}s!]")
        print(f"⚠️ Critical Anode Temperature reached: {anode_temp:,.1f} HU (Limit: {MAX_ANODE_HU:,.0f} HU)")
        
        # Calculate real-time cooling decay countdown targeting a safe 50% system threshold
        # Derived mathematically via inverted exponential cooling formulas
        lockout_duration = int(-np.log((0.50 * MAX_ANODE_HU) / anode_temp) / ANODE_COOLING_RATE)
        print(f"⏳ Cooling Fan Override Active. Safe state recovery countdown: {lockout_duration} Seconds Required.\n")
        
    # Disengage lockout once system cools down past the target safe threshold duration
    if lockout_engaged and (current_time >= lockout_start_time + lockout_duration):
        lockout_engaged = False
        print(f"\n✅ [⚙️ THERMAL LOCKOUT DISENGAGED AT {current_time}s]")
        print("📥 System cooling levels stabilized. Imaging track ready for operational backlog initialization.\n")

    # Record real-time states into metrics arrays for analytical tracking plots
    time_history.append(current_time)
    anode_history.append(anode_temp)
    housing_history.append(housing_temp)

# =====================================================================
# THE VISUAL PERFORMANCE DASHBOARD PLOT
# =====================================================================
print("\n📊 Compiling System Thermal Dissipation Dashboard Curve Graphs...")
fig, ax1 = plt.subplots(figsize=(11, 6))

# Primary Axis: Anode Heat Decay Data Plotting
color = '#e74c3c'
ax1.set_xlabel('Operational Sequence Runtime (Seconds)', fontweight='bold')
ax1.set_ylabel('Anode Target Heat Accumulation (HU)', color=color, fontweight='bold')
line1 = ax1.plot(time_history, anode_history, color=color, linewidth=2.5, label='Anode Target Core')
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(y=0.85*MAX_ANODE_HU, color='#c0392b', linestyle='--', alpha=0.7, label='85% Lockout Trip Threshold')
ax1.grid(True, linestyle=':', alpha=0.6)

# Secondary Axis: Housing Heat Transfer Data Plotting
ax2 = ax1.twinx()
color = '#3498db'
ax2.set_ylabel('Protective Housing / Oil Bath Heat Storage (HU)', color=color, fontweight='bold')
line2 = ax2.plot(time_history, housing_history, color=color, linewidth=2.5, linestyle='--', label='Oil Housing Compartment')
ax2.tick_params(axis='y', labelcolor=color)

# Combine labels into a clean unified plot legend tracker box
lines = line1 + line2 + [plt.Line2D([0], [0], color='#c0392b', linestyle='--')]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')

plt.title('Clinical Systems Physics: Dual-Compartment CT X-Ray Tube Thermal Profile', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
