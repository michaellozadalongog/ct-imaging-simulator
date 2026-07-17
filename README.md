# Medical Systems Engineering, Clinical IT Networking & Analytics Suite

A multi-disciplinary software workspace integrating diagnostic imaging physics, healthcare IT network routing protocols, relational database management, and interactive application design. 

All distinct systems are fully unified and executable via a central visual master console (`suite_dashboard.py`).

---

## 🖥️ Central Systems Control Deck Dashboard (`suite_dashboard.py`)
An interactive desktop front-end graphical user interface (GUI) engineered using native Tkinter frameworks. This console serves as an operational master station, orchestrating multi-threaded subprocess system bridges to cleanly trigger independent physical models, PACS transmissions, and live SQL database compliance metrics reports in real-time.

---

## 🧠 Project 1: CT Scanner Field Engineer Simulator (`ct_simulator.py`)
A diagnostic visualization simulation demonstrating how raw computed tomography data transforms into cross-sectional images, and how a physical hardware fault maps to a visual artifact.

* **Core Concept:** A single dead detector channel on a rotating CT gantry drops raw X-ray data across all 180 projection angles. While this looks like a flat vertical line in a raw **Sinogram**, the **Filtered Back-Projection (FBP)** algorithm maps this line into a perfect circle in the final image, known as a **Ring Artifact**.
* **Systems Impact:** When field service engineers encounter a ring artifact on a clinical scan, they skip abstract troubleshooting. They know instantly to pull, clean, or swap that specific physical detector module module index—dramatically reducing system downtime.

---

## ⚡ Project 2: X-Ray Tube Thermodynamic & Safety Lockout Simulator (`xray_thermal_sim.py`)
A continuous-time physics simulation using Newton's Law of Cooling to model thermal accumulation and multi-compartment heat transfer inside advanced CT scanners.

* **Core Concept:** Models energy exchange between a low-mass, high-heat Anode Target Core and an oil-filled cooling bath housing structure. If single-slice exposures (calculated via the radiographic equation $\text{HU} = \text{kV} \times \text{mA} \times \text{seconds} \times 1.45$) breach an 85% safety boundary, the system engages an automated software safety lockout.
* **Systems Impact:** The engine instantly outputs a calculated exponential cooling decay countdown clock. This simulates exactly how modern clinical systems proactively prevent component destruction and anode warping, allowing field engineers to audit scanner utilization efficiency during high-capacity trauma workloads.

---

## 🏥 Project 3: Hospital PACS & DICOM Network Node Pipeline (`pacs_server.py`, `dicom_push.py`)
A localized clinical network loopback architecture mimicking standard diagnostic transmission protocols and hospital server storage environments.

* **Core Concept:** Built an active background PACS Archive Node running a listener on port 4242 to process incoming healthcare data traffic. Paired it with a Modality Client simulator that programmatically generates valid digital medical images containing strict, mandatory DICOM metadata tags.
* **Systems Impact:** Successfully executed network handshakes to pass data packets via standard **Verification (C-ECHO)** and **Storage (C-STORE)** pipeline commands over the network loopback. This proves structural verification capability for hospital-wide clinical database integrations.

---

## 🗄️ Project 4: Military-Grade Medical Asset CMMS Database Engine (`asset_cmms.py`)
An automated Computerized Maintenance Management System (CMMS) designed to optimize asset lifecycle upkeep, device risk classification, and preventive safety compliance.

* **Core Concept:** Engineered a relational database structure containing two coupled tracking logs: inventory metrics (serial numbers, facility clinics, risk levels) and active maintenance work schedules. Built an automation algorithm that dynamically monitors upcoming safety expiration dates.
* **Systems Impact:** System parses fleet records in real time, automatically flashes critical clinical maintenance alarms for near-term expiring items, and auto-generates formal 'Pending' preventive maintenance work orders—eliminating scheduling bottlenecks for life-support infrastructure.

---

## 🛠️ Local Development & Execution Setup
To clone this workspace, activate the isolated environment wrapper, and fire up the central application deck on your machine, run the following sequential terminal commands:

```bash
# Clone the repository
git clone https://github.com
cd ct-imaging-simulator

# Initialize and activate your virtual environment wrapper
python3 -m venv ct_env
source ct_env/bin/activate

# Install the specialized medical networking and imaging physics libraries
python3 -m pip install numpy matplotlib scikit-image pydicom pynetdicom

# Launch the master operator dashboard interface
python3 suite_dashboard.py
```
