# Integrated Clinical Systems, Advanced Medical Imaging & Machine Learning Analytics Suite

A multi-disciplinary software engineering workspace integrating diagnostic imaging physics, fluid mechanics, acoustic signal processing, biological wave filtering, nuclear medicine math, healthcare IT network routing protocols, relational database management, data science, and custom application interface design. 

All independent modular sub-systems are fully unified, multi-threaded, and executable via a central terminal-native master control deck operator station (`suite_dashboard.py`).

---

## 🖥️ Architecture & Core Infrastructure

### Central Systems Control Deck Dashboard (`suite_dashboard.py`)
An interactive, terminal-native front-end console framework engineered using Python's standard shell interfaces. This console serves as an operational master station, orchestrating multi-threaded subprocess system bridges to cleanly trigger independent physical models, PACS transmissions, machine learning models, acoustic arrays, biological filtering, fluid dynamics, and live SQL database compliance metrics reports directly within the shell environment with zero phase or windowing lag.

### Continuous Integration & Operations
*   **`.github/workflows/`**: Automated Pylint workflow for strict Python code analysis, ensuring syntax validity, style compliance, and preventative bug catching across all sub-systems on every code push.
*   **`.gitignore`**: Optimized rule structures suppressing local operational artifacts, temporary python environment distributions (`__pycache__`), local database files, and system-specific text outputs.

---

## 🧠 Diagnostic Imaging & Medical Physics Simulations

### 1. CT Scanner Field Engineer Simulator (`ct_simulator.py`)
*   **Core Concept:** A diagnostic visualization simulation demonstrating how raw computed tomography data transforms into cross-sectional images, and how a physical hardware fault maps to a visual artifact. A single dead detector channel on a rotating CT gantry drops raw X-ray data across all 180 projection angles. While this looks like a flat vertical line in a raw Sinogram, the Filtered Back-Projection (FBP) algorithm maps this line into a perfect circle in the final image, known as a **Ring Artifact**.
*   **Systems Impact:** Enables field service engineers encountering a ring artifact on a clinical scan to instantly pull, clean, or swap that specific physical detector module index—dramatically reducing system downtime.

### 2. X-Ray Tube Thermodynamic & Safety Lockout Simulator (`xray_thermal_sim.py`)
*   **Core Concept:** A continuous-time physics simulation using Newton's Law of Cooling to model thermal accumulation and multi-compartment heat transfer inside advanced CT scanners. Models energy exchange between a low-mass, high-heat Anode Target Core and an oil-filled cooling bath housing structure. If single-slice exposures (calculated via the radiographic equation $HU = kV \times mA \times \text{seconds} \times 1.45$) breach an 85% safety boundary, the system engages an automated software safety lockout.
*   **Systems Impact:** Outputs a calculated exponential cooling decay countdown clock, simulating how modern clinical systems proactively prevent component destruction and anode warping.

### 3. Ultrasound Transducer Element Array Failure Analyzer (`ultrasound_sim.py`)
*   **Core Concept:** An acoustic signal processing simulation modeling radiofrequency (RF) backscatter echo profiles across complex multi-channel linear crystal arrays. Models waveform generation over a 128-element piezoelectric crystal array scanning a tissue structure with variations in density. Simulates structural crystal breakage (hard-faulting channels 45–52) to track wave attenuation and maps how broken channels distort image arrays through absolute envelope rectification and digital log-compression.
*   **Systems Impact:** Generates a real-time clinical B-mode scan demonstrating a distinct, sharp vertical acoustic dropout shadow artifact. This isolates physical probe crystal damage from internal backend electronics assembly issues.

### 4. Gamma Decoding Matrix Engine (`gamma_decoding_matrix.py`)
*   **Core Concept:** A nuclear medicine mathematical simulator calculating position decoding matrices for Gamma Cameras and PET scanners (such as Anger Logic calculations). It maps continuous light-distribution signals from a photomultiplier tube (PMT) array back into precise 2D spatial coordinates ($X, Y$) of individual photon scintillation events while correcting for non-linear crystal edge distortions.
*   **Systems Impact:** Validates detector positioning matrices, ensuring high spatial resolution and structural consistency for tumor localization scans.

---

## 🏥 Critical Care, Life Support & Biomechanical Modeling

### 5. Ventilator Pneumatic & Lung Mechanics Simulator (`ventilator_sim.py`)
*   **Core Concept:** A continuous time-series fluid dynamics simulator modeling respiratory mechanics. It solves equations of motion for the respiratory system ($P_{\text{aw}} = \frac{V}{C} + R \cdot Q$) to track continuous pressure, flow, and volume boundaries across changing lung compliance ($C$) and airway resistance ($R$) settings. Includes automated algorithms mapping barotrauma thresholds.
*   **Systems Impact:** Simulates real-time clinical ventilator waveforms and mechanical alerts (e.g., patient fighting the ventilator or circuit disconnects) to train automated feedback-loop software adjustments.

### 6. Infusion Pump Fluid Dynamics & Occlusion Simulator (`infusion_sim.py`)
*   **Core Concept:** Applies the Hagen-Poiseuille Law to track hydraulic pressure spikes across fluid pathways undergoing severe physical kinking deformations (0°–90°). Integrates dynamic fluid viscosity indexes (modeling saline solutions vs. high-density whole blood flows) to calculate the resulting mechanical counter-torque resistance metrics acting on internal peristaltic stepper motors.
*   **Systems Impact:** Models structural pressure waves moving down lines to intercept standard medical device alert margins (10 PSI limits). Automatically triggers safety sensor alarm routines and stalls internal motor tracking vectors to prevent downstream vascular tube failure.

### 7. Anesthesia Vaporizer Agent Concentration Simulator (`anesthesia_vaporizer_sim.py`)
*   **Core Concept:** A thermodynamic and partial-pressure fluid mixing application modeling the vapor output of liquid volatile anesthetic agents (e.g., Isoflurane, Sevoflurane) inside a bypassed carrier gas flow stream. Accounts for agent vapor pressure variants, temperature drops due to latent heat of vaporization, and variable carrier fresh gas flow rates.
*   **Systems Impact:** Models concentration fluctuations over time to test fail-safe mechanisms that prevent hypoxic gas mixtures or unintended agent overdose deliveries.

### 8. Dialysis Fluidics & Hemodialysis Transmembrane Simulator (`dialysis_sim.py`)
*   **Core Concept:** Models continuous mass transfer across a semipermeable hollow-fiber dialyzer membrane using counter-current flow mechanics. Tracks concentration gradients of blood urea nitrogen (BUN), creatinine, and electrolytes against dialysate fluids while continually adjusting Transmembrane Pressure (TMP) vectors to manage ultrafiltration rates.
*   **Systems Impact:** Simulates clinical blood purification curves and generates immediate warning flags if calculated TMP bounds predict dialyzer clotting or membrane rupture.

### 9. Closed-Loop Pacemaker Electronics Simulator (`pacemaker_sim.py`)
*   **Core Concept:** An electronic system simulator modeling an implantable cardiac pacemaker working in demand mode (e.g., VVI/DDD). Features a real-time state machine tracking sensing thresholds, refractory periods, and pacing capture outputs across adaptive heart-rate variations.
*   **Systems Impact:** Evaluates pacing response accuracy and power consumption metrics against variable cardiac signal inputs, verifying safety boundaries for continuous physiological monitoring.

### 10. Lab Robotics Automation & Pipette Kinematics Simulator (`lab_robotics_sim.py`)
*   **Core Concept:** A multi-axis kinematic simulation tracking automated high-throughput clinical laboratory pipetting assemblies. Maps joint velocities, positional trajectories, and fluid aspiration/dispensation forces across matrix sample trays to prevent fluid cross-contamination or mechanical collisions.
*   **Systems Impact:** Provides clear coordinate tracking optimizations to increase mechanical processing speeds and minimize mechanical stress on sample handling components.

---

## 📡 Signal Processing & Biometric DSP Engines

### 11. ECG Electrical Hardware DSP Notch Filter (`ecg_dsp_filter.py`)
*   **Core Concept:** Models a native human cardiac rhythm vector (generating synthetic P-QRS-T complex waves) heavily corrupted by an ambient 60Hz wall-power AC electromagnetic interference noise hum (0.6 mV amplitude distortion). Designs a tight mathematical digital IIR Notch Filter ($Q = 30$ constraints) combined with a zero-phase forward-backward `filtfilt` process.
*   **Systems Impact:** Successfully isolates and attenuates target power grid noise artifacts while safely preserving critical neighboring diagnostic biometric data coordinates. Outputs a 3-panel wave performance analysis layout.

### 12. PPG Adaptive Optoelectronic DSP Noise Canceller (`ppg_dsp_canceller.py`)
*   **Core Concept:** A biological wave processing engine focused on photoplethysmogram (PPG) signals. It utilizes adaptive filtering algorithms (such as Least Mean Squares - LMS) to cleanly separate primary cardiac blood volume pulse waves from massive motion artifacts and ambient light leakage waveforms captured by a surface photodiode sensor.
*   **Systems Impact:** Recovers highly accurate raw heart rate tracking coordinates from heavily distorted sensor readouts during intense patient physical movement profiles.

## 📡 Signal Processing & Biometric DSP Engines

### 13. SpO2 Optical Simulation & Tissue Absorption Model (`spo2_optical_sim.py`)
*   **Core Concept:** Establishes a highly detailed tissue spectrophotometry environment based on the Beer-Lambert Law. Models the AC/DC component absorption ratios of Red (660nm) and Infrared (940nm) light passing through pulsating capillary beds, tissue structures, and venous blood pools.
*   **Systems Impact:** Mathematically translates optical R-curves into precise blood oxygen saturation percentages ($\text{SpO}_2$), enabling calibration verification of pulse oximeter hardware arrays.

### 14. Radiofrequency (RF) Spectrum Analyzer Simulator (`rf_spectrum_analyzer.py`)
*   **Core Concept:** An RF communication engine that applies Fast Fourier Transforms (FFT) over broadband signals to monitor channel occupancy, power spectral densities, and signal-to-noise ratios (SNR). It introduces synthetic thermal noise, multi-path fading, and co-channel interference components.
*   **Systems Impact:** Allows engineers to simulate, detect, and isolate rogue telemetry emissions or device hardware leaks that could disrupt critical hospital wireless communication bands.

---

## 📊 Data Science, Machine Learning & Asset Operations

### 15. Critical Care Defibrillator Predictive Failure Analytics (`defib_analytics.py`)
*   **Core Concept:** A predictive data science track utilizing machine learning to project asset lifecycle metrics and proactively maintain emergency high-voltage performance thresholds. Utilizes Scikit-Learn (Linear Regression) to fit predictive models over time-series hardware degradation timelines. Models a degrading high-voltage capacitor charge leak dropping energy below safety standards ($200\text{ Joules} \pm 10$).
*   **Systems Impact:** Calculates the exact timeline intercept point where the asset will cross lower control limit safety specifications. Outputs real-time automated tech-dispatch alerts containing the calculated calendar cross-date.

### 16. Military-Grade Medical Asset CMMS Database Engine (`asset_cmms.py`)
*   **Core Concept:** An automated Computerized Maintenance Management System (CMMS) designed to optimize asset lifecycle upkeep, device risk classification, and preventive safety compliance. Engineered a relational database structure containing two coupled tracking logs: inventory metrics (serial numbers, facility clinics, risk levels) and active maintenance work schedules.
*   **Systems Impact:** Employs an automation algorithm that dynamically monitors upcoming safety expiration dates, compiling comprehensive risk-level summaries and maintenance histories for high-consequence healthcare facilities.

---

## 🛜 Healthcare IT, Cyber-Security & PACS Architecture

### 17. Hospital PACS & DICOM Network Node Pipeline (`pacs_server.py`, `dicom_push.py`)
*   **Core Concept:** A localized clinical network loopback architecture mimicking standard diagnostic transmission protocols and hospital server storage environments. Built an active background PACS Archive Node running a listener on port 4242 to process incoming healthcare data traffic. Paired it with a Modality Client simulator that programmatically generates valid digital medical images containing strict, mandatory DICOM metadata tags.
*   **Systems Impact:** Executed network handshakes to pass data packets via standard Verification (`C-ECHO`) and Storage (`C-STORE`) pipeline commands over the network loopback. This proves structural verification capability for hospital-wide clinical database integrations.

### 18. Automated DICOM HIPAA Data Privacy Anonymizer (`dicom_anonymizer.py`)
*   **Core Concept:** An automated healthcare cyber-security script built to isolate, mask, and re-code identifying metrics out of binary clinical medical studies. Recursively crawls storage directory paths to parse binary files. Targets specific hexadecimal tags protected under healthcare privacy parameters, including Patient Name `(0010,0010)`, Patient ID `(0010,0020)`, and Birth Date `(0010,0030)`.
*   **Systems Impact:** Wipes identifiable data, replaces personal identifiers with secure SHA-256 cryptographic hashes, and maps dates to wide safe demographic brackets. Saves outputs to secure isolated directories, allowing bulk processing for clinical trials without privacy non-compliance risks.

### 19. Medical Device Security Vulnerability Scanner (`device_security_scanner.py`)
*   **Core Concept:** An automated network security auditing engine specialized in profiling medical hardware interfaces. It scans targeted IP ranges for legacy/unencrypted healthcare protocols (e.g., raw HL7 over port 2575, unauthenticated DICOM over port 104, or legacy Telnet connections) and cross-references open ports against a database of known clinical firmware vulnerabilities.
*   **Systems Impact:** Generates a structured network risk landscape report, flagging critical, unencrypted communication pathways that require immediate firewall segmentation or TLS wrapping.

### 20. Hospital Wireless Network Bandwidth Monitor (`network_bandwidth_monitor.py`)
*   **Core Concept:** A discrete-event network traffic simulator tracking packet transmission latencies, queue depths, and data throughput bottlenecks across hospital local area networks. Simulates traffic prioritization configurations, explicitly analyzing how heavy bursts of PACS image routing impact real-time, low-bandwidth vital telemetry packet delivery streams.
*   **Systems Impact:** Validates network Quality of Service (QoS) rule allocations, proving that life-critical patient monitoring streams remain stable during heavy hospital-wide data movements.

### 21. Patient Telemetry Wireless RF Interference Suite (`vital_telemetry_suite.py`)
*   **Core Concept:** Connects physiological sensor physics (`SpO2` and pulse calculations) to a network simulation loop modeling random packet-drop margins across high-density hospital wireless access points undergoing severe ambient RF noise congestion.
*   **Systems Impact:** System runs real-time network loss monitoring loops. If network interference spikes past a 15% boundary limit, the software instantly triggers a clinical central monitoring station network safety alert.

---

## 📄 Financial & Administrative Operations

### 22. Clinical Financial Infrastructure & Invoice Processing (`Invoice_Honolulu_Diagnostic_Imaging.txt`)
*   **Core Concept:** A ledger system documenting administrative diagnostic operations, billing codes, technical service allocations, and device usage rates. It provides the financial template data used by the billing engines to reconcile operational engineering costs against facility clinical throughput.

### 23. Bioforge Billing Engine (`bioforge_billing.py`)
*   **Core Concept:** An administrative data system designed to parse operational medical logs, procedural codes, and equipment utilization runtimes into structured, insurance-compliant billing files.
*   **Systems Impact:** Automates institutional reconciliation workflows, minimizing manual claim preparation errors and bridging medical physics operations directly to institutional accounting ledgers.

### 24. Bioforge Freelance Engineering Tracker (`bioforge_freelance.py`)
*   **Core Concept:** A time, material, and resource tracking application built for independent biomedical and field service engineering consulting workloads. Manages contract rate sheets, field calibration hours, and parts tracking datasets.
*   **Systems Impact:** Generates professional engineering compliance reports and billing summaries, optimizing overhead tracking for outsourced healthcare technology groups.
## 🚀 Quick Start & Execution

### Prerequisites
*   **Operating System**: Windows 10/11, macOS, or Linux
*   **Runtime Environment**: Python 3.10 or higher
*   **Required Core Libraries**: `numpy`, `scipy`, `scikit-learn`, `pydicom`

### Installation & Workspace Setup

1. **Clone the Repository**  
   Open your terminal or command prompt and clone the workspace repository using Git:
   ```bash
   git clone https://github.com
   cd integrated-clinical-suite
   ```

2. **Initialize a Virtual Environment (Recommended)**  
   Isolate your project dependencies by creating and activating a clean virtual environment:
   ```bash
   # Create the virtual environment
   python -m venv venv

   # Activate on Windows (Command Prompt)
   venv\Scripts\activate
   
   # Activate on Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install Package Dependencies**  
   Install all mandatory mathematical, data science, and processing libraries needed by the underlying sub-systems:
   ```bash
   pip install --upgrade pip
   pip install numpy scipy scikit-learn pydicom
   ```

### Launching the Workspace Master Control Deck

To orchestrate, test, and run any of the independent physical models, network handlers, or digital signal processors from a unified station, execute the interactive, terminal-native master control console:

```bash
python suite_dashboard.py
```

### Verification & Testing
Upon launching `suite_dashboard.py`, you can test individual pipelines natively:
*   **PACS Pipeline**: Ensure port `4242` is open on your local interface before running `pacs_server.py`.
*   **Pylint Verifications**: Run local static analysis to confirm standard validation compliance parameters prior to tracking code modifications:
    ```bash
    pip install pylint
    pylint *.py
    ```
