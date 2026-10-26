# FraudSight — Bihar Police Cybercrime Hackathon
## 8-Minute Demo Script

**Live URL:** `https://fraud-detectorgraph.vercel.app`
**Audience:** Hackathon jury, senior Bihar Police officers (DGP / ADG Cyber / SPs), bank nodal officers
**Rule:** Stay entirely in the browser. No code files, no terminals, no slides.

---

## Timeline at a Glance

| Time | What's on screen | What you're showing |
|---|---|---|
| 0:00 – 1:15 | Cockpit landing page | The problem — why Bihar PS officers lose the golden hour |
| 1:15 – 2:30 | 6-pillar bar, cockpit overview | How the system covers each requirement from the problem statement |
| 2:30 – 3:45 | 1930 Complaint panel + Leaderboard | Cross-district correlation revealing an organized syndicate |
| 3:45 – 5:00 | Investigation timeline + graph | The automated investigation running live |
| 5:00 – 6:15 | Cytoscape network graph | Money trail and shared device evidence |
| 6:15 – 7:15 | HHG-001 (cleared citizen) | Why the system does not freeze legitimate accounts |
| 7:15 – 8:00 | Dossier tabs + /cases ledger | Court-ready evidence and closing |

---

## Pre-Recording Checklist

1. Browser fullscreen at `https://fraud-detectorgraph.vercel.app`
2. Case HHG-014 loaded and selected by default
3. Background tabs open: `/cases`, `/analytics`
4. Speak at a measured pace — pause after each point lands on screen

---

## Scene-by-Scene Script

---

### SCENE 1 — The Problem (0:00 – 1:15)

*Screen: Cockpit landing page. Let it fully load before speaking.*

Good morning. I want to start with a specific situation that repeats itself every day across Bihar.

A resident of Patna — a teacher, a shopkeeper, a daily wage worker — receives a WhatsApp video call. The caller is in a police uniform. They say the person's Aadhaar has been flagged in a narcotics trafficking case and they are under digital arrest. They must transfer money to a verification account immediately, or a police team will come to their home.

The victim transfers ₹6,247. Within about two and a half minutes, that money moves through two intermediate accounts and is withdrawn from an ATM in Muzaffarpur — 150 kilometres away.

When the victim calls 1930, the national cybercrime helpline, the officer at the police station runs into three real problems. First, tracking which accounts the money passed through, across different banks, takes days of manual coordination. Second, by the time any bank notice is issued, the account is already empty. Third, if the system responds too broadly and starts freezing accounts without verification, it catches legitimate people — a government employee's salary account, a pensioner's account — and that causes its own set of complaints.

FraudSight is built around those three constraints. It connects to the transaction network, traces where money moved, checks whether an account belongs to a genuine citizen, and if the evidence is sufficient, it triggers a debit freeze through the 1930 CFCFRMS portal — within the same session the complaint comes in.

---

### SCENE 2 — System Overview: 6 Pillars (1:15 – 2:30)

*Screen: Hover slowly across each pillar tile at the top of the cockpit. Rest on each one for two seconds before moving.*

The system is organized around the six capability areas from the problem statement. Let me go through each one briefly.

*(hover over Pillar 1)*
Transaction Analysis — the system ingests account-level transaction logs and looks for velocity patterns. An account that receives funds and moves 95% of them forward within 140 seconds is a textbook pass-through mule. That pattern alone triggers a flag.

*(hover over Pillar 2)*
Mule Risk Scoring — each flagged account gets a score between 0 and 1, built from four signals: how fast it moves money, how central it is in the transaction network, how many 1930 complaints name it, and whether the mobile device associated with it has appeared on other flagged accounts. The score determines what action is recommended.

*(hover over Pillar 3)*
Money Trail — the system follows the actual fund movement up to four hops from the victim's account to wherever the money ends up. Each step is tracked and timestamped.

*(hover over Pillar 4)*
1930 Complaint Correlation — complaints filed at different police stations across Bihar are connected through the graph. When two or three complaints from different districts point to the same receiving account, that is a syndicate pattern, not isolated incidents.

*(hover over Pillar 5)*
Network Visualization — the transaction network is rendered as an interactive graph. An officer can click any node and see what it is connected to and why it was flagged, without needing to read through a report.

*(hover over Pillar 6)*
Evidence Dossier — every completed investigation generates structured output: the full case record, a Suspicious Transaction Report formatted for FIU-IND, and the relevant legal citations under Section 66D of the IT Act and Section 65B of the Indian Evidence Act. One bundle, ready to go into the chargesheet.

---

### SCENE 3 — Cross-District Syndicate Detection (2:30 – 3:45)

*Screen: Left column. Point to the 1930 Complaint Correlation panel, then scroll down to the Mule Risk Leaderboard.*

*(point to the Syndicate Hub Detected box)*

This is the result for account 9123456789 PNB.

An officer looking at only one complaint would see a ₹6,247 transfer — small amount, easy to deprioritize in a busy station. But the system does not evaluate a complaint in isolation. It checks whether the same receiving account appears in any other complaint filed anywhere in Bihar.

In this case, the same PNB account appears in three separate 1930 complaints. One from Patna — a digital arrest case. One from Gaya — a fake investment scheme. One from Muzaffarpur — UPI phishing. Three different victims, three different districts, three different fraud types, all routing money into the same account.

That is not coincidence. That is a coordinated operation across Bihar.

The system marks this account as a syndicate hub and recommends a debit freeze under Section 66D of the IT Act through the CFCFRMS portal. On the leaderboard below, this account sits at the top with a risk score of 0.94.

---

### SCENE 4 — Autonomous Investigation (3:45 – 5:00)

*Screen: Click the "Run Investigation" button. Wait 2–3 seconds after clicking before speaking — let the first few timeline entries appear on screen.*

*(click the button, then pause)*

I will narrate what the system is doing as the timeline runs through.

The first step is pulling the 1930 complaint data for this account along with the relevant transaction records. That takes under 100 milliseconds.

The second step is the graph query — the system follows the edges from this account outward, two hops, and returns all connected accounts and how they are related. That runs in about 20 milliseconds.

Third, it extracts the four evidence signals: how quickly funds moved out, where this account sits in the broader network, how many complaints name it, and whether the device IMEI used to operate it has been seen on other flagged accounts.

Fourth — and this step is important for preventing wrongful action — it runs the citizen check. It looks for recurring salary credits, utility bill payment history, and how old the account is. For this account: no payroll credits, no utility payments, 45 days old. That does not match a legitimate personal account. The citizen check fails. This is a mule account, not a genuine holder who happened to be near a fraud network.

Fifth, the system checks whether it has collected enough evidence to close the investigation. There is a numeric threshold for this so the process does not run indefinitely. The score here is 0.031, well below the 0.05 cutoff. Evidence is sufficient.

Final output: confirmed fraud, debit freeze recommended.

The officer reviews this output and approves the action. The automated portion takes under a second.

---

### SCENE 5 — Money Trail and Device Graph (5:00 – 6:15)

*Screen: Central Cytoscape graph. Click nodes slowly — 2 to 3 seconds between each click.*

*(click the green victim node)*

This is the victim, Ramesh Yadav, Patna. The panel on the right shows the ₹6,247 transfer.

*(click the mule account node)*

This is account 9123456789 PNB — the primary receiving account. Look at the edges coming out of it.

*(trace the orange edge toward Muzaffarpur)*

One edge goes forward to a second account in Muzaffarpur. The money moved there within 92 seconds. That is the layering step — the goal is to put distance between the funds and the original account before any freeze can be issued.

*(click the IMEI node)*

This amber node is the mobile device IMEI. The system found that this one physical handset was used to log into four different bank accounts. That points to someone managing multiple accounts from a single device — different SIMs, same phone, one operator behind it.

*(click the complaint node)*

This node is the 1930 complaint. It is part of the same graph, which means the full chain — from the victim's complaint to the accounts the money moved through — is connected and auditable in one place.

The value of this view is practical. An officer can sit with a bank nodal officer, open this on screen, and walk through exactly which accounts to freeze and the reason behind each one. There is no ambiguity.

---

### SCENE 6 — Citizen Protection (6:15 – 7:15)

*Screen: Click HHG-001 in the investigation queue on the left.*

*(click HHG-001)*

I want to show this case, because getting this right matters as much as catching fraud.

This is Amit Kumar in Patna. His account was flagged because a payment he received connected to the broader fraud network the system was tracking. Under a blunt rule-based system, that proximity could trigger a freeze on his account.

Look at what the citizen protection check finds. He has consistent monthly salary credits from Bihar Government Finance Department. He has regular SBPDCL electricity bill payments going back over two years. His account is three years old with a normal transaction history.

All three checks pass. Risk score is 0.04. The system closes the case — no action, account stays active.

Across the 20 test cases in the benchmark, 6 were legitimate accounts. All 6 were correctly cleared. The system does not treat proximity to a flagged account as evidence of wrongdoing. It requires the account to actually fail the citizen checks before any freeze is recommended.

This matters legally — a wrongful freeze on a salary account is a serious error with real consequences. And it matters practically, because those errors damage public trust and create their own complaints. The system is built to make that mistake as unlikely as possible.

---

### SCENE 7 — Evidence Dossier and Close (7:15 – 8:00)

*Screen: Click each dossier tab at the bottom right. Pause briefly on each. Then navigate to /cases.*

*(click through: investigation_record → str_fiu_ind → initial_actions → final_actions)*

Every completed investigation automatically generates four output files.

The investigation record is the full case detail — every signal evaluated, the graph traversal steps, timestamps, the final disposition. This is the chain of custody document for the investigation.

The STR is the Suspicious Transaction Report, formatted for submission to FIU-IND and I4C. The officer does not write this manually — it is produced from the case data.

The action files show what the system recommended at the outset and what the final disposition was after the investigation completed. That gap is the audit trail — evidence that human review happened before anything was executed.

The officer clicks Export Dossier, downloads the bundle, and attaches it to the chargesheet. The legal references — Section 66D of the IT Act, Section 65B of the Indian Evidence Act — are already cited inside the document.

*(navigate to /cases)*

This is the full case ledger. 20 cases from across Bihar — Patna, Gaya, Muzaffarpur, Bhagalpur, Nalanda. Digital arrest, fake investment apps, UPI phishing, fake recruitment scams. 14 confirmed fraud, 6 cleared. No missed detections, no wrongful freezes across the benchmark set.

The system is live at fraud-detectorgraph.vercel.app. Thank you.

---

## Presenter Notes

- **Pace**: Slower than feels natural. The judges are reading the screen while you are speaking — let each element settle before you move to the next point.
- **Lists**: When the script has a sequence of items, speak them as connected sentences rather than reading them as a list. "The system checks X, then Y, and then verifies Z" — not "Point one: X. Point two: Y."
- **Technical terms**: Any time you use a technical phrase, immediately follow it with what it actually did in plain language. The term only earns its place if the explanation follows.
- **Amounts**: Say "rupees" clearly, not just the number. "Six thousand two hundred and forty-seven rupees" lands differently from reading out digits.
- **Pointing**: Point to or hover over a screen element before naming it. Give the judges a moment to locate it before you explain it.
- **Transitions**: The scene labels are reference points, not pauses. Move between sections with a connecting phrase rather than stopping cold.
