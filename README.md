<!-- ========================================================= -->
<!-- PROJECTS -->
<!-- ========================================================= -->

<br>

<div align="center">

## 🚀 Projects

### Flagship Engineering Systems & Research

<p>
  <img src="https://img.shields.io/badge/Problem_First-111827?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Systems_Engineering-4F46E5?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Build_•_Validate_•_Improve-0891B2?style=for-the-badge" />
</p>

<sub>
Real systems spanning secure communication, UAV software, AI,
cybersecurity, computer vision and embedded engineering.
</sub>

</div>

<br><br>


<!-- ========================================================= -->
<!-- 01 / GOBLINWISP -->
<!-- ========================================================= -->

<table width="100%">

<tr>

<td width="72%" valign="middle">

<h2>01 / GoblinWisp</h2>

<b>Identity-Bound & Directionally Isolated Secure Session Prototype</b>

</td>

<td width="28%" align="right" valign="middle">

<img
src="https://img.shields.io/badge/Repository-PRIVATE-111827?style=for-the-badge&logo=github&logoColor=white"
/>

</td>

</tr>


<tr>

<td colspan="2">

<img
src="./assets/goblinwisp-cover.png"
width="100%"
alt="GoblinWisp Secure Communication Prototype"
/>

</td>

</tr>


<tr>

<td width="50%" valign="top">

### ⚠️ The Problem

Peer devices operating in remote or infrastructure-constrained environments may need secure communication without relying on cloud servers, cellular connectivity or centralized authentication infrastructure.

Poor session handling, replayed packets, unsafe reset behaviour and unrestricted bidirectional trust can weaken peer communication security.

</td>


<td width="50%" valign="top">

### ⚙️ What I Built

Built an **ESP32-based secure communication proof-of-concept over ESP-NOW** with a dedicated secure-session layer.

The prototype implements **identity-bound sessions, authenticated encryption, independent direction-specific cryptographic state, replay handling and authenticated re-establishment**.

</td>

</tr>


<tr>

<td width="50%" valign="top">

### 🧩 Engineering Focus

**Directionally Isolated Security**

Opposite communication directions maintain independent keys, counters, nonce state and authorization context.

<br>

**Transport Independence**

ESP-NOW is used as the prototype transport while the secure-session architecture remains conceptually independent of the underlying wireless channel.

</td>


<td width="50%" valign="top">

### 📌 Project State

**Timeline**  
Dec 2025 — Aug 2026

**Status**  
Embedded Security Prototype

**Role**  
Lead Developer • Inventor

**Domain**  
Embedded Security • Applied Cryptography • Secure Communication

</td>

</tr>

</table>


<br>


<div align="center">

### ⚡ Core Stack

<img src="https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/ESP--NOW-334155?style=for-the-badge" />
<img src="https://img.shields.io/badge/Embedded_C%2FC++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/X25519-0F766E?style=for-the-badge" />
<img src="https://img.shields.io/badge/HKDF--SHA256-047857?style=for-the-badge" />
<img src="https://img.shields.io/badge/AES--GCM-166534?style=for-the-badge" />

<br><br>

### 🧠 Engineering Skills

<img src="https://img.shields.io/badge/Secure_Protocol_Design-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Applied_Cryptography-6D28D9?style=flat-square" />
<img src="https://img.shields.io/badge/Identity--Bound_Sessions-4F46E5?style=flat-square" />
<img src="https://img.shields.io/badge/Replay_Protection-DC2626?style=flat-square" />
<img src="https://img.shields.io/badge/Nonce_Management-E11D48?style=flat-square" />
<img src="https://img.shields.io/badge/Counter_Management-B91C1C?style=flat-square" />
<img src="https://img.shields.io/badge/Session_State_Management-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/Packet_Handling-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/Message_Authentication-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Integrity_Verification-047857?style=flat-square" />
<img src="https://img.shields.io/badge/Fault_Handling-F59E0B?style=flat-square" />
<img src="https://img.shields.io/badge/Real--Time_Debugging-64748B?style=flat-square" />
<img src="https://img.shields.io/badge/Peer--to--Peer_Comms-0F766E?style=flat-square" />
<img src="https://img.shields.io/badge/Wireless_Security-0369A1?style=flat-square" />

</div>


<br>


<details>

<summary><b>🖼️ Explore GoblinWisp Prototype Gallery</b></summary>

<br>

<table width="100%">

<tr>

<td width="33%">
<img src="./assets/goblinwisp-01.png" width="100%" alt="GoblinWisp Prototype View 1" />
</td>

<td width="33%">
<img src="./assets/goblinwisp-02.png" width="100%" alt="GoblinWisp Prototype View 2" />
</td>

<td width="34%">
<img src="./assets/goblinwisp-03.png" width="100%" alt="GoblinWisp Prototype View 3" />
</td>

</tr>

</table>

</details>


<br><br>

---

<!-- ========================================================= -->
<!-- 02 / AERONEXUS COMMAND CENTER -->
<!-- ========================================================= -->


<table width="100%">

<tr>

<td width="72%" valign="middle">

<h2>02 / Aeronexus Command Center</h2>

<b>Unified Mission Control for Next-Generation UAV Systems</b>

</td>

<td width="28%" align="right" valign="middle">

<img
src="https://img.shields.io/badge/Repository-PRIVATE-111827?style=for-the-badge&logo=github&logoColor=white"
/>

</td>

</tr>


<tr>

<td colspan="2">

<img
src="./assets/aeronexus-command-center-cover.png"
width="100%"
alt="Aeronexus Command Center Dashboard"
/>

</td>

</tr>


<tr>

<td width="50%" valign="top">

### ⚠️ The Problem

UAV missions commonly distribute telemetry, mission mapping, aircraft health, battery state, operational zones, alerts and event logs across disconnected interfaces.

This fragmentation increases operator workload and makes it harder to maintain a unified operational picture during time-sensitive missions.

</td>


<td width="50%" valign="top">

### ⚙️ What I Built

Developed a **unified mission-control platform** combining UAV telemetry, route visualization, mission mapping, geofencing, operational zones, aircraft health, battery monitoring, alerts, fleet status and operator controls.

The platform provides a modular software foundation for future **computer vision, onboard sensing, security events and multi-UAV services**.

</td>

</tr>


<tr>

<td width="50%" valign="top">

### 🧩 Engineering Focus

**Unified Operational Awareness**

Telemetry, mission context, aircraft state and operational intelligence are consolidated into a single operator-oriented interface.

<br>

**Modular Backend Architecture**

FastAPI-based services support telemetry ingestion, processing, persistence and communication between UAV-related system components.

</td>


<td width="50%" valign="top">

### 📌 Project State

**Timeline**  
Jul 2026 — Present

**Status**  
Active Development • Software PoC

**Role**  
Founder • Lead Developer

**Domain**  
UAV Systems • Mission Control • Backend Engineering

</td>

</tr>

</table>


<br>


<div align="center">

### ⚡ Core Stack

<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/REST_APIs-2563EB?style=for-the-badge" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/YOLO-111827?style=for-the-badge" />

<br><br>

### 🛰️ UAV & Systems Skills

<img src="https://img.shields.io/badge/UAV_Telemetry-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/Telemetry_Ingestion-0369A1?style=flat-square" />
<img src="https://img.shields.io/badge/Mission_Control-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/Mission_Mapping-4F46E5?style=flat-square" />
<img src="https://img.shields.io/badge/Route_Visualization-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Geofencing-0891B2?style=flat-square" />
<img src="https://img.shields.io/badge/Operational_Zones-0E7490?style=flat-square" />
<img src="https://img.shields.io/badge/Fleet_Monitoring-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Aircraft_Health-16A34A?style=flat-square" />
<img src="https://img.shields.io/badge/Battery_Monitoring-65A30D?style=flat-square" />
<img src="https://img.shields.io/badge/Situational_Awareness-F59E0B?style=flat-square" />
<img src="https://img.shields.io/badge/Event_&_Alert_Handling-EA580C?style=flat-square" />
<img src="https://img.shields.io/badge/Operational_Logs-64748B?style=flat-square" />
<img src="https://img.shields.io/badge/Backend_Architecture-334155?style=flat-square" />
<img src="https://img.shields.io/badge/Modular_System_Design-475569?style=flat-square" />

</div>


<br>


<details>

<summary><b>🖼️ Explore Command Center Interface Gallery</b></summary>

<br>

<table width="100%">

<tr>

<td width="33%">
<img src="./assets/aeronexus-01.png" width="100%" alt="Aeronexus Interface 1" />
</td>

<td width="33%">
<img src="./assets/aeronexus-02.png" width="100%" alt="Aeronexus Interface 2" />
</td>

<td width="34%">
<img src="./assets/aeronexus-03.png" width="100%" alt="Aeronexus Interface 3" />
</td>

</tr>

<tr>

<td width="33%">
<img src="./assets/aeronexus-04.png" width="100%" alt="Aeronexus Interface 4" />
</td>

<td width="33%">
<img src="./assets/aeronexus-05.png" width="100%" alt="Aeronexus Interface 5" />
</td>

<td width="34%">
<img src="./assets/aeronexus-06.png" width="100%" alt="Aeronexus Interface 6" />
</td>

</tr>

</table>

</details>


<br><br>

---

<!-- ========================================================= -->
<!-- 03 / VIGILANTEDGE -->
<!-- ========================================================= -->


<table width="100%">

<tr>

<td width="72%" valign="middle">

<h2>03 / VigilantEdge</h2>

<b>Adaptive AI Firewall & Self-Healing Cyber Defense</b>

</td>

<td width="28%" align="right" valign="middle">

<img
src="https://img.shields.io/badge/Repository-PRIVATE-111827?style=for-the-badge&logo=github&logoColor=white"
/>

</td>

</tr>


<tr>

<td colspan="2">

<img
src="./assets/vigilantedge-cover.png"
width="100%"
alt="VigilantEdge Cybersecurity Platform"
/>

</td>

</tr>


<tr>

<td width="50%" valign="top">

### ⚠️ The Problem

Traditional Web Application Firewalls depend heavily on static signatures and manually configured security policies.

They can struggle with application-specific anomalies, modified attack behaviour, API abuse and security decisions that require contextual understanding.

</td>


<td width="50%" valign="top">

### ⚙️ What I Designed

Designed a staged adaptive defensive architecture combining **reverse-proxy controls, request validation, behavioural analysis, ML-assisted anomaly detection, contextual risk scoring, explainability and policy-controlled remediation**.

Long-term research capabilities are intentionally separated from functionality that has already been implemented or validated.

</td>

</tr>


<tr>

<td width="50%" valign="top">

### 🧩 Engineering Focus

**Adaptive Detection**

Combines conventional defensive controls with behavioural and ML-assisted analysis instead of relying entirely on predefined rules.

<br>

**Explainable Security Decisions**

Explores interpretable risk scoring and explainability so AI-assisted defensive decisions remain reviewable.

</td>


<td width="50%" valign="top">

### 📌 Project State

**Timeline**  
Jan 2026 — Present

**Status**  
Architecture Defined • Staged R&D

**Role**  
Lead Developer • Researcher

**Domain**  
AI • Cybersecurity • Backend Systems

</td>

</tr>

</table>


<br>


<div align="center">

### ⚡ Core Stack

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" />
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />

<br><br>

### 🛡️ Security Engineering

<img src="https://img.shields.io/badge/Web_Application_Security-DC2626?style=flat-square" />
<img src="https://img.shields.io/badge/API_Security-E11D48?style=flat-square" />
<img src="https://img.shields.io/badge/Behavioural_Analysis-DB2777?style=flat-square" />
<img src="https://img.shields.io/badge/Anomaly_Detection-9D174D?style=flat-square" />
<img src="https://img.shields.io/badge/Risk_Scoring-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Explainable_AI-6D28D9?style=flat-square" />
<img src="https://img.shields.io/badge/Threat_Intelligence-B91C1C?style=flat-square" />
<img src="https://img.shields.io/badge/Threat_Hunting-991B1B?style=flat-square" />
<img src="https://img.shields.io/badge/Zero_Trust-4F46E5?style=flat-square" />
<img src="https://img.shields.io/badge/Policy--Driven_Response-2563EB?style=flat-square" />

<br><br>

### 🔬 Research Areas

<img src="https://img.shields.io/badge/Self--Healing_Security-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Cyber_Deception-0F766E?style=flat-square" />
<img src="https://img.shields.io/badge/SOC_Automation-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/Adversarial_AI-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Federated_Learning-6366F1?style=flat-square" />
<img src="https://img.shields.io/badge/Red_Teaming-DC2626?style=flat-square" />
<img src="https://img.shields.io/badge/Cyber_Resilience-EA580C?style=flat-square" />
<img src="https://img.shields.io/badge/IoT_&_5G_Security-0891B2?style=flat-square" />
<img src="https://img.shields.io/badge/Post--Quantum_Concepts-475569?style=flat-square" />

</div>


<br>


<details>

<summary><b>🖼️ Explore VigilantEdge Architecture & Interface Gallery</b></summary>

<br>

<table width="100%">

<tr>

<td width="33%">
<img src="./assets/vigilantedge-01.png" width="100%" alt="VigilantEdge View 1" />
</td>

<td width="33%">
<img src="./assets/vigilantedge-02.png" width="100%" alt="VigilantEdge View 2" />
</td>

<td width="34%">
<img src="./assets/vigilantedge-03.png" width="100%" alt="VigilantEdge View 3" />
</td>

</tr>

</table>

</details>


<br><br>

---

<!-- ========================================================= -->
<!-- 04 / EXOTRACE -->
<!-- ========================================================= -->


<table width="100%">

<tr>

<td width="72%" valign="middle">

<h2>04 / ExoTrace</h2>

<b>AI-Assisted Exoplanet Transit Detection & Candidate Screening</b>

</td>

<td width="28%" align="right" valign="middle">

<img
src="https://img.shields.io/badge/Research-Prototype-6D28D9?style=for-the-badge"
/>

</td>

</tr>


<tr>

<td colspan="2">

<img
src="./assets/exotrace-cover.png"
width="100%"
alt="ExoTrace Exoplanet Research Prototype"
/>

</td>

</tr>


<tr>

<td width="50%" valign="top">

### ⚠️ The Problem

Astronomical light curves contain noise, stellar variability and false-positive patterns that can resemble genuine planetary transit signals.

Candidate screening therefore requires both signal processing and careful machine-learning classification.

</td>


<td width="50%" valign="top">

### ⚙️ What I Built

Built a scientific ML pipeline that processes **TESS light curves**, applies **Box Least Squares**, extracts transit-related features and uses an **ExtraTrees classifier** for candidate prioritization.

The system is positioned as an AI-assisted screening tool rather than a final astronomical confirmation system.

</td>

</tr>


<tr>

<td width="50%" valign="top">

### 📊 Validation Snapshot

**Held-out Accuracy**  
78%

**Macro F1**  
77%

**Candidate Recall at Screening Threshold**  
98%

</td>


<td width="50%" valign="top">

### 📌 Project State

**Timeline**  
2026

**Status**  
Functional Research Prototype

**Domain**  
Scientific ML • Astronomy • Time-Series Analysis

</td>

</tr>

</table>


<br>


<div align="center">

### ⚡ Core Stack

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
<img src="https://img.shields.io/badge/ExtraTrees-6366F1?style=for-the-badge" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />

<br><br>

### 🔭 Scientific & ML Skills

<img src="https://img.shields.io/badge/TESS_Light_Curves-4F46E5?style=flat-square" />
<img src="https://img.shields.io/badge/Box_Least_Squares-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Time--Series_Analysis-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/Signal_Processing-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/Feature_Engineering-0891B2?style=flat-square" />
<img src="https://img.shields.io/badge/Classification-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Model_Evaluation-16A34A?style=flat-square" />
<img src="https://img.shields.io/badge/Precision_&_Recall-EA580C?style=flat-square" />
<img src="https://img.shields.io/badge/Candidate_Prioritization-DB2777?style=flat-square" />
<img src="https://img.shields.io/badge/Scientific_Machine_Learning-6D28D9?style=flat-square" />

</div>


<br>


<details>

<summary><b>🖼️ Explore ExoTrace Research Gallery</b></summary>

<br>

<table width="100%">

<tr>

<td width="33%">
<img src="./assets/exotrace-01.png" width="100%" alt="ExoTrace View 1" />
</td>

<td width="33%">
<img src="./assets/exotrace-02.png" width="100%" alt="ExoTrace View 2" />
</td>

<td width="34%">
<img src="./assets/exotrace-03.png" width="100%" alt="ExoTrace View 3" />
</td>

</tr>

</table>

</details>


<br><br>

---

<!-- ========================================================= -->
<!-- MORE ENGINEERING WORK -->
<!-- ========================================================= -->


<div align="center">

## 🧪 More Engineering Work

<sub>
Additional projects across Generative AI, computer vision,
threat intelligence, automation and embedded security.
</sub>

</div>

<br>


<table width="100%">

<tr>


<!-- EXAMFORGE -->
<td width="50%" valign="top">

### 📄 ExamForge AI

**Generative Assessment & Question Paper Builder**

Generative-AI assessment tool developed for configurable academic practice and GTU-oriented question generation.

<br>

**Core Stack**

<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white" />
<img src="https://img.shields.io/badge/Express.js-000000?style=flat-square&logo=express&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Gemini_API-4285F4?style=flat-square&logo=google&logoColor=white" />

<br><br>

**Skills**

<img src="https://img.shields.io/badge/Generative_AI-8B5CF6?style=flat-square" />
<img src="https://img.shields.io/badge/Prompt_Engineering-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/AI_Integration-6366F1?style=flat-square" />
<img src="https://img.shields.io/badge/REST_APIs-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/API_Integration-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/Input_Validation-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" />
<img src="https://img.shields.io/badge/Environment_Variables-475569?style=flat-square" />

<br><br>

[![View Repository](https://img.shields.io/badge/View_Repository-111827?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Spandan-Shah/Question-Paper-Generator)

</td>


<!-- TINYML -->
<td width="50%" valign="top">

### 📷 TinyML — ESP32-CAM Vision

**Embedded Camera Streaming & Object Detection**

Embedded vision experiment that streams ESP32-CAM frames to a receiver-side detection pipeline.

<br>

**Core Stack**

<img src="https://img.shields.io/badge/ESP32--CAM-E7352C?style=flat-square&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/UDP-2563EB?style=flat-square" />

<br><br>

**Skills**

<img src="https://img.shields.io/badge/Computer_Vision-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Object_Detection-4F46E5?style=flat-square" />
<img src="https://img.shields.io/badge/Image_Streaming-0284C7?style=flat-square" />
<img src="https://img.shields.io/badge/UDP_Streaming-0369A1?style=flat-square" />
<img src="https://img.shields.io/badge/Embedded_Vision-059669?style=flat-square" />
<img src="https://img.shields.io/badge/Frame_Dropping-EA580C?style=flat-square" />
<img src="https://img.shields.io/badge/Low--Latency_Processing-F59E0B?style=flat-square" />

<br><br>

[![View Repository](https://img.shields.io/badge/View_Repository-111827?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Spandan-Shah/TinyML---Object-Detection-Using-ESP32-Cam)

</td>

</tr>

</table>


<br>


<!-- ========================================================= -->
<!-- ADDITIONAL PROJECT BENTO GRID -->
<!-- ========================================================= -->


<table width="100%">

<tr>


<td width="33%" valign="top">

### 🚦 Berlin

**Intelligent Traffic Vision**

<img src="https://img.shields.io/badge/YOLO-111827?style=flat-square" />
<img src="https://img.shields.io/badge/DeepSORT-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/OCR-DB2777?style=flat-square" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square" />

<br><br>

`Vehicle Detection`  
`Object Tracking`  
`License Plate OCR`  
`Speed Estimation`  
`Trajectory Analysis`  
`Traffic Analytics`

</td>


<td width="33%" valign="top">

### 👁️ Vigil

**AI Situational Awareness**

<img src="https://img.shields.io/badge/YOLOv8-111827?style=flat-square" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square" />
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square" />
<img src="https://img.shields.io/badge/RTSP-2563EB?style=flat-square" />

<br><br>

`Object Detection`  
`Video Analytics`  
`Pose / Gesture Analysis`  
`Anomaly Detection`  
`Crowd Analysis`  
`Real-Time Monitoring`

</td>


<td width="34%" valign="top">

### 🕵️ NarcoTrace AI

**Multimodal Threat Intelligence**

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square" />
<img src="https://img.shields.io/badge/NLP-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square" />
<img src="https://img.shields.io/badge/OSINT-DB2777?style=flat-square" />

<br><br>

`Threat Intelligence`  
`Network Analysis`  
`Scrapy`  
`BeautifulSoup`  
`GeoPandas`  
`Responsible AI`

</td>

</tr>


<tr>


<td width="33%" valign="top">

### 📡 SpectraGuard

**Wireless Security Testbed**

<img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square" />
<img src="https://img.shields.io/badge/NRF24L01-2563EB?style=flat-square" />
<img src="https://img.shields.io/badge/SPI-334155?style=flat-square" />

<br><br>

`RF Communication`  
`Wireless Security`  
`Packet Analysis`  
`RF Interference Testing`  
`SPI Interfacing`  
`Embedded Debugging`

</td>


<td width="33%" valign="top">

### 🔄 FlowOps

**Workflow Automation**

<img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" />
<img src="https://img.shields.io/badge/Webhooks-7C3AED?style=flat-square" />

<br><br>

`Workflow Automation`  
`Webhook Processing`  
`API & Data Integration`  
`Input Validation`  
`Event-Driven Workflows`  
`Participant Data Processing`

</td>


<td width="34%" valign="top">

### 🌐 Blackout Community

**Technology & Innovation Community**

<img src="https://img.shields.io/badge/Leadership-111827?style=flat-square" />
<img src="https://img.shields.io/badge/Community-4F46E5?style=flat-square" />

<br><br>

`Team Building`  
`Hackathon Collaboration`  
`Technical Coordination`  
`Community Management`  
`Peer Learning`

</td>

</tr>

</table>

<br>
