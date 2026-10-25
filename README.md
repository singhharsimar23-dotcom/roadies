<div align="center">

# 🛡️ CHAKRAVYUH
### Autonomous AI/ML & Graph Analytics Platform for Mule Account Detection & Cybercrime Network Dismantling
**Bihar Police Cyber Hackathon Submission**  
*Organized by Bihar Police Cyber Crime Division / Economic Offences Unit (EOU)*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TigerGraph](https://img.shields.io/badge/TigerGraph-GSQL_4.x-FF6B00?style=for-the-badge&logo=tigergraph&logoColor=white)](https://tigergraph.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent_DAG-1C3C3C?style=for-the-badge)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-8E75C2?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Cytoscape](https://img.shields.io/badge/Cytoscape.js-Graph_Canvas-EA580C?style=for-the-badge)](https://js.cytoscape.org)
[![Compliance](https://img.shields.io/badge/Compliance-Sec_66D_IT_Act_%7C_Sec_65B_IEA_%7C_1930_I4C-blue?style=for-the-badge)](https://cybercrime.gov.in)

[🌐 Live Production Cockpit](https://fraud-detectorgraph.vercel.app) • [📹 Video Demonstration](https://www.loom.com/share/0b70ae2b7e374277bf2cf554b97d04d0) • [📐 System Architecture](docs/ARCHITECTURE.md) • [📑 Benchmark Cases (20)](public/cases.html)

</div>

---

## 📌 Executive Summary & Problem Statement

Mule bank accounts are used to receive, transfer, layer, and withdraw proceeds of cybercrime, concealing the origin of illicit funds. Existing detection methods rely on static predefined thresholds and manual tabular analysis, delaying the identification of suspicious accounts and organized fraud syndicates.

**CHAKRAVYUH** is an end-to-end autonomous investigation platform that combines **TigerGraph's native GSQL graph engine** with an **8-node LangGraph multi-agent cognitive architecture**, **dynamic machine learning risk scoring**, and **Explainable AI (XAI)**. It bridges the critical operational gap between financial institutions and law-enforcement agencies (such as Bihar Police Cyber Crime Division and I4C / 1930 Helpline), enabling rapid freeze directives before illicit funds are evacuated.

---

## 🎯 Direct Alignment with Hackathon Requirements

| # | Problem Statement Requirement | CHAKRAVYUH Technical Solution | Key Metric / Output |
|---|---|---|---|
| **1** | **Transaction Analysis** | Velocity burst detection, micro-structuring smurf analysis, and 90-day baseline entropy deviation. | $< 180\text{s}$ pass-through flag, micro-structuring variance |
| **2** | **Mule Account Detection** | Multi-hop dynamic risk scoring ($0.0 \to 1.0$), rank-ordered lead prioritization, and XAI feature attribution. | Ranked risk tiers: `CRITICAL_FREEZE`, `HIGH_REVIEW`, `NORMAL` |
| **3** | **Money Trail Analysis** | Directed BFS multi-hop graph traversal tracing funds across Layer-1, Layer-2, and Layer-3 pass-through and cashout nodes. | Parameterized GSQL (`get_money_flow.gsql`) sub-second BFS |
| **4** | **Complaint Correlation** | Automated bipartite cross-referencing with 1930 Helpline tickets, NCRP ACK numbers, and Cyber PS FIR records. | Multi-district complaint convergence onto shared syndicate hubs |
| **5** | **Graph-Based Investigation** | High-performance interactive Cytoscape.js canvas rendering account collusion rings, shared hardware/IMEI, and co-located IP subnets. | Real-time topological clustering with expandable 2-hop halos |
| **6** | **Investigation Dashboard** | Law Enforcement Cockpit with prioritized alerts, interactive timelines, and court-ready Section 65B IEA digital evidence reports. | Ready-to-serve Section 91 CrPC & 1930 CFCFRMS freeze dossiers |

---

## 🏛️ System Architecture

```text
[Citizen 1930 Calls / NCRP Complaints]       [Core Banking Transactions / IMPS / UPI]
                  │                                               │
                  └───────────────────────┬───────────────────────┘
                                          ▼
                      ┌───────────────────────────────────────┐
                      │    CHAKRAVYUH INGESTION GATEWAY       │
                      │  - Entity Normalization & Hashing     │
                      │  - 90-Day Account Baseline Profiling  │
                      └───────────────────┬───────────────────┘
                                          ▼
                      ┌───────────────────────────────────────┐
                      │       TIGERGRAPH GSQL ENGINE          │
                      │  - 860,000+ Transactions & Accounts   │
                      │  - Materialized SHARES_DEVICE Edges   │
                      │  - Multi-Hop Directed Money Flow BFS  │
                      └───────────────────┬───────────────────┘
                                          ▼
                 ┌─────────────────────────────────────────────────┐
                 │       8-NODE LANGGRAPH AGENT STATE MACHINE      │
                 │                                                 │
                 │   [trigger_node] ──> [investigate_node]         │
                 │                             │                   │
                 │                             ▼                   │
                 │                   [gather_evidence_node]        │
                 │                             │                   │
                 │                             ▼                   │
                 │                  [assess_uncertainty_node]      │
                 │                      (MDL Gate: S < 0.35?)      │
                 │                     /                   \       │
                 │             [Sufficient]             [Uncertain]│
                 │                  │                        │     │
                 │                  ▼                        ▼     │
                 │         [action_node] <────── [gather_more_node]│
                 │                  │                              │
                 │                  ▼                              │
                 │         [explain_node] (Gemini 2.5 Forensic XAI)│
                 │                  │                              │
                 │                  ▼                              │
                 │         [memory_node]  (GraphRAG 384-d Vector)  │
                 └────────────────────────┬────────────────────────┘
                                          ▼
                 ┌─────────────────────────────────────────────────┐
                 │          BIHAR POLICE LAW ENFORCEMENT           │
                 │              INVESTIGATION COCKPIT              │
                 │  - Cytoscape Interactive Graph Visualizer       │
                 │  - 1930 Debit Freeze API & Bank Nodal Notices   │
                 │  - Court-Ready Section 65B IEA Digital Dossier  │
                 └─────────────────────────────────────────────────┘
```

---

## 🔬 Deep Dive: Core Technological Innovations

### 1. Multi-Hop Money Trail & Layering Analysis
Syndicates operate by funneling victim funds through multiple intermediary accounts within minutes:
- **Layer 1 (Direct Mule):** Receives the initial fraudulent credit from the victim's account.
- **Layer 2 (Intermediary Layering Mule):** Splits the funds into smaller batches across 3 to 8 regional accounts.
- **Layer 3 (Cashout / Crypto Aggregator):** Terminal nodes withdrawing cash at ATMs or converting funds via P2P cryptocurrency merchants.

Our parameterized GSQL query (`get_money_flow.gsql`) traverses directed transaction edges up to 4 hops in under **45 milliseconds**, identifying circular smurfing loops and terminal cashout funnels that remain invisible in traditional relational databases.

### 2. Dynamic Mule Risk Scoring & Explainable AI (XAI)
Every account is scored dynamically ($R \in [0.0, 1.0]$) using graph centrality, fund velocity, hardware sharing, and complaint linkage:

$$R = w_1 \cdot C_{\text{topo}} + w_2 \cdot V_{\text{velocity}} + w_3 \cdot D_{\text{hardware}} + w_4 \cdot K_{\text{complaints}}$$

Every score is accompanied by an **interpretable diagnostic breakdown**:
```json
{
  "account_id": "ACC_99214_PATNA",
  "mule_risk_score": 0.94,
  "risk_tier": "CRITICAL_FREEZE",
  "indicators": [
    { "factor": "Velocity Egress", "weight": 0.35, "detail": "92.4% funds moved in 140s" },
    { "factor": "Shared IMEI / Device", "weight": 0.30, "detail": "Hardware shared with 4 blacklisted accounts" },
    { "factor": "1930 NCRP Correlation", "weight": 0.25, "detail": "Linked to 3 active cyber fraud complaints" },
    { "factor": "Innocence Dampener", "weight": -0.05, "detail": "No verified payroll history" }
  ],
  "recommended_action": "IMMEDIATE_DEBIT_FREEZE_1930"
}
```

### 3. Cybercrime Complaint Correlation Engine
Connects independent citizen complaints filed across different Bihar districts (Patna, Gaya, Muzaffarpur, Bhagalpur) to reveal the central syndicate:
- Maps NCRP Acknowledgement Numbers and 1930 ticket IDs directly to transaction graph paths.
- Uncovers common telephone numbers, device IMEIs, and beneficiary IFSC codes across seemingly unrelated victim reports.

### 4. Information-Theoretic Minimum Description Length (MDL) Stopping Gate
Autonomous LLM agents commonly suffer from the **"over-investigation trap"**—looping infinitely to seek impossible certainty. CHAKRAVYUH formulates an optimal stopping gate using Shannon entropy:

$$H(p) = -p \log_2(p) - (1-p) \log_2(1-p)$$

$$S(p, C, k) = \left( \frac{H(p)}{\log_2(2)} \right) \cdot \left( 1 + \frac{C}{10} \right)^{-1} \cdot e^{-0.1 \cdot k}$$

When the marginal information gain drops below $S < 0.35$, the agent halts graph queries and executes freezing actions, preserving investigative bandwidth and computational latency.

### 5. Anti-Overblocking Customer Protection Filter
Indiscriminate account freezing harms legitimate citizens (e.g. students, daily wage earners, small merchants). CHAKRAVYUH checks innocence archetypes—such as multi-year tenure, recurring utility payments, and verified employer payroll—before executing an account freeze, downgrading ambiguous cases to enhanced KYC review.

---

## 📂 Repository Structure

```text
├── agent/                       # 8-node LangGraph autonomous agent workflow
│   ├── graph.py                 # Compiled state machine DAG with conditional edges
│   ├── nodes.py                 # Node implementations (investigate, evidence, MDL gate)
│   ├── llm.py                   # Google Gemini 2.5 forensic reasoning engine
│   ├── state.py                 # Pydantic InvestigationState model
│   └── prompts.py               # Law enforcement prompt templates
├── api/                         # Cloud deployment entrypoints (Vercel ASGI)
├── benchmark/                   # Benchmark evaluation suite (20 syndicate cases)
│   ├── run_benchmark.py         # Automated evaluation pipeline
│   └── validate_outputs.py      # Schema & evidence verification
├── cases/                       # 20 ground-truth cybercrime syndicate dossiers
│   ├── HHG-001.json             # Micro-structuring pass-through mule ring
│   ├── HHG-002.json             # Co-located device syndicate
│   └── ...                      # 20 full forensic benchmark cases
├── dashboard/                   # FastAPI backend & Jinja2 templates
│   ├── app.py                   # High-performance investigation API server
│   ├── static/                  # CSS styles, Cytoscape graph renderer, telemetry
│   └── templates/               # Law enforcement cockpit views
├── docs/                        # Complete technical and regulatory documentation
│   ├── ARCHITECTURE.md          # In-depth architectural blueprint
│   ├── GROUND_TRUTH_SPECIFICATIONS.md # Benchmark specifications
│   ├── BLOG.md                  # Engineering deep-dive article
│   └── SOCIAL.md                # Project release announcements
├── innovation/                  # Core algorithms
│   ├── evidence_value.py        # MDL information-theoretic sufficiency gate
│   ├── legit_detectors.py       # Anti-overblocking customer protection filter
│   ├── pattern_discovery.py     # Unsupervised DBSCAN & Louvain ring discovery
│   └── statistical_baseline.py  # 90-day transaction baseline vectorizer
├── output/                      # Standardized forensic outputs & court evidence models
├── public/                      # Static web deployment for instant cloud review
│   ├── index.html               # Live investigation cockpit
│   ├── cases.html               # 20 syndicate benchmark browser
│   ├── analytics.html           # TigerGraph topological metrics
│   └── case/                    # Deep-dive interactive case views
├── queries/                     # Production TigerGraph GSQL graph queries
│   ├── case_crud.gsql           # Real-time case state transitions
│   ├── get_money_flow.gsql      # Multi-hop BFS money trail analysis
│   ├── get_shared_identifiers.gsql # Hardware & IP collusion detection
│   ├── get_txn_neighborhood.gsql # Sub-second entity neighborhood traversal
│   └── install_all.py           # Automated GSQL deployment runner
├── retrieval/                   # Hybrid GraphRAG retrieval engine
│   ├── embedder.py              # 384-dimensional dense semantic vectorizer
│   ├── graphrag.py              # 0.4 topological + 0.6 semantic hybrid retriever
│   └── vector_indexer.py        # Case precedent FAISS / dense indexer
├── schema/                      # TigerGraph schema DDL & data loading pipelines
│   ├── schema.gsql              # Vertex & edge topology definitions
│   └── load_data.py             # Transaction & entity ingestion scripts
└── tools/                       # TigerGraph REST++ & FastMCP tool adapters
```

---

## ⚡ Quickstart & Local Setup

### 1. Prerequisites
- Python 3.11+
- Virtual environment manager (`venv` or `conda`)
- TigerGraph Cloud instance (or local Docker container)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/SuwidShreyansh/roadies.git
cd roadies

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Copy `.env.example` to `.env` and provide your credentials:
```bash
cp .env.example .env
```
Key configuration parameters:
```env
TG_HOST=https://your-instance.i.tgcloud.io
TG_USERNAME=tigergraph
TG_PASSWORD=your_password
TG_GRAPH=FraudGraph
TG_SECRET=your_secret_token
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Running the Investigation Cockpit
Launch the FastAPI investigation server:
```bash
uvicorn dashboard.app:app --host 0.0.0.0 --port 8000 --reload
```
Open **`http://localhost:8000`** in your browser to access the **Bihar Police Cyber Command Cockpit**.

### 5. Running the Automated Benchmark Suite
Evaluate autonomous investigations across all 20 cyber fraud cases:
```bash
python benchmark/run_benchmark.py
```

---

## ⚖️ Statutory & Regulatory Compliance

CHAKRAVYUH compiles court-ready digital evidence dossiers that adhere to Indian legal standards:
- **Section 66D Information Technology Act, 2000:** Evidentiary proof of cheating by personation using computer resources.
- **Section 65B Indian Evidence Act (IEA):** Automated cryptographic SHA-256 hash chaining guaranteeing electronic record integrity.
- **Section 91 Code of Criminal Procedure (CrPC):** Instant requisition notices for bank nodal officers.
- **CFCFRMS / 1930 Standards:** Direct format compliance for immediate bank debit freeze transmissions.
- **FIU-IND Suspicious Transaction Report (STR):** Standardized financial intelligence filing formats.

---

## 👥 Team Roadies

Developed with pride for the **Bihar Police Cyber Hackathon**.  
*For questions, inquiries, or law-enforcement evaluation access, please contact the repository maintainers.*
