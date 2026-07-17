import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sqlite3

class MedTechSuiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Systems & Imaging Engineering Master Suite")
        self.root.geometry("750x820")
        self.root.configure(bg="#1e1e24")
        
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
        header = ttk.Label(main_frame, text="MEDTECH INTEGRATED ARCHITECTURE SYSTEMS CONTROL DECK", style="Header.TLabel")
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
        
        # 🔴 NEW PANEL 7: ECG DSP NOTCH FILTER
        p7_frame = ttk.LabelFrame(main_frame, text=" Project 7: ECG Electrical Hardware DSP Notch Filter ", padding="12")
        p7_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p7_frame, text="Simulates raw biometric millivolt heart rhythms corrupted by 60Hz power-line AC electromagnetic hum. Designs and applies an IIR Notch Filter to attenuate ambient interference noise.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p7_frame, text="Execute Signal Filtering & View DSP Waveforms", command=self.run_ecg_dsp_filter, style="Action.TButton").pack(anchor=tk.W)

        # PANEL 8: HIPAA CYBER-SECURITY STRIPPER
        p8_frame = ttk.LabelFrame(main_frame, text=" Project 8: Automated DICOM HIPAA Data Anonymizer ", padding="12")
        p8_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p8_frame, text="Scans directory paths for raw data payloads, intercepts rigid hexadecimal storage tags, strips personal metrics, and commits cryptographic hashed keys to isolated outputs.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        ttk.Button(p8_frame, text="Batch Sanitize Local DICOM Headers", command=self.run_anonymizer, style="Action.TButton").pack(anchor=tk.W)
        
        # PANEL 9: MILITARY EQUIPMENT CMMS DATABASE
        p9_frame = ttk.LabelFrame(main_frame, text=" Project 9: Relational Maintenance CMMS Database Logs ", padding="12")
        p9_frame.pack(fill=tk.X, pady=8)
        ttk.Label(p9_frame, text="Queries SQLite database backend tables tracking asset compliance profiles. Flags expiring high-risk assets and generates open corrective schedule backlog text modules.", wrap=650).pack(anchor=tk.W, pady=(0, 5))
        btn_layout = ttk.Frame(p9_frame)
        btn_layout.pack(anchor=tk.W)
        ttk.Button(btn_layout, text="Calculate Compliance & Open Work Orders", command=self.run_cmms_automation, style="Action.TButton").grid(row=0, column=0, padx=(0, 10))
        ttk.Button(btn_layout, text="View Database Schedule Logs", command=self.view_database_logs, style="Action.TButton").grid(row=0, column=1)

    # Subprocess execution bridges
    def run_ct_simulator(self):
        subprocess.Popen(["python3", "ct_simulator.py"])
        
    def run_thermal_simulator(self):
        messagebox.showinfo("Control Deck Alert", "Look at your active terminal screen to input exposure constants!")
        os.system("python3 xray_thermal_sim.py &")
        
    def run_dicom_pipeline(self):
        result = subprocess.run(["python3", "dicom_push.py"], capture_output=True, text=True)
        messagebox.showinfo("Network Return Log", result.stdout)
        
    def run_defib_analytics(self):
        subprocess.Popen(["python3", "defib_analytics.py"])

    def run_infusion_simulator(self):
        messagebox.showinfo("Control Deck Alert", "Look at your active terminal screen to configure fluid viscosity and line kinks!")
        os.system("python3 infusion_sim.py &")

    def run_ultrasound_simulator(self):
        subprocess.Popen(["python3", "ultrasound_sim.py"])

    def run_ecg_dsp_filter(self):
        subprocess.Popen(["python3", "ecg_dsp_filter.py"])
        
    def run_anonymizer(self):
        result = subprocess.run(["python3", "dicom_anonymizer.py"], capture_output=True, text=True)
        messagebox.showinfo("Sanitizer Return Log", result.stdout)
        
    def run_cmms_automation(self):
        result = subprocess.run(["python3", "asset_cmms.py"], capture_output=True, text=True)
        messagebox.showinfo("Automation Return Log", result.stdout)

    def view_database_logs(self):
        db_path = os.path.expanduser("~/ct_project/military_biomed_cmms.db")
        if not os.path.exists(db_path):
            messagebox.showerror("System Error", "Database not initialized. Run CMMS Automation first.")
            return
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT work_order_id, asset_id, order_type, status FROM work_orders")
        orders = cursor.fetchall()
        conn.close()
        
        log_win = tk.Toplevel(self.root)
        log_win.title("Live Work Order Registry Logs")
        log_win.geometry("500x300")
        log_win.configure(bg="#2d2d35")
        txt = tk.Text(log_win, bg="#2d2d35", fg="#ffffff", font=("Courier", 11), padding=10)
        txt.pack(fill=tk.BOTH, expand=True)
        txt.insert(tk.END, "--- LIVE WORK ORDER SCHEDULE LOGS ---\n\n")
