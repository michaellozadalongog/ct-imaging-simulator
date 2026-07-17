import numpy as np
import matplotlib.pyplot as plt
import skimage.transform  # Fixed: explicit import needed for resize
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon

# ==========================================
# STEP 2: Generate the Digital Phantom
# ==========================================
print("Generating Shepp-Logan Head Phantom...")
phantom = shepp_logan_phantom()
phantom = skimage.transform.resize(phantom, (256, 256))

# ==========================================
# STEP 3: Simulate Raw Data (Radon Transform)
# ==========================================
print("Simulating X-ray collection (Sinogram)...")
theta = np.linspace(0., 180., max(phantom.shape), endpoint=False)
# Fixed: added explicit circle=True to align with modern skimage defaults
sinogram = radon(phantom, theta=theta, circle=True) 

# ==========================================
# STEP 4: Inject Hardware Fault (Dead Channel)
# ==========================================
print("Simulating broken detector channel at index 130...")
corrupted_sinogram = sinogram.copy()
# This mimics a detector element reporting zero radiation through the full rotation
corrupted_sinogram[:, 130] = 0 

# ==========================================
# STEP 5: Reconstruct and Plot
# ==========================================
print("Reconstructing images...")
clean_reconstruction = iradon(sinogram, theta=theta, circle=True)
corrupted_reconstruction = iradon(corrupted_sinogram, theta=theta, circle=True)

print("Displaying results...")
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot normal operations
axes[0].imshow(clean_reconstruction, cmap='gray')
axes[0].set_title("Normal Scanner Operation\n(Clean Reconstruction)")
axes[0].axis('off')

# Plot the hardware fault
axes[1].imshow(corrupted_reconstruction, cmap='gray')
axes[1].set_title("Hardware Fault:\nRing Artifact (Detector 130)")
axes[1].axis('off')

plt.tight_layout()
plt.show()
