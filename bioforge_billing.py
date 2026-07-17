import os
import sqlite3
from datetime import datetime

print("🪙 KapoleiBioForge Commercial SaaS Billing & Client Revenue Engine Online 🪙")

# =====================================================================
# 1. DATABASE CONFIGURATION & SAAS TRANSACTION LOGS
# =====================================================================
db_path = os.path.expanduser("~/ct_project/bioforge_commercial_billing.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create structured tables tracking client contracts and dynamic billing usage
cursor.execute('''
CREATE TABLE IF NOT EXISTS client_accounts (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    clinic_name TEXT UNIQUE NOT NULL,
    base_monthly_fee REAL NOT NULL,
    per_use_rate REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS usage_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    system_module TEXT NOT NULL,
    execution_volume INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(client_id) REFERENCES client_accounts(client_id)
)
''')
conn.commit()

# =====================================================================
# 2. SEED COMMERCIAL SAMPLE ACCOUNTS (Your Initial Client Backlog)
# =====================================================================
cursor.execute("DELETE FROM usage_logs;")
cursor.execute("DELETE FROM client_accounts;")

# Populate active freelance contracts on Oahu
cursor.execute("INSERT INTO client_accounts (clinic_name, base_monthly_fee, per_use_rate) VALUES ('Kapolei Urgent Care Center', 150.00, 0.75);")
cursor.execute("INSERT INTO client_accounts (clinic_name, base_monthly_fee, per_use_rate) VALUES ('Honolulu Diagnostic Imaging', 250.00, 1.25);")

# Log transactional usage metrics (simulating automated triggers when they click buttons in your app)
cursor.execute("INSERT INTO usage_logs (client_id, system_module, execution_volume, timestamp) VALUES (1, 'ECG_DSP_Filter', 120, '2026-07-10');")
cursor.execute("INSERT INTO usage_logs (client_id, system_module, execution_volume, timestamp) VALUES (1, 'DICOM_Anonymizer', 45, '2026-07-12');")
cursor.execute("INSERT INTO usage_logs (client_id, system_module, execution_volume, timestamp) VALUES (2, 'CT_Simulator_Physics', 85, '2026-07-15');")
cursor.execute("INSERT INTO usage_logs (client_id, system_module, execution_volume, timestamp) VALUES (2, 'Ultrasound_Array_Analyzer', 60, '2026-07-16');")
conn.commit()

# =====================================================================
# 3. CONVERGENT INVOICE AUTOMATION ENGINE
# =====================================================================
def generate_commercial_invoice():
    print("\n--- Active KapoleiBioForge Client Accounts ---")
    cursor.execute("SELECT client_id, clinic_name FROM client_accounts")
    accounts = cursor.fetchall()
    for acc in accounts:
        print(f"🆔 Client ID: {acc[0]} | Name: {acc[1]}")
        
    try:
        selected_id = int(input("\nSelect Client ID to process and invoice: "))
    except ValueError:
        print("❌ Error: Invalid identifier input selection.")
        conn.close()
        return

    # Query account contract specifications
    cursor.execute("SELECT clinic_name, base_monthly_fee, per_use_rate FROM client_accounts WHERE client_id = ?", (selected_id,))
    account_meta = cursor.fetchone()
    
    if not account_meta:
        print("❌ Error: Client profile not found in relational lookup tables.")
        conn.close()
        return
        
    clinic_name, base_fee, use_rate = account_meta
    
    # Calculate usage volume totals
    cursor.execute("SELECT system_module, SUM(execution_volume) FROM usage_logs WHERE client_id = ? GROUP BY system_module", (selected_id,))
    usage_data = cursor.fetchall()
    
    total_volume = sum(row[1] for row in usage_data) if usage_data else 0
    variable_cost = total_volume * use_rate
    gross_total = base_fee + variable_cost
    
    current_date = datetime.now().strftime('%B %d, %Y')
    invoice_filename = f"Invoice_{clinic_name.replace(' ', '_')}.txt"
    
    # Compile production-grade business deliverable receipt
    invoice_template = f"""======================================================================
                  💵 KAPOLEIBIOFORGE COMMERCIAL INVOICE 💵
======================================================================
Issuer: KapoleiBioForge Engineering Group
Contact: michaellozadalongog@gmail.com | Kapolei, HI
Date of Issue: {current_date}

Billed To:
  Facility Name: {clinic_name}
  Account Index Reference: KBF-00{selected_id}
----------------------------------------------------------------------
SYSTEM RESOURCE METRICS AUDIT LOGS:
"""
    if usage_data:
        for row in usage_data:
            invoice_template += f"  • Module: {row[0]:<30} | Audited Cycles: {row[1]:<5}\n"
    else:
        invoice_template += "  • No data processing usage logs generated in this billing cycle.\n"
        
    invoice_template += f"""----------------------------------------------------------------------
COMMERCIAL BILLING BREAKDOWN:
  Fixed Base Subscriptions Service Fee :  ${base_fee:,.2f}
  Dynamic API Usage Volume Total       :  {total_volume} Operations
  Variable Usage Computation Rate      :  ${use_rate:,.2f} / Operation
  Calculated Variable Surcharge        :  ${variable_cost:,.2f}
----------------------------------------------------------------------
🔥 TOTAL AMOUNT DUE NOW              :  ${gross_total:,.2f}
----------------------------------------------------------------------
Payment Terms: Net 30 days. Remit checks payable to KapoleiBioForge Group.
Thank you for your business! Keeping your clinical architecture online.
======================================================================
"""
    
    with open(invoice_filename, 'w') as file:
        file.write(invoice_template)
        
    print(f"\n🚀 Invoice compiled and generated perfectly!")
    print(f"📂 Client receipt saved directly to your workspace: {invoice_filename}")

if __name__ == "__main__":
    generate_commercial_invoice()
    conn.close()
