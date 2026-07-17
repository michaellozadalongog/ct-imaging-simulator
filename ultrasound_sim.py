import numpy as np
import matplotlib.pyplot as plt

print("🧬 Multi-Vendor Ultrasound Acoustic Simulation Engine Online 🧬")

# =====================================================================
# SYSTEM CONFIGURATION (Transducer Array Parameters)
# =====================================================================
NUM_ELEMENTS = 128            # Standard linear array transducer crystal count
SCAN_LINES = 128              # Number of acoustic scan lines in the raw vector frame
DEPTH_SAMPLES = 256           # Axial depth resolution samples per scan line

print(f"📊 Initializing Transducer Configuration: {NUM_ELEMENTS}-Element Piezoelectric Array...")

# =====================================================================
# SYNTHETIC CLINICAL ANATOMY TARGET INITIALIZATION
# =====================================================================
# Generate high-frequency acoustic backscatter representing underlying liver/tissue
np.random.seed(24)
tissue_backscatter = np.random.normal(0, 0.2, (DEPTH_SAMPLES, SCAN_LINES))

# Inject a highly echogenic circular tissue target (e.g., a fluid cyst or lesion focal boundary)
y_indices, x_indices = np.ogrid[:DEPTH_SAMPLES, :SCAN_LINES]
focal_mask = ((y_indices - 128) ** 2 + (x_indices - 64) ** 2) < 25 ** 2
tissue_backscatter[focal_mask] += 0.6  # Boost structural reflectivity

# =====================================================================
# PHYSICAL HARDWARE FAULT INJECTION (Broken Transducer Elements)
# =====================================================================
# Simulating a physical drop fault: Fracturing internal PZT crystals 45 to 52
print("🚨 Simulating Physical Drop Impact: Piezoelectric crystal fracture detected.")
print("⚠️ Hard-fault mapped to Transducer Channel Array Element Index: 45 through 52.")

hardware_element_status = np.ones(NUM_ELEMENTS)
hardware_element_status[45:53] = 0.0  # Wiping out signal transmission efficiency

# =====================================================================
# ACOUSTIC FIELD REFLECTION AND WAVEFORM SUMMATION
# =====================================================================
rf_ultrasound_frame = tissue_backscatter.copy()

# Apply the hardware array mask directly to the radiofrequency (RF) acoustic lines matrix
for line in range(SCAN_LINES):
    # Map scan line lines directly to corresponding physical channel elements
    if hardware_element_status[line] == 0.0:
        # Attenuate acoustic wave generation and return echoes by 95% due to dead elements
        rf_ultrasound_frame[:, line] *= 0.05

# =====================================================================
# DIGITAL B-MODE ENVELOPE DETECTION PROCESSING
# =====================================================================
# Apply a simple analytical absolute rectification to isolate reflection envelope intensities
envelope_frame = np.abs(rf_ultrasound_frame)

# Apply log-compression to match human vision mechanics and clinical monitor specifications
log_compressed_frame = 20 * np.log10(envelope_frame + 1e-5)

# Normalizing image boundaries for pixel grayscale display
log_compressed_frame -= np.min(log_compressed_frame)
log_compressed_frame /= np.max(log_compressed_frame)

# =====================================================================
# DIAGNOSTIC CLINICAL GRAPH RECOVERY DISPLAY
# =====================================================================
print("📊 Compiling Acoustic RF B-Mode Echogram Rendition...")
plt.figure(figsize=(10, 6))

plt.imshow(log_compressed_frame, cmap='gray', aspect='auto')

# Visual marker labeling the acoustic dropout boundaries
if np.any(hardware_element_status == 0.0):
    plt.axvline(x=45, color='#e74c3c', linestyle=':', alpha=0.6)
    plt.axvline(x=52, color='#e74c3c', linestyle=':', alpha=0.6)
    plt.text(48, 30, '⚠️ CRACKED PZT\nELEMENT DROPOUT\nARTIFACT SHADOW', color='#e74c3c', 
             fontsize=9, fontweight='bold', rotation=90, verticalalignment='top', horizontalalignment='center')

plt.title('Clinical Imaging Diagnostics: B-Mode Ultrasound Transducer Element Array Failure', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Transducer Lateral Array Channel Index (Elements 1-128)', fontweight='bold')
plt.ylabel('Axial Scan Depth Time-of-Flight Samples', fontweight='bold')

# Align template with your personal dark-mode profile brand aesthetics
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
