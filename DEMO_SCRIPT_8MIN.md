# 🎬 FraudSight — Bihar Police Cybercrime Hackathon
## Final 8-Minute Video Demo Script (100% Live UI — Zero Code Openings)
**Platform URL:** `https://fraud-detectorgraph.vercel.app` (or `localhost:8000`)  
**Target Audience:** Senior Police Leadership (DGP, ADG Cyber, SPs, DSPs), Hackathon Evaluation Jury, and Bank Nodal Officers  
**Key Principle:** The entire 8-minute presentation takes place **exclusively within the live Web UI**. You never open VS Code, Python files, or terminals. Everything the judges need to see is beautifully rendered in the Cockpit, Network Graph, and Dossier.

---

## ⏱️ Video Timeline Overview
| Timestamp | Scene Name | What is on Screen | Key Message for Judges |
| :--- | :--- | :--- | :--- |
| **0:00 – 1:15** | **The Crisis & Problem Statement** | Problem Intro & Cockpit Load | The Golden Hour crisis in Bihar: ₹3.4L lost in minutes across 5 districts. |
| **1:15 – 2:30** | **The Police Cockpit (6 Pillars)** | FraudSight Main Cockpit (`/`) | All 6 mandatory pillars live in one operational command center. |
| **2:30 – 3:45** | **Syndicate Hub & 1930 Helpline** | Complaint Correlation & Leaderboard | 3 complaints, 3 districts, 1 mule account: instant debit freeze via 1930. |
| **3:45 – 5:00** | **Live AI Autonomous Investigation** | Timeline & Interactive Graph | Live click of "Launch Autonomous Investigation" on Case HHG-014. |
| **5:00 – 6:15** | **Money Trail & IMEI Device Sharing** | Cytoscape Visual Network Graph | Click nodes: Victim → Mule L1 → Mule L2 → ATM Cashout & shared hardware. |
| **6:15 – 7:15** | **Citizen Protection Shield** | Case HHG-001 (Cleared Citizen) | Anti-Overblocking: Why we do NOT freeze innocent citizens' accounts. |
| **7:15 – 8:00** | **Court Dossier & Final Summary** | Dossier Viewer, Cases & Analytics | Court-ready Sec 65B evidence, 20-case ledger, and production readiness. |

---

## 📋 Pre-Recording Setup
1. Open browser in full screen (F11 or maximize) at `https://fraud-detectorgraph.vercel.app`.
2. Ensure Dark Mode is active (default).
3. Reset view so Case `HHG-014` is selected by default.
4. Keep tabs ready for `/cases` and `/analytics` in background tabs if needed.
5. Speak with confidence, calm authority, and clear pacing.

---

## 🎬 SCENE-BY-SCENE PRESENTATION SCRIPT

### 📍 SCENE 1: THE CRISIS & BIHAR POLICE PROBLEM STATEMENT (0:00 – 1:15)
**Screen:** FraudSight Cockpit landing page (`/`), showing the top bar: "Bihar Police Cyber Command • TigerGraph Grid".

> **[PRESENTER — DELIBERATE & AUTHORITATIVE]**
>
> *"Respected members of the jury and senior officers of Bihar Police.*
>
> *Every single day across Patna, Gaya, Muzaffarpur, Bhagalpur, and Nalanda, ordinary citizens receive a terrifying WhatsApp video call. The person on the screen wears a police uniform or displays a fake CBI badge. They say: 'Your Aadhaar card has been linked to a narcotics shipment. You are under Digital Arrest. Transfer your savings to this court-authorized verification account, or a police team will break your door down.'*
>
> *Panicked, the victim transfers ₹6,247 or ₹45,000 or ₹1,20,000. Within 180 seconds, that money is moved through two intermediate mule accounts and cashed out at an ATM 150 kilometers away.*
>
> *When the victim calls the 1930 National Cybercrime Helpline, the investigating officer faces three massive roadblocks:*
> 1. *First: Tracing layered mule bank accounts manually across different banks takes days.*
> 2. *Second: By the time notices are issued, the account is emptied.*
> 3. *Third: Blunt automated blocks frequently freeze innocent citizens' salary accounts, causing public harassment.*
>
> *This is FraudSight: Bihar Police's Autonomous Cybercrime Investigation and Mule Account Detection Cockpit. Powered by TigerGraph's graph engine, it analyzes multi-hop money trails, correlates 1930 complaints in real-time, and executes legal debit freezes within the golden hour."*

---

### 📍 SCENE 2: THE POLICE COCKPIT & 6 PILLARS (1:15 – 2:30)
**Screen:** Hover and point smoothly across the 6 Pillars Bar at the top of the screen.

> **[PRESENTER]**
>
> *"Looking at the screen, notice how FraudSight addresses every single requirement of the hackathon problem statement through our top Command Strip:*
> - *[Hover over Pillar 1]* **Pillar 1: Transaction Analysis** — Ingesting live transaction logs with sub-second GSQL traversal.
> - *[Hover over Pillar 2]* **Pillar 2: Mule Detection** — Multi-factor XAI scoring ranking account risk from 0 to 1.
> - *[Hover over Pillar 3]* **Pillar 3: Money Trail** — 4-hop deep topological path traversal showing exactly where victim funds moved.
> - *[Hover over Pillar 4]* **Pillar 4: 1930 NCRP Correlation** — Linking independent complaints across multiple Bihar police stations to unmask organized syndicates.
> - *[Hover over Pillar 5]* **Pillar 5: Graph Visualization** — Real-time interactive Cytoscape network view.
> - *[Hover over Pillar 6]* **Pillar 6: Police Cockpit & Evidence Dossier** — Court-ready Section 65B Indian Evidence Act certificates and 1930 debit freeze execution.
>
> *Everything is in Indian Rupees, grounded in Bihar's jurisdiction, and built specifically for police operations."*

---

### 📍 SCENE 3: SYNDICATE HUB & 1930 HELPLINE GOLDEN HOUR (2:30 – 3:45)
**Screen:** Left Column — Focus on the **1930 / NCRP Complaint Correlation** panel and **Mule Risk Leaderboard**.

> **[PRESENTER]**
>
> *"[Point to the pulsing red box labeled 'SYNDICATE HUB DETECTED']*
>
> *Here is the power of cross-district graph correlation. Notice account **9123456789_PNB**.*
>
> *An investigating officer sitting in Patna Cyber PS might think this is just an isolated complaint of ₹6,247.*
> *But FraudSight instantly correlates the graph across the entire state of Bihar:*
> - *Complaint 1: `NCRP/BH/2024/001234` filed in Patna — Digital Arrest extortion.*
> - *Complaint 2: `NCRP/BH/2024/002891` filed in Gaya — Fake Investment App scam.*
> - *Complaint 3: `NCRP/BH/2024/003445` filed in Muzaffarpur — UPI OTP Phishing.*
>
> *Three separate victims. Three different districts. Yet all three funneled money into this exact same PNB account!*
>
> *This is an organized cybercrime syndicate operating across Bihar. FraudSight immediately triggers an automated disposition:*
> **`INITIATE_DEBIT_FREEZE_1930`** *under Section 66D of the IT Act through the Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS).*
>
> *Looking at the Mule Account Leaderboard below, this account ranks #1 with a Critical Risk Score of **0.94**."*

---

### 📍 SCENE 4: LIVE AI AUTONOMOUS INVESTIGATION (3:45 – 5:00)
**Screen:** Center/Right — Point to the **Launch Autonomous Investigation** button, click it, and watch the live timeline and graph react.

> **[PRESENTER]**
>
> *"Now, let us watch the AI conduct an autonomous forensic investigation live on screen.*
>
> *[Click the 'Launch Autonomous Investigation' button]*
>
> *Watch the Investigation Timeline terminal stream in real-time:*
> 1. *At `00:00.08` — Ingest: 1930 complaint ingested for Account `9123456789_PNB` with ₹6,247 victim loss.*
> 2. *At `00:00.18` — Traversal: TigerGraph executes a 2-hop topological query in just 21 milliseconds.*
> 3. *At `00:00.32` — Evidence Extraction: 4 forensic signals extracted — velocity burst, multi-district linkage, shared hardware.*
> 4. *At `00:00.44` — Citizen Filter: Checks salary and utility patterns. The account has zero salary credits, no utility bills, and is only 45 days old. Citizen Check: FAIL — Mule Account Confirmed.*
> 5. *At `00:00.56` — Stopping Gate: Information-Theoretic VOI is 0.031, passing the 0.05 threshold. The AI mathematically proves it has sufficient evidence to conclude.*
> 6. *At `00:00.68` — Disposition: Status updates to **CONFIRMED FRAUD — FREEZE EXECUTED**.*
>
> *Notice that the investigator didn't have to write queries or wait days. In under 1 second, the investigation is concluded with mathematical precision."*

---

### 📍 SCENE 5: INTERACTIVE MONEY TRAIL & SHARED HARDWARE GRAPH (5:00 – 6:15)
**Screen:** Main Visual Graph in the center. Click on nodes to demonstrate interactivity.

> **[PRESENTER]**
>
> *"Now look at the visual graph in the center of the cockpit.*
>
> *[Click on the green hexagon node: 'Victim: Ramesh Yadav']*
> *Here is the victim in Patna. The drawer on the right shows his transfer.*
>
> *[Click on the red diamond node: 'Txn: Rs.6,247']*
> *Here is the coerced transfer of ₹6,247.*
>
> *[Click on the red ellipse node: 'Mule Account 9123456789_PNB']*
> *Here is the primary mule account in Patna. But look where the edges lead:*
>
> *1. First, an orange edge **LAYERED_TO** connects to `Mule L2: 9876543210_SBI` in Muzaffarpur. The fraudsters immediately moved the money to a second layer to evade detection.*
>
> *2. Second, look at the amber node: **`IMEI: 864209041234567`**. This is shared mobile hardware. FraudSight discovered that this single physical device was used to log into 4 different bank accounts! That is definitive forensic proof of a professional mule handler operating multiple burner SIMs on one handset.*
>
> *3. Third, the pink diamond connects directly to the **1930 National Cybercrime Portal complaint**.*
>
> *Every node is color-coded, labeled in Indian Rupees, and clickable. A non-technical investigating officer can understand this entire syndicate in 10 seconds."*

---

### 📍 SCENE 6: CITIZEN PROTECTION SHIELD (ANTI-OVERBLOCKING) (6:15 – 7:15)
**Screen:** Left Queue — Click on **HHG-001 - Account CLEARED (Legitimate Citizen - Rs.0)**.

> **[PRESENTER]**
>
> *"Now let us demonstrate the most critical feature for public trust: **Anti-Overblocking**.*
>
> *[Click on 'HHG-001' in the queue]*
>
> *In any cybercrime operation, there is always a danger of wrongful freezes. An innocent shopkeeper or teacher receives a payment that happened to touch a flagged account, and suddenly their life savings are frozen.*
>
> *Look at what FraudSight does for Case HHG-001 — a citizen named Amit Kumar in Patna:*
> - *Look at the Citizen Protection Filter panel on the left:*
>   - *Recurring Salary Credits: **PASS (Active)** — Monthly salary verified from Bihar Government Finance Department.*
>   - *Utility Bill Payment History: **PASS (Active)** — Regular payments to SBPDCL Electricity Board for over 2 years.*
>   - *Account Tenure: **PASS (Active)** — Established account with a 3-year spotless history.*
>
> *[Look at the graph]*
> *The graph displays verified green connections: Salary Credit, Utility Bill, and Routine UPI.*
>
> *The Citizen Protection Shield instantly fires: **PASS — Innocent Citizen Verified. Account remains active.** Risk score is 0.04. The action is **CLOSE_NO_FRAUD**.*
>
> *Out of our 20 benchmark cases, 6 legitimate citizens were completely protected from wrongful freezing. We catch the criminals without harassing the citizens."*

---

### 📍 SCENE 7: COURT DOSSIER & FINAL PRODUCTION READINESS (7:15 – 8:00)
**Screen:** Click tabs in the Forensic Evidence Dossier (bottom right), then briefly show the `/cases` directory.

> **[PRESENTER]**
>
> *"Finally, an investigation is only as good as the evidence presented in a court of law.*
>
> *[Click the Dossier tabs: 'case_record', 'sar', 'action_before', 'action_after']*
>
> *At the bottom right, FraudSight automatically produces the complete legal evidence package:*
> - *`case_record`: The full GSQL traversal trail with microsecond timestamps.*
> - *`sar`: The Suspicious Transaction Report formatted for FIU-IND and I4C.*
> - *Legal References: Cited under Section 66D of the IT Act and Section 65B of the Indian Evidence Act (now Bharatiya Sakshya Adhiniyam).*
> - *[Hover over 'Download Evidence Bundle (ZIP)']* An officer can download the entire evidentiary bundle with one click to attach to the Chargesheet.*
>
> *[Briefly navigate to `/cases`]*
> *Here is the full Cybercrime Syndicate Ledger — 20 verified Bihar cases spanning Digital Arrest, Fake Investment Apps, UPI Phishing, and Job Scams across Muzaffarpur, Gaya, Patna, Bhagalpur, and Nalanda.*
>
> *In conclusion: FraudSight is not a prototype or concept. It is a live, resilient, zero-BS command platform built to empower Bihar Police to win the golden hour and dismantle cyber syndicates across the state.*
>
> *Jai Hind. Thank you."*

---

## 🎯 Presenter Tips
1. **Never mention technical code files** (do not say "in `mule_risk_scorer.py`", say "our multi-factor XAI engine").
2. **Always point out Bihar specifics** (say "Patna Cyber PS", "Gaya", "Muzaffarpur", "1930 Helpline", "CFCFRMS").
3. **Keep your mouse smooth** — avoid erratic cursor movements; let each click rest on screen for 2-3 seconds so the judges can read the data.
4. **Emphasize the Rupees** — whenever discussing amounts, say "Rupees" or "₹", emphasizing how it represents real citizen savings.
