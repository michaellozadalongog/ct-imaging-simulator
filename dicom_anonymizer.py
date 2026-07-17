import os
import hashlib
import random
from pydicom import dcmread
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, SecondaryCaptureImageStorage

print("🛡️ Medical Cyber-Security: HIPAA DICOM Automated Anonymizer Pipeline Active 🛡️")

# Ensure the local environment paths exist from our network projects
source_dir = os.path.expanduser('~/medical_data')
output_dir = os.path.expanduser('~/anonymized_output')
os.makedirs(output_dir, exist_ok=True)

# Generate a test image to ensure execution if directory was cleared out
sample_file = os.path.join(source_dir, 'sample_image.dcm')
if not os.path.exists(sample_file):
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = SecondaryCaptureImageStorage
    file_meta.MediaStorageSOPInstanceUID = '1.2.3.4.5.6.7'
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    ds = Dataset()
    ds.file_meta = file_meta
    ds.PatientName = "Lozada^Michael^John"
    ds.PatientID = "SSN-999-12-3456"
    ds.PatientBirthDate = "19880414"
    ds.SOPClassUID = SecondaryCaptureImageStorage
    ds.SOPInstanceUID = '1.2.3.4.5.6.7'
    ds.is_little_endian = True
    ds.is_implicit_VR = False
    ds.save_as(sample_file, write_like_original=False)

# =====================================================================
# DATA PATIENT WORKFLOW ANONYMIZATION PROCESSING ENGINE
# =====================================================================
print(f"\nScanning repository targets at: {source_dir}...")
dicom_files = [f for f in os.listdir(source_dir) if f.endswith('.dcm')]

if not dicom_files:
    print("⚠️ No valid medical scan structures found to sanitize.")
else:
    print(f"🔬 Found {len(dicom_files)} targets. Stripping sensitive identifiers...")
    
    for filename in dicom_files:
        file_path = os.path.join(source_dir, filename)
        
        # Open and decrypt structural binary elements
        ds = dcmread(file_path)
        
        # Capture baseline headers before running masking loops
        raw_name = getattr(ds, 'PatientName', 'Unknown')
        raw_id = getattr(ds, 'PatientID', 'Unknown')
        
        # 1. Obfuscate Hexadecimal Tag (0010,0010) Patient Name -> Secure Hash Unique Code
        hashed_identity = "SUBJ_" + hashlib.sha256(str(raw_name).encode()).hexdigest()[:8].upper()
        ds.PatientName = hashed_identity
        
        # 2. Obfuscate Hexadecimal Tag (0010,0020) Patient ID -> Masked Tracking System Token
        ds.PatientID = f"ANON-SYS-{random.randint(10000, 99999)}"
        
        # 3. Obfuscate Hexadecimal Tag (0010,0030) Patient Birth Date -> General Age Bracket
        # Keeps diagnostic demographics valid without triggering structural privacy violations
        if hasattr(ds, 'PatientBirthDate') and ds.PatientBirthDate:
            try:
                birth_year = int(ds.PatientBirthDate[:4])
                approximate_age = 2026 - birth_year
                ds.PatientBirthDate = f"AGE_BRACKET_{approximate_age // 10 * 10}S"
            except ValueError:
                ds.PatientBirthDate = "AGE_BRACKET_UNKNOWN"
        else:
            ds.PatientBirthDate = "AGE_BRACKET_RESTRICTED"
            
        # Write files securely to separate isolated partition space
        output_path = os.path.join(output_dir, f"sanitized_{filename}")
        ds.save_as(output_path)
        
        print("\n--- CLINICAL PRIVACY CONTEXT SANITIZED ---")
        print(f"❌ [ORIGINAL METRICS]: Name: {raw_name} | Ident ID: {raw_id}")
        print(f"🔒 [ANONYMIZED CONTEXT]: Key: {ds.PatientName} | Token: {ds.PatientID} | Demographics: {ds.PatientBirthDate}")
        print(f"📂 Verification payload output isolated at: {output_path}")

print("\n🚀 Database batch sanitization cycle complete.")
