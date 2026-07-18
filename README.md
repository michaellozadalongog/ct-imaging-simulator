# Integrated Clinical Systems, Advanced Medical Imaging & Machine Learning Analytics Suite

A multi-disciplinary software workspace integrating diagnostic imaging physics, fluid mechanics, acoustic signal processing, biological wave filtering, nuclear medicine math, healthcare IT network routing protocols, relational database management, data science, and custom application interface design.

All independent modular sub-systems are fully unified, multi-threaded, and executable via a central terminal-native master control deck operator station (`suite_dashboard.py`).

---

## 🖥️ Central Systems Control Deck Dashboard (`suite_dashboard.py`)
An interactive, terminal-native front-end console framework engineered using Python's standard shell interfaces. This console serves as an operational master station, orchestrating multi-threaded subprocess system bridges to cleanly trigger independent physical models, PACS transmissions, machine learning models, acoustic arrays, biological filtering, fluid dynamics, and live SQL database compliance metrics reports directly within the shell environment with zero phase or windowing lag.

---

## 🧠 Project 1: CT Scanner Field Engineer Simulator (`ct_simulator.py`)
A diagnostic visualization simulation demonstrating how raw computed tomography data transforms into cross-sectional images, and how a physical hardware fault maps to a visual artifact.

* **Core Concept:** A single dead detector channel on a rotating CT gantry drops raw X-ray data across all 180 projection angles. While this looks like a flat vertical line in a raw **Sinogram**, the **Filtered Back-Projection (FBP)** algorithm maps this line into a perfect circle in the final image, known as a **Ring Artifact**.
* **Systems Impact:** When field service engineers encounter a ring artifact on a clinical scan, they know instantly to pull, clean, or swap that specific physical detector module index—dramatically reducing system downtime.

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

## 📊 Project 4: Critical Care Defibrillator Predictive Failure Analytics (`defib_analytics.py`)
A predictive data science track utilizing machine learning to project asset lifecycle metrics and proactively maintain emergency high-voltage performance thresholds.

* **Core Concept:** Utilizes **Scikit-Learn (Linear Regression)** to fit predictive models over time-series hardware degradation timelines. Models a degrading high-voltage capacitor charge leak dropping energy below safety standards (200 Joules $\pm 10\%$).
* **Systems Impact:** Calculates the exact timeline intercept point where the asset will cross lower control limit safety specifications. Outputs real-time automated tech-dispatch alerts containing the calculated calendar cross-date, enabling proactive hardware swap-outs before clinical failure events.

---

## 💧 Project 5: Infusion Pump Fluid Dynamics & Mechanical Occlusion Simulator (`infusion_sim.py`)
A comprehensive mechanical system analysis leveraging fluid physics equations to evaluate back-pressure parameters and motor-torque threshold drift boundaries.

* **Core Concept:** Applies the **Hagen-Poiseuille Law** to track hydraulic pressure spikes across fluid pathways undergoing severe physical kinking deformations ($0-90\%$). Integrates dynamic fluid viscosity indexes (modeling saline solutions vs. high-density whole blood flows) to calculate the resulting mechanical counter-torque resistance metrics acting on internal peristaltic stepper motors.
* **Systems Impact:** Automatically models structural pressure waves moving down lines to intercept standard medical device alert margins ($10\text{ PSI}$ limits). Automatically triggers safety sensor alarm routines and stalls internal motor tracking vectors to simulate system shutdown procedures, preventing downstream vascular tube failure.

---

## 🧬 Project 6: Ultrasound Transducer Element Array Failure Analyzer (`ultrasound_sim.py`)
An acoustic signal processing simulation modeling radiofrequency (RF) backscatter echo profiles across complex multi-channel linear crystal arrays.

* **Core Concept:** Models waveform generation over a 128-element piezoelectric crystal array scanning a tissue structure with variations in density. Simulates structural crystal breakage (hard-faulting channels $45-52$) to track wave attenuation and maps how broken channels distort image arrays through absolute envelope rectification and digital log-compression.
* **Systems Impact:** Generates a real-time clinical B-mode scan demonstrating a distinct, sharp vertical acoustic dropout shadow artifact. This simulation enables field engineers to immediately verify probe mechanical element degradation, helping teams isolate physical probe crystal damage from internal backend electronics assembly issues.

---

## 🗄️ Project 7: ECG Electrical Hardware DSP Notch Filter (`ecg_dsp_filter.py`)
An electrical engineering signal processing track designing infinite impulse response (IIR) filtering systems to clean raw biometric data streams.

* **Core Concept:** Models a native human cardiac rhythm vector (generating synthetic P-QRS-T complex waves) heavily corrupted by an ambient 60Hz wall-power AC electromagnetic interference noise hum ($0.6\text{ mV}$ amplitude distortion). Designs a tight mathematical digital **IIR Notch Filter** ($Q=30$ constraints) combined with a zero-phase forward-backward `filtfilt` process.
* **Systems Impact:** Successfully isolates and attenuates target power grid noise artifacts while safely preserving critical neighboring diagnostic biometric data coordinates. Outputs a 3-panel wave performance analysis layout, demonstrating clinical hardware diagnostic filtering capabilities crucial for patient monitoring systems.

---

## 📡 Project 8: Patient Telemetry Wireless RF Interference & Optical PPG Suite (`vital_telemetry_suite.py`)
A comprehensive dual-discipline module fusing physiological sensor physics with wireless network communications performance modeling.

* **Core Concept:** Applies the **Beer-Lambert Law** of optical absorption across Red ($660\text{nm}$) and Infrared ($940\text{nm}$) spectrum paths to compute blood oxygen saturation ($\text{SpO}_2$) out of synthetic arterial pulse waves. Connects this device data to a network simulation loop modeling random packet-drop margins across high-density hospital wireless access points undergoing severe ambient RF noise congestion.
* **Systems Impact:** System runs real-time network loss monitoring loops. If network interference spikes past a $15\%$ boundary limit, the software instantly triggers a clinical central monitoring station network safety alert, allowing systems engineers to audit coverage mapping and isolate localized antenna assembly failures from environmental spectrum blocks.

---

## 🔒 Project 9: Automated DICOM HIPAA Data Privacy Anonymizer (`dicom_anonymizer.py`)
An automated healthcare cyber-security script built to isolate, mask, and re-code identifying metrics out of binary clinical medical studies.

* **Core Concept:** Recursively crawls storage directory paths to parse binary files. Targets specific hexadecimal tags protected under healthcare privacy parameters, including Patient Name `(0010,0010)`, Patient ID `(0010,0020)`, and Birth Date `(0010,0030)`. 
* **Systems Impact:** Wipes identifiable data, replaces personal identifiers with secure SHA-256 cryptographic hashes, and maps dates to wide safe demographic brackets. Saves outputs to secure isolated directories, allowing bulk processing for clinical trials without privacy non-compliance risks.

---

## 🗄️ Project 10: Military-Grade Medical Asset CMMS Database Engine (`asset_cmms.py`)
An automated Computerized Maintenance Management System (CMMS) designed to optimize asset lifecycle upkeep, device risk classification, and preventive safety compliance.

* **Core Concept:** Engineered a relational database structure containing two coupled tracking logs: inventory metrics (serial numbers, facility clinics, risk levels) and active maintenance work schedules. Built an automation algorithm that dynamically monitors upcoming safety expiration dates.
