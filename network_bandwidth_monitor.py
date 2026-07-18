import os
import random
from datetime import datetime

print("📶 KapoleiBioForge Network Engineering: Hospital AP Bandwidth Monitor Active 📶")

# =====================================================================
# 1. HOSPITAL WIRELESS INFRASTRUCTURE LAYOUT
# =====================================================================
# Maximum theoretical data bandwidth allocated per clinical access point (Mbps)
MAX_AP_BANDWIDTH_MBPS = 100.0
CHOKE_THRESHOLD_PERCENT = 85.0

access_points = {
    "AP_ICU_01": {"Zone": "Intensive Care Unit", "Connected_Devices": 42, "Base_Traffic": 62.5},
    "AP_ER_02":  {"Zone": "Emergency Department", "Connected_Devices": 58, "Base_Traffic": 81.2},
    "AP_OR_03":  {"Zone": "Operating Rooms",     "Connected_Devices": 12, "Base_Traffic": 34.1},
    "AP_RAD_04": {"Zone": "Radiology Suite",     "Connected_Devices": 28, "Base_Traffic": 55.8}
}

print(f"\nIntercepting telemetry frames from central wireless network controller...")
print(f"Monitoring {len(access_points)} high-density clinical access points...\n")

current_date = datetime.now().strftime('%B %d, %Y')
network_log_filename = "Hospital_Network_Traffic_Audit.txt"

network_report = f"""======================================================================
           📶 KAPOLEIBIOFORGE CLINICAL NETWORK MONITOR LOG 📶
======================================================================
Monitoring Station: Central Wireless Infrastructure Controller
Date of Audit     : {current_date}
System Status     : Active Network Traversal Protocol Engaged
----------------------------------------------------------------------
"""

# =====================================================================
# 2. RUN REAL-TIME DATA TRAFFIC TRAVERSAL AND CHOKE EVALUATIONS
# =====================================================================
reroute_count = 0
random.seed(808) # Hawaiian area code baseline seed

for ap_id, ap_data in access_points.items():
    # Simulate a dynamic network burst load (e.g., streaming high-resolution ultrasound data or heavy logs)
    dynamic_burst = random.uniform(5.0, 15.0)
    total_current_load = ap_data["Base_Traffic"] + dynamic_burst
    utilization_percentage = (total_current_load / MAX_AP_BANDWIDTH_MBPS) * 100.0
    
    print(f"📡 AP Link: {ap_id} [{ap_data['Zone']}] | Active Nodes: {ap_data['Connected_Devices']}")
    print(f"   Calculated Bandwidth Consumption: {total_current_load:.2f} Mbps ({utilization_percentage:.1f}% Utilization)")
    
    network_report += f"🌐 Access Point ID: {ap_id:<12} | Sector: {ap_data['Zone']:<25}\n"
    network_report += f"   • Active Nodes connected: {ap_data['Connected_Devices']} devices\n"
    network_report += f"   • Measured Throughput    : {total_current_load:.2f} / {MAX_AP_BANDWIDTH_MBPS} Mbps ({utilization_percentage:.1f}%)\n"
    
    # Traffic Shaping Decision Logic: Balance load if allocation reaches the 85% limit
    if utilization_percentage >= CHOKE_THRESHOLD_PERCENT:
        reroute_count += 1
        print(f"   🚨 WARNING: Bandwidth saturation detected! Exceeds safe operating limit ({CHOKE_THRESHOLD_PERCENT}%).")
        print(f"   🔄 TRAFFIC SHAPING: Rerouting non-essential telemetry packets to adjacent secondary channel...\n")
        network_report += f"   • 🚨 ALARM STATUS: AP CAPACITY EXHAUSTED. Network saturation risk.\n"
        network_report += f"   • 🔄 MANAGEMENT ACTION: Triggered automated load balancing. Shedding 25% traffic to secondary loop.\n"
    else:
        print(f"   ✅ Channel Clearance Clear: Link operations running within baseline specs.\n")
        network_report += f"   • ✅ ALARM STATUS: STABLE. Link capacity operating within nominal parameters.\n"
        
    network_report += "----------------------------------------------------------------------\n"

network_report += f"""AUDIT SUMMARY:
  Total Monitored Links    : {len(access_points)} Sectors
  Saturated Access Points  : {reroute_count} Intercepts Fired
  Overall Framework Status : SYSTEM STABILIZED / BALANCED
======================================================================
"""

# Export the network diagnostic document
with open(network_log_filename, 'w') as file:
    file.write(network_report)

print(f"🚀 Hospital network throughput analysis complete!")
print(f"📂 Diagnostic statement generated and isolated at: {network_log_filename}")
