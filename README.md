# CT Scanner Field Engineer Simulator (Python)

A diagnostic simulation demonstrating how raw computed tomography data transforms into cross-sectional images, and how a physical hardware fault maps to a visual artifact.

## Core Engineering Concept
A single dead detector channel on a rotating CT gantry drops raw X-ray data across all 180 projection angles. While this looks like a flat vertical line in a raw **Sinogram**, the **Filtered Back-Projection (FBP)** algorithm maps this line into a perfect circle in the final image, known as a **Ring Artifact**.

## Impact for Field Managers
When field service engineers encounter a ring artifact on a clinical scan, they can skip abstract troubleshooting. They know instantly to pull, clean, or swap that specific physical detector module module index—dramatically reducing system downtime.
