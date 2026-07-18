import os
import sys

def print_header():
    os.system('clear')
    print("\033[94m======================================================================")
    print("         🧠 KAPOLEIBIOFORGE MASTER BUSINESS OPERATING STATION 🧠       ")
    print("======================================================================\033[0m")
    print("\033[93m⚠️  LEGAL INDEMNIFICATION BOUNDARY ACTIVE: decision-support simulation tool only. \033[0m\n")

def display_menu():
    print(" Select an Engineering Module or Business Asset to Execute:")
    print("----------------------------------------------------------------------")
    print(" [\033[92m1\033[0m]  Project 1: CT Scan Gantry Physics Ring Artifact Simulator")
    print(" [\033[92m2\033[0m]  Project 2: X-Ray Tube Continuous Thermodynamic Engine")
    print(" [\033[92m3\033[0m]  Project 3: Hospital PACS Server Archive Node Listener (Port 4242)")
    print(" [\033[92m4\033[0m]  Project 4: Modality Loopback Transmission Client (DICOM Push)")
    print(" [\033[92m5\033[0m]  Project 5: Defibrillator ML Time-Series Failure Forecaster")
    print(" [\033[92m6\033[0m]  Project 6: Infusion Pump Fluid Occlusion Motor-Torque Analyzer")
    print(" [\033[92m7\033[0m]  Project 7: Ultrasound Transducer 128-Element Crystal Failure Analyzer")
    print(" [\033[92m8\033[0m]  Project 8: ECG Electrical Hardware 60Hz Noise DSP Notch Filter")
    print(" [\033[92m9\033[0m]  Project 9: Patient Telemetry Wireless RF Interferences & SpO2 PPG Suite")
    print(" [\033[92m10\033[0m] Project 10: Secure HIPAA DICOM Hexadecimal Tag Data Anonymizer")
    print(" [\033[92m11\033[0m] Project 11: Relational Compliance Inventory Scheduling Database Logs")
    print(" [\033[92m12\033[0m] Project 12: SQLite Corporate SaaS Billing Ledger & Invoice Engine")
    print(" [\033[92m13\033[0m] Project 13: Pulse Oximeter PPG Motion Artifact DSP Canceller Engine")
    print(" [\033[92m14\033[0m] Project 14: Hemodialysis Peristaltic Pump Roller Pressure Model")
    print(" [\033[92m15\033[0m] Project 15: Gamma Camera Scintillation Crystal Position Matrix Decoder")
    print(" [\033[92m16\033[0m] Project 16: Ventilator Proportional Solenoid Valve PID Pneumatic Simulator")
    print(" [\033[92m17\033[0m] Project 17: Medical Telemetry RF Signal Spectrum Analyzer (SNR Monitor)")
    print(" [\033[92m18\033[0m] Project 18: Hospital Wi-Fi Medical Device Vulnerability Exploit Scanner")
    print(" [\033[92m19\033[0m] Project 19: Clinical Network Access Point Throughput Bandwidth Monitor")
    print(" [\033[92m20\033[0m] Project 20: Anesthesia Vaporizer Agent Concentration PID Thermal Controller")
    print(" [\033[92m21\033[0m] Project 21: Clinical Immunoassay Robotic Pipette X-Y-Z Gantry Stepper Analyzer")
    print(" [\033[92m22\033[0m] Project 22: AED Biphase Truncated Exponential (BTE) Discharge Waveform Generator")
    print("----------------------------------------------------------------------")
    print(" [\033[91m0\033[0m]  Exit Operational Control Station")
    print("----------------------------------------------------------------------")

def main():
    print_header()
    print("MANDATORY LEGAL TERMS OF USE & LIABILITY WAIVER:")
    print("This suite is an engineering decision-support tool. All outcomes must be")
    print("physically verified by a certified Biomedical Equipment Technician (BMET).")
    print("Under no circumstances shall the developer be liable for any patient injuries,")
    print("hardware destruction, or local facility compliance infractions.")
    
    agree = input("\nDo you accept these terms and conditions? (y/n): ").strip().lower()
    if agree != 'y':
        print("\033[91mTerms declined. Shutting down operational control pipelines.\033[0m")
        sys.exit()

    while True:
        print_header()
        display_menu()
        choice = input("\nEnter target index code selection (0-22): ").strip()
        
        print("\n\033[94m[⚙️  Executing Selected Architecture Stream... Close any pop-up plots to return]\033[0m\n")
        
        if choice == '1':
            os.system("python3 ct_simulator.py")
        elif choice == '2':
            os.system("python3 xray_thermal_sim.py")
        elif choice == '3':
            print("🚀 Launching Port 4242 PACS Node Archive. Press Ctrl+C inside that window to close.")
            os.system("python3 pacs_server.py")
        elif choice == '4':
            os.system("python3 dicom_push.py")
        elif choice == '5':
            os.system("python3 defib_analytics.py")
        elif choice == '6':
            os.system("python3 infusion_sim.py")
        elif choice == '7':
            os.system("python3 ultrasound_sim.py")
        elif choice == '8':
            os.system("python3 ecg_dsp_filter.py")
        elif choice == '9':
            os.system("python3 vital_telemetry_suite.py")
        elif choice == '10':
            os.system("python3 dicom_anonymizer.py")
        elif choice == '11':
            os.system("python3 asset_cmms.py")
        elif choice == '12':
            os.system("python3 bioforge_billing.py")
        elif choice == '13':
            os.system("python3 ppg_dsp_canceller.py")
        elif choice == '14':
            os.system("python3 dialysis_sim.py")
        elif choice == '15':
            os.system("python3 gamma_decoding_matrix.py")
        elif choice == '16':
            os.system("python3 ventilator_sim.py")
        elif choice == '17':
            os.system("python3 rf_spectrum_analyzer.py")
        elif choice == '18':
            os.system("python3 device_security_scanner.py")
        elif choice == '19':
            os.system("python3 network_bandwidth_monitor.py")
        elif choice == '20':
            os.system("python3 anesthesia_vaporizer_sim.py")
        elif choice == '21':
            os.system("python3 lab_robotics_sim.py")
        elif choice == '22':
            os.system("python3 defib_waveform_sim.py")
        elif choice == '0':
            print("\033[92mSafely disconnecting KapoleiBioForge data links. Goodbye!\033[0m")
            break
        else:
            print("\033[91m❌ Selection out of index boundaries. Retrying entry logic.\033[0m")
            
        input("\n\033[93mPress [Enter] to return to the Master Control Menu...\033[0m")

if __name__ == "__main__":
    main()
