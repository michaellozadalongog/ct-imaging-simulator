import numpy as np
import matplotlib.pyplot as plt

print("🫀 Active Implantable Systems: Demand Pacemaker Control Loop Online 🫀")

# =====================================================================
# 1. FIRMWARE & HARDWARE SAMPLING CONFIGURATION
# =====================================================================
fs = 200.0                      # Internal pacemaker micro-controller sampling rate (200 Hz)
duration = 8.0                  # Monitoring timeline sweep (8 seconds)
t = np.arange(int(duration * fs)) / fs

ESCAPE_INTERVAL_MS = 1000.0     # 1000ms escape interval (Equivalent to a lower pacing rate of 60 BPM)
SENSING_THRESHOLD_MV = 2.5      # R-wave detection sensitivity ceiling (2.5 millivolts)
PACING_PULSE_VOLTS = 5.0        # Constant voltage amplitude delivered when pacing fires

# =====================================================================
# PHYSIOLOGICAL PATHOLOGY MATRIX CAPTURE
# =====================================================================
try:
    print("\n--- Configure Patient Intrinsic Cardiac Rhythm ---")
    print("1: Intrinsic Normal Sinus Rhythm (Natural heart rate at 72 BPM)")
    print("2: Sudden Severe Bradycardia Event (Heart rate drops to 35 BPM at second 2.0)")
    rhythm_choice = input("Select patient physiological profile (1 or 2): ").strip()
except ValueError:
    rhythm_choice = "1"

# =====================================================================
# 2. GENERATE INTRACARDIAC VOLTAGE MATRIX FEED WITH FAULT CONDITIONS
# =====================================================================
intracardiac_signal = np.zeros_like(t)

# Program real-time timestamp arrays for intrinsic cardiac R-wave spikes
if rhythm_choice == "1":
    # Normal rhythm: heart beats naturally every 0.83 seconds (~72 BPM)
    heartbeat_timestamps = [0.4, 1.23, 2.06, 2.89, 3.72, 4.55, 5.38, 6.21, 7.04, 7.87]
else:
    # Bradycardia event: beats normally twice, then enters deep bradycardia (every 1.71 seconds / ~35 BPM)
    heartbeat_timestamps = [0.4, 1.23, 2.94, 4.65, 6.36, 8.07]

# Inject 3.5 mV intrinsic polarization R-waves into the voltage array
for beat in heartbeat_timestamps:
    idx = int(beat * fs)
    if idx < len(intracardiac_signal):
        intracardiac_signal[idx] = 3.5

# =====================================================================
# 3. RUN ACTIVE DEMAND PACING TIMING LOOPS & PULSE GENERATION
# =====================================================================
pacing_output = np.zeros_like(t)
timer_accumulated_ms = 0.0
sample_step_ms = (1.0 / fs) * 1000.0  # Time passed per single sample array index (5ms steps)

pacing_count = 0
inhibited_count = 0

print(f"\n⚡ Processing telemetry pipeline tracks. Lower rate boundary set at {60000/ESCAPE_INTERVAL_MS:.0f} BPM...")

for idx, current_time in enumerate(t):
    # Step the clock forward
    timer_accumulated_ms += sample_step_ms
    
    # 1. READ SENSING AMPLIFIER: Check if heart generates a natural R-wave past threshold
    if intracardiac_signal[idx] >= SENSING_THRESHOLD_MV:
        # INHIBIT ACTION: Intrinsic heartbeat sensed on time. Reset pacing countdown clock.
        timer_accumulated_ms = 0.0
        inhibited_count += 1
        
    # 2. EVALUATE ESCAPE TIMER OVERRIDE
    if timer_accumulated_ms >= ESCAPE_INTERVAL_MS:
        # PACE ACTION: Escape interval expired without sensing an R-wave. Deliver shock.
        pacing_output[idx] = PACING_PULSE_VOLTS
        pacing_count += 1
        
        # Reset internal clock after sending pacing pulse energy
        timer_accumulated_ms = 0.0

print("\n--- 🫀 IMPLANTED TELEMETRY DOWNLOAD REPORT ---")
print(f"📋 Monitored Timeline Duration: {duration:.1f} Seconds")
print(f" Sensed Intrinsic R-Waves: {inhibited_count} Signals Detected (Pacemaker Inhibited)")
print(f"⚡ Generated Pacing Pulses : {pacing_count} Active Spikes Delivered")

if pacing_count > 0:
    print("🔒 PACING ACTIVE: Patient bradycardia intercepted. Maintaining lower rate boundary specs.")
else:
    print("✅ PASSIVE INHIBIT: Patient cardiac conduction loops tracking within safe boundaries.")

# =====================================================================
# 4. SPECTRAL PACEMAKER TIMING VISUALIZATION DISPLAY
# =====================================================================
print("\n📊 Compiling Pacemaker Electrogram Timeline Charts...")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

# Panel 1: Intracardiac Sensing Channel
ax1.plot(t, intracardiac_signal, color='#2ecc71', linewidth=2.0, label='Intrinsic Intracardiac Signal (mV)')
ax1.axhline(y=SENSING_THRESHOLD_MV, color='#e67e22', linestyle='--', alpha=0.8, label=f'Sensing Amplifier Threshold ({SENSING_THRESHOLD_MV} mV)')
ax1.set_title('1. Intracardiac Lead Sensing Channel Feedback (Ventral Ventricular Lead)', fontweight='bold', color='white')
ax1.set_ylabel('Signal Potential (mV)', fontweight='bold')
ax1.set_ylim(-0.5, 4.5)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='upper right')

# Panel 2: Pacemaker Voltage Pulse Output Channel
ax2.plot(t, pacing_output, color='#e74c3c', linewidth=2.5, label='Pacemaker Pulse Output (Volts)')
ax2.set_title(f'2. Active Stimulus Pulse Generator Circuit Output Line ({pacing_count} Total Shocks)', fontweight='bold', color='white')
ax2.set_xlabel('Real-Time Run Duration Timeline (Seconds)', fontweight='bold')
ax2.set_ylabel('Pacing Stimulus (V)', fontweight='bold')
ax2.set_ylim(-0.5, 6.0)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.legend(loc='upper right')

# Seamless integration into KapoleiBioForge dark theme parameters
for ax in [ax1, ax2]:
    ax.set_facecolor('#2d2d35')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#44444e')
plt.gcf().patch.set_facecolor('#1e1e24')

plt.tight_layout()
plt.show()
print("🏁 Pacemaker micro-controller tracking loop finalized.")
