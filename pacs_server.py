from pynetdicom import AE, evt
from pynetdicom.sop_class import Verification, SecondaryCaptureImageStorage

# Define what happens when our server receives an image file
def handle_store(event):
    dataset = event.dataset
    dataset.file_meta = event.file_meta
    patient_name = getattr(dataset, 'PatientName', 'Anonymous')
    print(f"📦 Received medical scan successfully! Patient Name: {patient_name}")
    return 0x0000  # Return success code to the sender

handlers = [(evt.EVT_C_STORE, handle_store)]

# Initialize Server Application Entity
ae = AE(ae_title=b'HOSPITAL_PACS')
ae.add_supported_context(Verification)
ae.add_supported_context(SecondaryCaptureImageStorage)

print("🚀 Hospital PACS Node is online and listening on port 4242...")
# Start the server (runs forever until you press Ctrl+C)
ae.start_server(('127.0.0.1', 4242), block=True, evt_handlers=handlers)
