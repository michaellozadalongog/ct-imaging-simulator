import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sqlite3

class MedTechSuiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Systems & Imaging Engineering Master Suite")
        self.root.geometry("750x850")
        self.root.configure(bg="#1e1e24")
        
        # --------------------------------------------------------
        # RISK MITIGATION: MANDATORY LEGAL DISCLAIMER POP-UP
        # --------------------------------------------------------
        disclaimer_text = (
            "⚠️ KAPOLEIBIOFORGE SYSTEMS ARCHITECTURE — LEGAL DISCLAIMER ⚠️\n\n"
            "This software suite is an engineering simulation, decision-support, and analytical data tool. "
            "It is NOT a medical device, nor has it been evaluated by the FDA or local regulatory bodies.\n\n"
            "1. NO CLINICAL LIABILITY: Under no circumstances shall KapoleiBioForge or its developers be held liable "
            "for any patient injury, hardware destruction, clinical downtime, or inaccurate diagnostic forecasting.\n"
            "2. REGULATORY INDEMNIFICATION: The automated DICOM HIPAA anonymization and database logging modules "
            "do not guarantee absolute legal privacy compliance. Final audit verification remains the sole "
            "responsibility of the clinical facility.\n"
            "3. NO REPLACEMENT FOR CERTIFIED BMETS: Final electrical calibration, fluid mechanics validation, and "
            "imaging physics tracking must always be verified physically by a certified Biomedical Equipment Technician "
            "(BMET) or Field Service Engineer using calibrated hardware analyzers.\n\n"
            "By clicking 'I Accept and Agree', you assume all operational risk and fully indemnify the developers."
        )
        
        # Show warning box before building the application panels
        agreement = messagebox.askokcancel("Mandatory Terms of Use & Liability Waiver", disclaimer_text)
        if not agreement:
            # Force close the application instantly if they refuse the liability terms
            self.root.destroy()
            return

        # Style Customization
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#1e1e24")
        style.configure("TLabel", background="#1e1e24", foreground="#ffffff", font=("Helvetica", 11))
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), foreground="#4a90e2")
        style.configure("Action.TButton", font=("Helvetica", 10, "bold"), foreground="#ffffff", background="#4a90e2", padding=4)
        
        # Scrollable Frame Wrapper Setup
        canvas = tk.Canvas(root, bg="#1e1e24", highlightthickness=0)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        main_frame = ttk.Frame(canvas, padding="20")
        
        main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=main_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Dashboard Title Header
        header = ttk.Label(main_frame, text="KAPOLEIBIOFORGE MASTER BUSINESS OPERATING STATION", style="Header.TLabel")
        header.pack(pady=(0, 20))
        
        # PANEL 1: CT SCAN PHYSICS
        p1_frame = ttk.LabelFrame(main_frame, text=" Project 1: CT Scan Gantry Physics Simulator ", padding="12")
        p1_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p1_frame, text="Executes a simulated Radon transform on a Shepp-Logan phantom, injects a dead detector channel anomaly (Channel 130), and runs an FBP reconstruction to output a distinct Ring Artifact plot side-by-side.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p1_frame, text="Run Gantry Physics Simulator & Generate Plot", command=self.run_ct_simulator, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 2: X-RAY THERMODYNAMICS
        p2_frame = ttk.LabelFrame(main_frame, text=" Project 2: X-Ray Tube Thermodynamic Simulator ", padding="12")
        p2_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p2_frame, text="Models real-time X-ray tube heat accumulation and cooling using Newton's Law of Cooling. Simulates automated safety lockouts and plots continuous dual-compartment dissipation curves.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p2_frame, text="Launch Thermal Physics Engine & Input Parameters", command=self.run_thermal_simulator, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 3: HOSPITAL PACS NETWORK
        p3_frame = ttk.LabelFrame(main_frame, text=" Project 3: DICOM PACS Server Network Pipeline ", padding="12")
        p3_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p3_frame, text="Spins up an internal DICOM listening node archive on port 4242 to intercept data traffic, generates a mock structural .dcm study, and triggers a C-STORE data network transmission loopback.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p3_frame, text="Launch Port 4242 Server & Transmit Scan Data", command=self.run_dicom_pipeline, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 4: PREDICTIVE ASSET DEFIB ML
        p4_frame = ttk.LabelFrame(main_frame, text=" Project 4: Critical Care Defibrillator Machine Learning Tracker ", padding="12")
        p4_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p4_frame, text="Tracks multi-device weekly performance telemetry metrics via scikit-learn. Fits a dynamic linear regression model over hardware decay to calculate precision component failure dates.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p4_frame, text="Execute Regression Training & Forecast Failures", command=self.run_defib_analytics, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 5: INFUSION PUMP FLUID MECHANICS
        p5_frame = ttk.LabelFrame(main_frame, text=" Project 5: Infusion Pump Fluid Dynamics & Sensor Occlusion Model ", padding="12")
        p5_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p5_frame, text="Applies the Hagen-Poiseuille equation to evaluate hydraulic pressure drops across kinked IV paths. Bridges fluid friction models directly to stepper motor counter-torque loads to trigger alert flags.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p5_frame, text="Launch Fluid Dynamics Console & Select Viscosity", command=self.run_infusion_simulator, style="Action.TButton").pack(anchor=tk.W)

        # PANEL 6: ULTRASOUND PIEZOELECTRIC FAULT ANALYZER
        p6_frame = ttk.LabelFrame(main_frame, text=" Project 6: Ultrasound Transducer Element Array Failure Analyzer ", padding="12")
        p6_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p6_frame, text="Models acoustic RF backscatter waveforms passing through a 128-element linear crystal matrix array. Injects dropped physical probe channels to render diagnostic vertical acoustic shadow artifacts.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p6_frame, text="Run Acoustic Array Model & Render B-Mode Scan", command=self.run_ultrasound_simulator, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 7: ECG DSP NOTCH FILTER
        p7_frame = ttk.LabelFrame(main_frame, text=" Project 7: ECG Electrical Hardware DSP Notch Filter ", padding="12")
        p7_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p7_frame, text="Simulates raw biometric millivolt heart rhythms corrupted by 60Hz power-line AC electromagnetic hum. Designs and applies an IIR Notch Filter to attenuate ambient interference noise.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p7_frame, text="Execute Signal Filtering & View DSP Waveforms", command=self.run_ecg_dsp_filter, style="Action.TButton").pack(anchor=tk.W)

        # PANEL 8: VITAL SIGNS & TELEMETRY NETWORK SIMULATOR
        p8_frame = ttk.LabelFrame(main_frame, text=" Project 8: Patient Telemetry Wireless RF Interference & Optical PPG Suite ", padding="12")
        p8_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p8_frame, text="Models arterial pulse hemodynamics via the Beer-Lambert Law to compute SpO2 levels. Injects simulated hospital environment RF network congestion to chart wireless packet loss.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p8_frame, text="Launch Telemetry Monitor Console & Select Environment", command=self.run_telemetry_suite, style="Action.TButton").pack(anchor=tk.W)

        # PANEL 9: HIPAA CYBER-SECURITY STRIPPER
        p9_frame = ttk.LabelFrame(main_frame, text=" Project 9: Automated DICOM HIPAA Data Anonymizer ", padding="12")
        p9_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p9_frame, text="Scans directory paths for raw data payloads, intercepts rigid hexadecimal storage tags, strips personal metrics, and commits cryptographic hashed keys to isolated outputs.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p9_frame, text="Batch Sanitize Local DICOM Headers", command=self.run_anonymizer, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 10: MILITARY EQUIPMENT CMMS DATABASE
        p10_frame = ttk.LabelFrame(main_frame, text=" Project 10: Relational Maintenance CMMS Database Logs ", padding="12")
        p10_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p10_frame, text="Queries SQLite database backend tables tracking asset compliance profiles. Flags expiring high-risk assets and generates open corrective schedule backlog text modules.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        btn_layout = ttk.Frame(p10_frame)
        btn_layout.pack(anchor=tk.W)
        ttk.Button(btn_layout, text="Calculate Compliance & Open Work Orders", command=self.run_cmms_automation, style="Action.TButton").grid(row=0, column=0, padx=(0, 10))
