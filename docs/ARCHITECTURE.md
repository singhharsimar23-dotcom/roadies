# FraudSight: Technical Architecture & System Blueprint
### Autonomous AI/ML & Graph Analytics Engine for Mule Account Detection & Cybercrime Network Dismantling
**Submission for Bihar Police Cyber Hackathon**  
*Organized by Bihar Police Cyber Crime Division / Economic Offences Unit (EOU)*

---

## 1. Executive Summary & Problem Alignment

Modern cybercrime syndicates (e.g. digital arrest fraud, APK credential theft, fake investment platforms, sextortion, and illegal betting rings) rely on **mule bank accounts** to receive, layer, and cash out illicit proceeds. Traditional rules-based threshold filters fail because they evaluate transactions in isolated tables, leading to delayed freeze actions and rampant fund dissipation before victims can be made whole.

**FraudSight** is an enterprise-grade AI/ML and Graph Analytics investigation platform custom-engineered to solve the six core requirements of the **Bihar Police Cyber Hackathon**:

| Problem Requirement | FraudSight Solution Pillar | Underlying Technology |
| :--- | :--- | :--- |
| **1. Transaction Analysis** | Velocity spike detection, micro-structuring smurf analysis, and 90-day entropy deviation scoring. | TigerGraph GSQL + Statistical Baseline Vectorizer |
| **2. Mule Account Detection** | Multi-hop dynamic risk scoring (0.0 to 1.0), rank ordering, and Explainable AI (XAI) feature attribution. | Graph Centrality + Random Forest / Gradient Boosting + XAI |
| **3. Money Trail Analysis** | Directed multi-hop BFS fund tracing across Layer-1, Layer-2, and Layer-3 pass-through and cashout nodes. | Parameterized GSQL (`get_money_flow.gsql`) |
| **4. Complaint Correlation** | Automated cross-referencing of bank accounts with 1930 Helpline tickets, NCRP ACK numbers, and Cyber PS FIRs. | TigerGraph Shared Identifier Cluster Traversal |
| **5. Graph-Based Investigation** | Sub-second visual exploration of account rings, shared hardware/IMEI, and co-located IP subnets. | Cytoscape.js interactive GPU graph visualizer |
| **6. Investigation Dashboard** | Real-time Law Enforcement Cockpit, prioritized freeze leads, and court-ready Section 65B IEA digital evidence dossiers. | FastAPI + Jinja2 + Vercel Cloud Native Edge Cockpit |

---

## 2. Graph Schema Topology (`MuleGraph`)

TigerGraph's native graph database powers the core entity-relationship model. The schema is optimized for sub-second BFS multi-hop traversals and dynamic relationship materialization across millions of nodes.

### 2.1 Vertex & Edge Topology Diagram

```text
       ┌──────────────┐                                ┌──────────────┐
       │    Device    │                                │  IPCluster   │
       │ (device_id,  │                                │(ip_subnet_id,│
       │  imei_hash)  │                                │ proxy_flag)  │
       └──────▲───────┘                                └──────▲───────┘
              │                                               │
        USED_DEVICE                                    FROM_IP_CLUSTER
              │                                               │
       ┌──────┴───────────────────────────────────────────────┴───────┐
       │                         Transaction                          │
       │     (txn_id, amount_inr, timestamp, is_fraud, risk_score)    │
       └──────────────────────────────▲───────────────────────────────┘
                                      │
                                  PERFORMED
                                      │
       ┌──────────────────────────────┴───────────────────────────────┐
       │                         Bank Account                         │
       │     (account_id, ifsc_code, customer_id, branch, risk_score) │
       └──────┬───────────────────────┬───────────────────────┬───────┘
              │                       │                       │
        SHARES_DEVICE        SHARES_EMAIL_DOMAIN        SHARES_ADDRESS
       (Undirected Ring)       (Collusion Link)        (Mule Safehouse)
              │                       │                       │
              ▼                       ▼                       ▼
       [Hardware Ring]       [Syndicate Hub]          [Mule Cluster]

========================================================================
            CYBERCRIME COMPLAINT & EVIDENTIARY GOVERNANCE SUBGRAPH
========================================================================

       ┌──────────────────────────────────────────────────────────────┐
       │                   Cybercrime Complaint                       │
       │       (ncrp_ack_no, 1930_ticket_id, victim_loss, category)   │
       └───┬──────────────────────────┬──────────────────────────┬────┘
           │                          │                          │
      REPORTED_TXN               LINKED_MULE               EVIDENCE_FOR
           │                          │                          │
           ▼                          ▼                          ▼
    ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
    │ Transaction  │           │ Account/Mule │           │ EvidenceItem │
    │  (Flagged)   │           │ (Freezable)  │           │ (weight, src)│
    └──────────────┘           └──────────────┘           └──────┬───────┘
                                                                 │
                                                       ACTION_GOVERNED_BY
                                                                 │
                                                                 ▼
                                                          ┌──────────────┐
                                                          │ PolicyRule   │
                                                          │(Sec 66D IT,  │
                                                          │ 1930 Freeze) │
                                                          └──────────────┘
```

### 2.2 Schema Entities Summary
- **Financial & Entity Nodes:** `Account` (bank accounts, UPI VPA handles), `Transaction` (NEFT, RTGS, IMPS, UPI, ATM cashout), `Device` (IMEI, device fingerprint, MAC), `IPCluster` (ISP, ASN, VPN/Tor exit flag).
- **Derived Collusion Edges:** `SHARES_DEVICE` (materialized ring linking accounts operating from identical physical hardware), `SHARES_EMAIL_DOMAIN`, `SHARES_ADDRESS`, `MONEY_TRAIL_DIRECT` (directed transfer chains).
- **Complaint & Governance Nodes:** `CyberComplaint` (1930 / NCRP ACK records), `EvidenceItem`, `PolicyRule` (Law Enforcement standard operating procedures under Section 66D IT Act & Section 91 CrPC).

---

## 3. Core Engine Modules & Problem Statement Solutions

### 3.1 Requirement 1: Transaction Analysis (Layering & Velocity Engine)
Organized syndicates split high-value cyber fraud proceeds into smaller micro-structuring transfers ("smurfing") and push funds through 3 to 5 layers within 15 minutes of victim debit.
- **Velocity Burst Tracker:** Computes $\Delta t = t_{out} - t_{in}$ for consecutive transfers on an account. When $\Delta t < 180\text{ seconds}$ with $>85\%$ balance egress, a **Rapid Pass-Through Mule Flag** is materialized.
- **Micro-Structuring Anomaly:** Calculates transaction size entropy relative to statutory thresholds (₹50,000 / ₹2,00,000). Coordinated identical micro-bursts trigger high-priority alerts.
- **Baseline Behavioral Deviation:** Evaluates current transaction frequency against the 90-day moving average. Dormant accounts suddenly receiving high-velocity incoming transfers are ranked in the top 99th percentile of fraud risk.

### 3.2 Requirement 2: Dynamic Mule Risk Scoring & Explainable AI (XAI)
Rather than a non-interpretable black-box score, FraudSight computes a multi-factor **Dynamic Mule Risk Score ($R \in [0.0, 1.0]$)** combining:

$$R = w_1 \cdot C_{\text{topo}} + w_2 \cdot V_{\text{velocity}} + w_3 \cdot D_{\text{hardware}} + w_4 \cdot K_{\text{complaints}}$$

Where:
- $C_{\text{topo}}$: Graph centrality (PageRank and 2-hop connected suspicious neighbor ratio in TigerGraph).
- $V_{\text{velocity}}$: Pass-through transfer speed and rapid fund evacuation indicator.
- $D_{\text{hardware}}$: Hardware collision factor (accounts sharing same device fingerprint / IMEI).
- $K_{\text{complaints}}$: Number of independent 1930 / NCRP complaints linked to transactions touching this account.

**Explainable AI (XAI) Indicators:**
Every scored mule account displays an itemized evidence card:
- `[+0.35]` Rapid Fund Dissipation: 94.2% of credited funds transferred out within 210 seconds.
- `[+0.30]` Hardware Clustering: Shared mobile device fingerprint with 4 known fraud accounts.
- `[+0.25]` Cybercrime Correlation: Directly linked as Layer-1 beneficiary in NCRP Ack #20241025-089.
- `[-0.15]` Legitimacy Attenuation: Verified salary credit from registered PSU entity (Anti-Overblocking).

### 3.3 Requirement 3: Multi-Hop Money Trail Analysis
FraudSight implements parameterized GSQL queries (`get_money_flow.gsql`) executing directed breadth-first search (BFS) up to 4 hops:
- **Layer 1 (Direct Beneficiary):** The initial account receiving funds directly from the cybercrime victim.
- **Layer 2 (Intermediate Layering Mules):** Split accounts used to divide funds into multiple parallel streams.
- **Layer 3 (Cashout & Aggregator Nodes):** Final collection nodes terminating at ATM cash withdrawals, P2P crypto merchants, or POS terminal cashouts.
- **Funnel Account Identification:** Identifies fan-in nodes where multiple disparate victim funds converge into a single consolidation account.

### 3.4 Requirement 4: Cybercrime Complaint Correlation Engine
A single mule ring frequently victimizes citizens across multiple districts (e.g. Patna, Gaya, Muzaffarpur, Bhagalpur).
- Ingests NCRP citizen complaint feeds and 1930 Helpline tickets.
- Materializes bipartite links between `CyberComplaint` and `Transaction` / `Account`.
- Discovers hidden multi-complaint convergence: where 5 different complaints filed at different police stations point back to the same underlying device, mobile number, or IFSC branch hub.

### 3.5 Requirement 5: Graph-Based Visual Investigation Cockpit
- High-performance Cytoscape.js canvas rendering up to 10,000 entities with hardware-accelerated WebGL / Canvas.
- Color-coded node topology:
  - 🔴 **Red:** Confirmed Mule Accounts (Risk > 0.85).
  - 🟠 **Orange:** Layer-2/3 Intermediary Nodes.
  - 🔵 **Cyan:** Transaction nodes with directional flow indicators.
  - 🟣 **Purple:** Hardware devices and IMEI clusters.
  - 🟢 **Green:** Verified Legitimate Accounts (Anti-Overblocking).
- Dynamic hop expansion: Investigators can click any node to expand 1-hop or 2-hop neighborhoods in sub-seconds.

### 3.6 Requirement 6: Law Enforcement Investigation Dashboard & Evidentiary Dossier
- Real-time priority alerts ranked by financial exposure and flight risk.
- **Court-Ready Evidentiary Dossier:**
  - Automated generation of Section 65B Indian Evidence Act compliant digital certificates.
  - Ready-to-serve Section 91 CrPC notice templates for bank nodal officers.
  - Automated Layer-1 and Layer-2 bank account freeze requests formatted for 1930 / CFCFRMS integration.
  - Suspicious Activity Report (SAR) compliant with FIU-IND regulatory guidelines.

---

## 4. LangGraph 8-Node Autonomous Investigation Agent

```text
                            [START INTAKE]
                                  │
                                  ▼
                           [trigger_node]
                 - Ingests 1930 alert or banking trigger
                 - Validates transaction ID & baseline risk
                                  │
                                  ▼
                         [investigate_node]
                 - Executes TigerGraph native GSQL queries
                 - Traverses 1-hop & 2-hop topological BFS
                                  │
                                  ▼
                       [gather_evidence_node]
                 - Evaluates shared device hardware fingerprints
                 - Computes velocity bursts & money mule links
                 - Correlates NCRP cyber complaint records
                                  │
                                  ▼
             ┌────────► [assess_uncertainty_node] ◄──────────────┐
             │   - Calculates Shannon entropy H(p)               │
             │   - Evaluates MDL Sufficiency Metric              │
             │   - Assesses uncertainty score                    │
             │                   │                               │
             │            (should_gather_more)                   │
             │              /            \                       │
             │   [MDL < 0.35 or iter>=3]  [MDL >= 0.35]          │
             │         /                      \                  │
             │     [proceed]              [gather_more]          │
             │        │                         │                │
             │        │                         ▼                │
             │        │            [gather_more_evidence_node] ──┘
             │        │            - Deep 4-hop money flow BFS
             │        │            - Cross-district syndicate ring scan
             │        ▼
             │   [action_node]
             │   - Evaluates Bihar Police Cyber SOP Matrix
             │   - Escalates: TIER_1_FREEZE -> SP_CYBER_APPROVAL
             │   - Triggers 1930 CFCFRMS immediate debit freeze
             │        │
             │        ▼
             │   [explain_node]
             │   - Prompts Gemini 2.5 Flash for forensic narrative
             │   - Compiles Section 65B IEA / FIU-IND dossier
             │   - Generates case_record.json audit trail
             │        │
             │        ▼
             │   [memory_node]
             │   - Generates 384-d normalized vector embeddings
             │   - Stores resolved case memory in GraphRAG
             │        │
             │        ▼
             └───── [END]
```

---

## 5. Information-Theoretic Minimum Description Length (MDL) Stopping Gate

In graph-augmented agentic systems, LLMs exhibit a propensity to enter indefinite search loops—repeatedly querying adjacent hops to achieve zero uncertainty. In high-stakes law enforcement operations, every graph traversal introduces latency while adding diminishing marginal diagnostic value.

FraudSight formulates optimal stopping using **Minimum Description Length (MDL)** principles:

$$H(p) = -p \log_2(p) - (1-p) \log_2(1-p)$$

$$S(p, C, k) = \left( \frac{H(p)}{\log_2(2)} \right) \cdot \left( 1 + \frac{C}{10} \right)^{-1} \cdot e^{-0.1 \cdot k}$$

Where:
- $p \in [0, 1]$: Current estimated mule probability.
- $H(p) \in [0, 1]$: Binary Shannon entropy.
- $C$: Cumulative cost of gathered evidence.
- $k$: Traversal iteration counter.

**Decision Gate Logic:**
- If $S(p, C, k) < 0.35$ or $k \ge 3$: **HALT INVESTIGATION**. Evidence is sufficient to substantiate freeze action under Section 66D IT Act.
- If $S(p, C, k) \ge 0.35$: **DEEP EXPANSION**. Continue 3-hop traversal to identify coordinating kingpin nodes.

---

## 6. Anti-Overblocking Customer Protection Filter

A critical flaw in standard mule detection algorithms is wrongful freezing of innocent citizens (e.g. students, gig workers, small traders). FraudSight implements an automated **Customer Protection Filter**:
- Tests for legitimate behavioral archetypes before debit freeze execution.
- Checks: recurring utility bill payments, verified payroll credits, longstanding tenure (>3 years), trusted personal hardware history.
- If legitimate indicators outweigh fraud signals, downgrades action from `IMMEDIATE_DEBIT_FREEZE` to `ENHANCED_KYC_VERIFICATION`, preventing harassment of innocent account holders.

---

## 7. Compliance & Legal Standard Adherence

All investigation outputs conform to Indian statutory and regulatory standards:
1. **Section 66D Information Technology Act, 2000:** Punishment for cheating by personation using computer resources.
2. **Section 91 Criminal Procedure Code (CrPC):** Summons to produce documents or electronic records.
3. **Section 65B Indian Evidence Act (IEA):** Admissibility of electronic records with cryptographic hash integrity (SHA-256).
4. **CFCFRMS / 1930 SOPs:** Instant debit freeze messaging protocol for Layer-1 and Layer-2 beneficiary accounts.
5. **FIU-IND Suspicious Transaction Report (STR):** Formatted electronic XML/JSON reporting for AML surveillance.
