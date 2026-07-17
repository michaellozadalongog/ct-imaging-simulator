from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, SecondaryCaptureImageStorage
from pynetdicom import AE
from pynetdicom.sop_class import Verification

# 1. Build a mock clinical image file metadata
file_meta = FileMetaDataset()
file_meta.MediaStorageSOPClassUID = SecondaryCaptureImageStorage
file_meta.MediaStorageSOPInstanceUID = '1.2.3.4.5.6.7'
file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

ds = Dataset()
ds.file_meta = file_meta
ds.PatientName = "Simulated^Patient"
ds.PatientID = "123456"
ds.SOPClassUID = SecondaryCaptureImageStorage
ds.SOPInstanceUID = '1.2.3.4.5.6.7'
ds.is_little_endian = True
ds.is_implicit_VR = False

# 2. Connect and transfer across the network loopback
ae = AE(ae_title=b'MY_CT_SCANNER')
ae.add_requested_context(Verification)
ae.add_requested_context(SecondaryCaptureImageStorage)

print("Connecting to local Hospital PACS...")
assoc = ae.associate('127.0.0.1', 4242)

if assoc.is_established:
    print('🤝 Connected! Transmitting scan over network...')
    status = assoc.send_c_store(ds)
    if status.Status == 0x0000:
        print('🚀 Network Success! Image pushed into server.')
    assoc.release()
else:
    print('❌ Connection Refused.')
