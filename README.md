# Medical Systems Engineering & Imaging Portfolio

A collection of high-fidelity engineering simulations demonstrating deep expertise in diagnostic imaging systems physics, healthcare IT networking, and clinical device architecture.

---

## Project 1: CT Scanner Field Engineer Simulator
A diagnostic simulation demonstrating how raw computed tomography data transforms into cross-sectional images, and how a physical hardware fault maps to a visual artifact.

* **Core Concept:** A single dead detector channel on a rotating CT gantry drops raw X-ray data across all 180 projection angles. While this looks like a flat vertical line in a raw **Sinogram**, the **Filtered Back-Projection (FBP)** algorithm maps this line into a perfect circle in the final image, known as a **Ring Artifact**.
* **Field Service Impact:** When field service engineers encounter a ring artifact on a clinical scan, they skip abstract troubleshooting. They know instantly to pull, clean, or swap that specific physical detector module—drastically reducing system downtime.

---

## Project 2: Hospital PACS & DICOM Network Node
A localized clinical network loopback architecture mimicking hospital server environments and standard diagnostic transmission protocols.

* **Core Concept:** Built an active background PACS Archive Node running a listener on port 4242 to process incoming healthcare data traffic. Paired it with a Modality Client simulator that programmatically generates valid digital medical images containing strict, mandatory DICOM metadata tags.
* **Systems Impact:** Successfully executed network handshakes to pass data packets via standard **Verification (C-ECHO)** and **Storage (C-STORE)** pipeline commands over the network loopback. This proves structural verification capability for hospital-wide clinical database integrations.

---

## Project 3: Military-Grade Medical Asset CMMS Database
An automated Computerized Maintenance Management System (CMMS) designed to optimize asset lifecycle upkeep, risk classification, and preventive safety compliance.

* **Core Concept:** Engineered a relational relational database structure containing two coupled tracking logs: inventory metrics (serial numbers, facility clinics, risk levels) and active maintenance work schedules. Built an automation algorithm that dynamically monitors upcoming safety expiration dates.
* **Operations Impact:** System parses fleet records in real time, automatically flashes critical clinical maintenance alarms for near-term expiring items, and auto-generates formal 'Pending' preventive maintenance work orders—eliminating scheduling bottlenecks for life-support infrastructure.
