import sqlite3
from datetime import datetime, timedelta

# ------------------------------------------------------------
# 1. DATABASE INITIALIZATION & SCHEMA
# ------------------------------------------------------------
print("🗄️ Initializing Military Biomed CMMS Database...")
conn = sqlite3.connect('military_biomed_cmms.db')
cursor = conn.cursor()

# Enable foreign keys for relational tracking
cursor.execute("PRAGMA foreign_keys = ON;")

# Create Table 1: Medical Assets Fleet Inventory
cursor.execute('''
CREATE TABLE IF NOT EXISTS medical_assets (
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number TEXT UNIQUE NOT NULL,
    device_name TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    model TEXT NOT NULL,
    risk_level TEXT CHECK(risk_level IN ('High', 'Medium', 'Low')),
    facility_clinic TEXT NOT NULL,
    last_pm_date TEXT NOT NULL,
    pm_interval_months INTEGER NOT NULL,
    next_pm_date TEXT
)
''')

# Create Table 2: Maintenance Log & Work Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS work_orders (
    work_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER,
    order_type TEXT CHECK(order_type IN ('Preventive', 'Corrective', 'Calibration')),
    status TEXT CHECK(status IN ('Pending', 'In Progress', 'Completed')),
    date_opened TEXT NOT NULL,
    date_closed TEXT,
    technician_notes TEXT,
    FOREIGN KEY (asset_id) REFERENCES medical_assets(asset_id)
)
''')

# ------------------------------------------------------------
# 2. POPULATE MOCK HOSPITAL FLEET DATA
# ------------------------------------------------------------
# Clear out old mock data if re-running script to prevent unique constraint blocks
cursor.execute("DELETE FROM work_orders;")
cursor.execute("DELETE FROM medical_assets;")

# Define modern mock assets found in military trauma units and operating spaces
mock_assets = [
    ('GE-AM-9921', 'Anesthesia Machine', 'GE HealthCare', 'Aisys CS2', 'High', 'Operating Room 1', '2026-01-15', 6),
    ('PH-MX-4402', 'Patient Monitor', 'Philips', 'IntelliVue MX550', 'Medium', 'ICU Bed 3', '2025-11-01', 12),
    ('ZLL-DF-8811', 'Defibrillator', 'Zoll', 'R Series', 'High', 'Emergency Dept', '2026-07-10', 6), # Expiring soon
    ('BD-IP-1102', 'Infusion Pump', 'BD Alaris', '8100 Module', 'Low', 'Pediatrics', '2025-08-20', 12)
]

# Calculate and bake next_pm_date dynamically before inserting
for asset in mock_assets:
    sn, name, manu, mod, risk, clinic, last_pm, interval = asset
    last_dt = datetime.strptime(last_pm, '%Y-%m-%d')
    # Rough approximation of adding calendar months
    next_dt = last_dt + timedelta(days=interval * 30.4)
    next_pm = next_dt.strftime('%Y-%m-%d')
    
    cursor.execute('''
    INSERT INTO medical_assets (serial_number, device_name, manufacturer, model, risk_level, facility_clinic, last_pm_date, pm_interval_months, next_pm_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (sn, name, manu, mod, risk, clinic, last_pm, interval, next_pm))

conn.commit()
print("✅ Database fleet populated with high-risk clinical inventory.")

# ------------------------------------------------------------
# 3. DISPATCHER AUTOMATION QUERIES
# ------------------------------------------------------------
print("\n🔍 Running Automation Queries: Tracking Expiring Assets within 30 days...")

# Mocking current date to July 17, 2026 to align with standard project timeline metrics
current_date_str = "2026-07-17"
current_dt = datetime.strptime(current_date_str, '%Y-%m-%d')
target_dt = current_dt + timedelta(days=30)
target_date_str = target_dt.strftime('%Y-%m-%d')

# Query A: Find assets needing immediate scheduling review
cursor.execute('''
SELECT asset_id, device_name, facility_clinic, next_pm_date 
FROM medical_assets 
WHERE next_pm_date <= ?
ORDER BY next_pm_date ASC
''', (target_date_str,))

flagged_assets = cursor.fetchall()

print("\n--- CLINICAL PM ALERT FLASH ---")
for row in flagged_assets:
    print(f"⚠️ ASSET ID {row[0]}: {row[1]} in {row[2]} requires maintenance by {row[3]}!")

# Query B: Auto-generate Pending Work Orders for flagged equipment
for row in flagged_assets:
    asset_id = row[0]
    cursor.execute('''
    INSERT INTO work_orders (asset_id, order_type, status, date_opened)
    VALUES (?, 'Preventive', 'Pending', ?)
    ''', (asset_id, current_date_str))

conn.commit()
print(f"\n⚡ Success: Automated work orders opened for {len(flagged_assets)} expiring medical device(s).")

# Quick verification print out of active pending backlog logs
cursor.execute("SELECT work_order_id, asset_id, order_type, status FROM work_orders")
print("\n--- LIVE WORK ORDER SCHEDULE LOGS ---")
for order in cursor.fetchall():
    print(f"📋 Order #{order[0]} | Asset ID: {order[1]} | Type: {order[2]} | Status: {order[3]}")

conn.close()
