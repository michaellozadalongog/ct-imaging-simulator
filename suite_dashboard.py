import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sqlite3

class MedTechSuiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Systems & Imaging Engineering Suite")
        self.root.geometry("700x550")
        self.root.configure(bg="#1e1e24")
        
        # Style Configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#1e1e24")
        style.configure("TLabel", background="#1e1e24", foreground="#ffffff", font=("Helvetica", 11))
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), foreground="#4a90e2")
        style.configure("Action.TButton", font=("Helvetica", 11, "bold"), foreground="#ffffff", background="#4a90e2", padding=6)
        
        # Main Layout Wrapper
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title Header
        header = ttk.Label(main_frame, text="MEDTECH CENTRAL SYSTEMS CONTROL DECK", style="Header.TLabel")
        header.pack(pady=(0, 20))
        
        # --------------------------------------------------------
        # PANEL 1: PROJECT 1 - SCANNER PHYSICS SIMULATOR
        # --------------------------------------------------------
        p1_frame = ttk.LabelFrame(main_frame, text=" Project 1: CT Scan Gantry Physics Simulator ", padding="15")
        p1_frame.pack(fill=tk.X, pady=10)
        p1_desc = ttk.Label(p1_frame, text="Executes a simulated Radon transform on a Shepp-Logan phantom, injects a dead detector channel anomaly (Channel 130), and runs an FBP reconstruction to output a distinct Ring Artifact plot side-by-side.", wrap=600)
        p1_desc.pack(anchor=tk.W, pady=(0, 10))
        p1_btn = ttk.Button(p1_frame, text="Run Gantry Physics Simulator & Generate Plot", command=self.run_ct_simulator, style="Action.TButton")
        p1_btn.pack(anchor=tk.W)
        
        # --------------------------------------------------------
        # PANEL 2: PROJECT 2 - PACS & DICOM NETWORKING NODE
        # --------------------------------------------------------
        p2_frame = ttk.LabelFrame(main_frame, text=" Project 2: DICOM PACS Server Network Pipeline ", padding="15")
        p2_frame.pack(fill=tk.X, pady=10)
        p2_desc = ttk.Label(p2_frame, text="Spuns up an internal DICOM listening node archive on port 4242 to intercept data traffic, generates a mock structural .dcm study, and triggers a C-STORE data network transmission loopback.", wrap=600)
        p2_desc.pack(anchor=tk.W, pady=(0, 10))
        p2_btn = ttk.Button(p2_frame, text="Launch Port 4242 Server & Transmit Scan Data", command=self.run_dicom_pipeline, style="Action.TButton")
        p2_btn.pack(anchor=tk.W)
        
        # --------------------------------------------------------
        # PANEL 3: PROJECT 3 - CLINICAL BIOMED ASSET CMMS
        # --------------------------------------------------------
        p3_frame = ttk.LabelFrame(main_frame, text=" Project 3: Relational Maintenance CMMS Database Logs ", padding="15")
        p3_frame.pack(fill=tk.X, pady=10)
        p3_desc = ttk.Label(p3_frame, text="Queries the SQLite relational backend tables tracking military hospital clinical assets. Automatically flags expiring high-risk inventory items and prints active open work schedules.", wrap=600)
        p3_desc.pack(anchor=tk.W, pady=(0, 10))
        
        btn_layout = ttk.Frame(p3_frame)
        btn_layout.pack(anchor=tk.W)
        p3_btn = ttk.Button(btn_layout, text="Calculate Compliance & Open Work Orders", command=self.run_cmms_automation, style="Action.TButton")
        p3_btn.grid(row=0, column=0, padx=(0, 10))
        p3_view_btn = ttk.Button(btn_layout, text="View Database Schedule Logs", command=self.view_database_logs, style="Action.TButton")
        p3_view_btn.grid(row=0, column=1)

    # Subprocess execution pipelines linking back to your completed code scripts
    def run_ct_simulator(self):
        try:
            messagebox.showinfo("Processing", "Compiling Shepp-Logan Sinogram matrix and running Filtered Back-Projection... Close the pop-up plot window to return to control deck.")
            subprocess.Popen(["python3", "ct_simulator.py"])
        except Exception as e:
            messagebox.showerror("System Error", f"Could not launch simulator: {str(e)}")

    def run_dicom_pipeline(self):
        try:
            # Re-running the push script safely establishes a fresh server connection and triggers transmission log prints
            script_path = os.path.expanduser("~/ct_project/dicom_push.py")
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)
            messagebox.showinfo("Network Pipeline Log Return", result.stdout)
        except Exception as e:
            messagebox.showerror("Network Error", f"Pipeline failed: {str(e)}")

    def run_cmms_automation(self):
        try:
            script_path = os.path.expanduser("~/ct_project/asset_cmms.py")
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)
            messagebox.showinfo("CMMS Automation Engine Return", result.stdout)
        except Exception as e:
            messagebox.showerror("Database Error", f"Automation execution failed: {str(e)}")

    def view_database_logs(self):
        db_path = os.path.expanduser("~/ct_project/military_biomed_cmms.db")
        if not os.path.exists(db_path):
            messagebox.showerror("Database Error", "Database file not initialized. Run CMMS Automation first.")
            return
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT work_order_id, asset_id, order_type, status FROM work_orders")
            orders = cursor.fetchall()
            conn.close()
            
            log_window = tk.Toplevel(self.root)
            log_window.title("Live Active Work Order Registry Logs")
            log_window.geometry("500x300")
            log_window.configure(bg="#2d2d35")
            
            txt = tk.Text(log_window, bg="#2d2d35", fg="#ffffff", insertbackground="white", padding=10, font=("Courier", 11))
            txt.pack(fill=tk.BOTH, expand=True)
            
            txt.insert(tk.END, "--- LIVE WORK ORDER SCHEDULE LOGS ---\n\n")
            for order in orders:
                txt.insert(tk.END, f"📋 Order #{order[0]} | Asset ID: {order[1]} | Type: {order[2]} | Status: {order[3]}\n")
            txt.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Database Read Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MedTechSuiteApp(root)
    root.mainloop()
