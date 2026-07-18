import numpy as np
import matplotlib.pyplot as plt

print("🩸 Optical Physics Systems: SpO2 Multi-Wavelength R-Curve Calibration Engine Online 🩸")

# =====================================================================
# 1. OPTICAL SAMPLING FRAMEWORK SETUP
# =====================================================================
fs = 125.0                      # Optical photodiode ADC polling rate (125 Hz)
duration = 4.0                  # Vital window pulse observation frame (4 seconds)
t = np.arange(int(duration * fs)) / fs

# Known physical light absorption coefficients (Molar Extinction Coefficients)
ABS_RED_HB  = 0.82; ABS_RED_HBO2  = 0.08  # Deoxygenated absorbs 10x more Red
ABS_IR_HB   = 0.20; ABS_IR_HBO2   = 0.36  # Oxygenated absorbs nearly 2x more Infrared

# =====================================================================
# CLINICAL PHYSIOLOGY ARTERIAL SATURATION PATHOLOGY SELECTION
# =====================================================================
try:
    print("\n--- Configure Patient Arterial Blood Oxygenation States ---")
    print("1: Normal Healthy Oxygenation Profile (Target SpO2: ~98%)")
    print("2: Critical Hypoxia Event (Target SpO2: ~75% - Emergency Operating Room Cyanosis)")
    state_choice = input("Select patient physiological state (1 or 2): ").strip()
    
    true_saturation = 0.98 if state_choice == "1" else 0.75
except ValueError:
    true_saturation = 0.98

# Simulate a clean arterial pulse volume change (Photoplethysmogram wave shape)
cardiac_pulse = 0.4 * (1.0 + np.sin(2 * np.pi * 1.2 * t)) + 0.1 * np.sin(4 * np.pi * 1.2 * t)

# =====================================================================
# 2. APPLICATION OF THE BEER-LAMBERT LAW TO PHOTODIODE DATA VOLTAGES
# =====================================================================
# Calculate composite multi-component path absorption coefficients based on patient saturation
total_absorption_red = (true_saturation * ABS_RED_HBO2) + ((1.0 - true_saturation) * ABS_RED_HB)
total_absorption_ir  = (true_saturation * ABS_IR_HBO2) + ((1.0 - true_saturation) * ABS_IR_HB)

# Baseline Tissue / Venous background Direct Current light level (DC component)
RED_DC_BASELINE = 1.80
IR_DC_BASELINE  = 2.20

# Alternating Current heart pulse absorption swings (AC component)
# Transmitted light is an inverse function of absorption: Intensity = Baseline - PulseDelta
raw_red_voltage = RED_DC_BASELINE - (cardiac_pulse * total_absorption_red * 1.5)
raw_ir_voltage  = IR_DC_BASELINE - (cardiac_pulse * total_absorption_ir * 1.2)

# =====================================================================
# 3. EXTRACTION OF AC/DC RATIOS & CALIBRATION MATRIX LOOKUPS
# =====================================================================
print("\n🔬 Processing multi-channel photodiode telemetry stream frames...")

# Extract components programmatically using max/min tracking to capture peak pulse parameters
red_ac = np.max(raw_red_voltage) - np.min(raw_red_voltage)
red_dc = np.mean(raw_red_voltage)

ir_ac = np.max(raw_ir_voltage) - np.min(raw_ir_voltage)
ir_dc = np.mean(raw_ir_voltage)

# Calculate the final "Ratio of Ratios" (R-Value Parameter)
# R = (AC_Red / DC_Red) / (AC_IR / DC_IR)
R_value = (red_ac / red_dc) / (ir_ac / ir_dc)

# Apply industrial calibrated linear empirical R-Curve Look-Up Equation
# Standard hardware calibration approximation formula: SpO2 = A - B * R
calibrated_spo2_percent = 110.0 - (25.0 * R_value)

print("\n--- 📶 PULSE OXIMETER CALIBRATION CALCULATION REPORT ---")
print(f"🔴 Red Channel   : AC Mod = {red_ac:.4f} V | DC Base = {red_dc:.4f} V")
print(f"🟤 Infrared Chan : AC Mod = {ir_ac:.4f} V | DC Base = {ir_dc:.4f} V")
print(f"🎛️  Computed R-Value Matrix Ratio: {R_value:.4f}")
print(f"🩸 Reconstructed Clinical SpO2 : {calibrated_spo2_percent:.2f}% Saturation Checked.")

# Evaluate accuracy tolerances compared to industrial target guidelines
if calibrated_spo2_percent <= 85.0:
    print("\n--- 🚨 CRITICAL LOW SPO2 RESPIRATORY HYPOXIA ALARM ---")
    print("⚠️  SYSTEM WARNING: Severe blood oxygen depletion detected. Verify target ventilation sensor path lines.")
else:
    print("\n📶 Operational Saturation Tolerances Safe: Physiological target metrics tracking stable.")

# =====================================================================
# 4. OPTICAL PHOTOPLETHYSMOGRAM DISIPLAY WAVEFORM GRAPHING
# =====================================================================
print("\n📊 Compiling Multi-Wavelength Photodiode Signal Analytics Dashboard...")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

ax1.plot(t, raw_red_voltage, color='#e74c3c', linewidth=2.0, label='Red Light Absorption Feed (660nm)')
ax1.set_title(f'1. Red Channel Photodiode Output Stream (AC Peak-to-Peak Delta: {red_ac:.4f} V)', fontweight='bold', color='white')
ax1.set_ylabel('Receiver Output (V)', fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='upper right')

ax2.plot(t, raw_ir_voltage, color='#9b59b6', linewidth=2.0, label='Infrared Light Absorption Feed (940nm)')
ax2.set_title(f'2. Infrared Channel Photodiode Output Stream (AC Peak-to-Peak Delta: {ir_ac:.4f} V)', fontweight='bold', color='white')
ax2.set_xlabel('Sensor Acquisition Duration Frame Timeline (Seconds)', fontweight='bold')
ax2.set_ylabel('Receiver Output (V)', fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.legend(loc='upper right')

# Seamless integration into KapoleiBioForge dark theme layout templates
for ax in [ax1, ax2]:
    ax.set_facecolor('#2d2d35')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#44444e')
plt.gcf().patch.set_facecolor('#1e1e24')

plt.suptitle(f'Clinical Optical Systems: Multi-Wavelength Beer-Lambert Pulse Oximeter Calibration\nReconstructed System Vital Metric -> Calculated SpO2 Level: {calibrated_spo2_percent:.1f}%', fontsize=12, fontweight='bold', color='white', y=0.98)
plt.tight_layout()
plt.show()
print("🏁 Optical analytics matrix computation finalized.")
