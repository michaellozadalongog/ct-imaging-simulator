import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("⚡ Defibrillator Predictive Calibration Analytics Engine Online ⚡")

# =====================================================================
# 1. GENERATE TIME-SERIES HARDWARE DRIFT DATASETS
# =====================================================================
np.random.seed(42)
start_date = datetime(2025, 1, 1)
weeks = 80  # ~18 months of weekly preventive maintenance (PM) verification tracking

# Target energy calibration standard is 200 Joules. 
# Industry safety margins allow a maximum variance of ±10% (180J to 220J)
target_energy = 200.0
ucl = 220.0
lcl = 180.0

dates = [start_date + timedelta(weeks=i) for i in range(weeks)]
days_passed = np.array([i * 7 for i in range(weeks)]).reshape(-1, 1)

# Device A: Stable system with normal hardware noise variance
device_A_noise = np.random.normal(0, 1.8, weeks)
device_A_energy = target_energy + device_A_noise

# Device B: Degraded interior capacitor leaking charge over operational runtime
# Simulates a slow, linear internal system component decay slope
degradation_slope = -0.42  # Drops roughly 0.42 Joules per week
device_B_noise = np.random.normal(0, 1.2, weeks)
device_B_energy = target_energy + (degradation_slope * (days_passed.flatten() / 7)) + device_B_noise

df = pd.DataFrame({
    'Days': days_passed.flatten(),
    'Device_A_Joules': device_A_energy,
    'Device_B_Joules': device_B_energy
}, index=dates)

# =====================================================================
# 2. FIT THE MACHINE LEARNING PREDICTIVE MODEL (LINEAR REGRESSION)
# =====================================================================
print("\n📊 Training regression models on hardware degradation timelines...")

# Fit model to the failing device (Device B)
X = df[['Days']].values  # Independent variable: Time elapsed in days
y = df['Device_B_Joules'].values  # Dependent variable: Output energy delivered

model = LinearRegression()
model.fit(X, y)

# Extract mathematical coefficients (y = mx + c)
intercept = model.intercept_
slope_per_day = model.coef_[0]

print(f"📈 Estimated Component Drift Velocity: {slope_per_day * 7:.3f} Joules lost per week.")

# Calculate the exact timestamp crossing the Lower Control Limit threshold boundary (180 Joules)
# 180 = slope * target_day + intercept -> target_day = (180 - intercept) / slope
failure_day = (lcl - intercept) / slope_per_day
failure_date = start_date + timedelta(days=int(failure_day))

print("\n--- 🚨 PREDICTIVE MAINTENANCE TELEMETRY ALERT ---")
print(f"⚠️ SYSTEM CRITICAL: Defibrillator Asset #003 (Device B) displays component decay.")
print(f"📅 Calculated failure cross-date threshold: {failure_date.strftime('%B %d, %Y')}")
print("🛠️ ACTION REQUIRED: Dispatch service technician to hot-swap high-voltage discharge capacitor module.")

# =====================================================================
# 3. COMPILE REGRESSION VISUALIZATION TREND BANDS
# =====================================================================
# Predict future timeline vectors to overlay prediction curve line
future_days = np.array([i * 7 for i in range(weeks + 25)]).reshape(-1, 1)
future_dates = [start_date + timedelta(days=int(d)) for d in future_days.flatten()]
predicted_energy = model.predict(future_days)

plt.figure(figsize=(11, 6))

# Plot historical sensor telemetry data
plt.scatter(df.index, df['Device_B_Joules'], color='#e74c3c', alpha=0.7, label='Device B Telemetry readings (Failing Unit)')
plt.plot(df.index, df['Device_A_Joules'], color='#2ecc71', alpha=0.4, linestyle=':', label='Device A Telemetry tracker (Control Unit)')

# Plot machine learning prediction slope ray
plt.plot(future_dates, predicted_energy, color='#c0392b', linewidth=2.5, linestyle='--', label='ML Predictive Degradation Slope')

# Structural industry regulatory boundary bands
plt.axhline(y=target_energy, color='#ffffff', linestyle='-', alpha=0.3, label='Target Benchmark (200J)')
plt.axhline(y=ucl, color='#d35400', linestyle='-.', alpha=0.6, label='Upper Regulatory Threshold (220J)')
plt.axhline(y=lcl, color='#d35400', linestyle='-.', alpha=0.6, label='Lower Regulatory Threshold (180J)')

# Highlight failure crossing boundary point intersection intersection
plt.axvline(x=failure_date, color='#95a5a6', linestyle=':', alpha=0.8)
plt.text(failure_date + timedelta(days=10), 183, f"Predicted Out-of-Spec:\n{failure_date.strftime('%m/%d/%Y')}", color='#ffffff', fontweight='bold', bbox=dict(facecolor='#c0392b', alpha=0.8))

plt.title('Clinical Asset Analytics: Defibrillator Energy Drift Forecast via Linear Regression', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Preventive Maintenance Verification Dates', fontweight='bold')
plt.ylabel('Delivered Energy Output Performance (Joules)', fontweight='bold')
plt.ylim(170, 230)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='lower left')
plt.tight_layout()

# Force dark-mode styling aesthetics for professional control deck theme formatting
plt.gcf().patch.set_facecolor('#1e1e24')
plt.gca().set_facecolor('#2d2d35')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().title.set_color('white')
plt.gca().tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color('#44444e')

plt.show()
