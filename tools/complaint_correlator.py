"""
tools/complaint_correlator.py — Bihar Police 1930 Helpline & NCRP Complaint Correlation Engine

This module implements Pillar 4 of the Bihar Police Cyber Hackathon requirements:
  "Correlate financial transactions with multiple cybercrime complaints to identify
   related incidents, accounts, and entities."

How it works:
  Citizens who lose money to cyber fraud (UPI scams, investment fraud, digital arrest,
  romance scams, etc.) file complaints via:
    - 1930 National Cybercrime Helpline (immediate helpline call)
    - NCRP (National Cybercrime Reporting Portal) — gives an ACK number
    - Local Cyber Police Station — FIR registration

  The correlator maps these complaint references BACK to the bank accounts that received
  the victim's money, enabling Bihar Police to:
    (a) Identify which accounts are actively receiving fraud proceeds
    (b) Group multiple unrelated victim complaints that actually share the same mule account
    (c) Build "syndicate profiles" by clustering co-appearing accounts across many complaints

Usage:
    from tools.complaint_correlator import ComplaintCorrelator
    correlator = ComplaintCorrelator()

    # Find all accounts linked to a complaint
    results = correlator.get_accounts_for_complaint("NCRP/BH/2024/001234")

    # Find all complaints that reference a bank account
    complaints = correlator.get_complaints_for_account("9876543210")

    # Find the syndicate hub: accounts appearing in 3+ complaints
    hubs = correlator.find_syndicate_hubs(min_complaint_count=3)
"""

import json
import re
from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime


# ---------------------------------------------------------------------------
# Static complaint-to-account correlation database
# In production: queried live from TigerGraph CybercrimeComplaint vertices
# Here: pre-populated from Bihar Police sample dataset for Vercel demo
# ---------------------------------------------------------------------------

# Format: Each complaint contains the accounts it directly names as fraudulent recipients
COMPLAINT_REGISTRY: List[Dict[str, Any]] = [
    {
        "complaint_ref": "NCRP/BH/2024/001234",
        "ticket_1930": "1930-BH-2024-091422",
        "fir_number": "FIR/PATNA-CYBER/2024/0078",
        "district": "Patna",
        "complainant_name": "Ramesh Kumar",
        "victim_loss_inr": 45000.0,
        "fraud_category": "Digital Arrest Fraud",
        "incident_date": "2024-09-14",
        "accounts_implicated": ["9876543210_SBI", "9123456789_PNB"],
        "upi_handles": ["pay.scam@axl", "fake.officer@ybl"],
        "imei_devices": ["869234058162847"],
        "narrative": "Victim received call from person posing as CBI officer. Transferred ₹45,000 to avoid fake 'arrest warrant'.",
    },
    {
        "complaint_ref": "NCRP/BH/2024/002891",
        "ticket_1930": "1930-BH-2024-092981",
        "fir_number": "FIR/GAYA-CYBER/2024/0034",
        "district": "Gaya",
        "complainant_name": "Sunita Devi",
        "victim_loss_inr": 120000.0,
        "fraud_category": "Fake Investment Platform",
        "incident_date": "2024-09-29",
        "accounts_implicated": ["9123456789_PNB", "8765432101_HDFC"],
        "upi_handles": ["invest.profit@axl"],
        "imei_devices": ["869234058162847", "354812093847561"],
        "narrative": "Victim lured into fake stock trading app. Transferred ₹1,20,000 in multiple UPI payments over 12 days.",
    },
    {
        "complaint_ref": "NCRP/BH/2024/003445",
        "ticket_1930": "1930-BH-2024-094512",
        "fir_number": "FIR/MUZAFFARPUR-CYBER/2024/0019",
        "district": "Muzaffarpur",
        "complainant_name": "Anil Singh",
        "victim_loss_inr": 78500.0,
        "fraud_category": "OTP Phishing",
        "incident_date": "2024-10-02",
        "accounts_implicated": ["7654321098_AXIS", "9123456789_PNB"],
        "upi_handles": ["otp.verify@ybl"],
        "imei_devices": ["354812093847561"],
        "narrative": "Victim received SMS claiming KYC expiry. Shared OTP; ₹78,500 transferred from savings account.",
    },
    {
        "complaint_ref": "NCRP/BH/2024/004122",
        "ticket_1930": "1930-BH-2024-095891",
        "fir_number": "FIR/BHAGALPUR-CYBER/2024/0042",
        "district": "Bhagalpur",
        "complainant_name": "Priya Sharma",
        "victim_loss_inr": 35000.0,
        "fraud_category": "Romance Scam",
        "incident_date": "2024-10-08",
        "accounts_implicated": ["8765432101_HDFC", "6543210987_ICICI"],
        "upi_handles": ["army.gift@axl"],
        "imei_devices": [],
        "narrative": "Victim deceived via matrimonial app by person claiming to be Army officer. Transferred ₹35,000 as 'customs clearance'.",
    },
    {
        "complaint_ref": "NCRP/BH/2024/005678",
        "ticket_1930": "1930-BH-2024-097234",
        "fir_number": None,  # Complaint filed before FIR stage
        "district": "Nalanda",
        "complainant_name": "Manoj Paswan",
        "victim_loss_inr": 60000.0,
        "fraud_category": "Fake Job Offer",
        "incident_date": "2024-10-15",
        "accounts_implicated": ["6543210987_ICICI", "9876543210_SBI"],
        "upi_handles": ["jobs.fee@oksbi"],
        "imei_devices": ["869234058162847"],
        "narrative": "Victim paid ₹60,000 as 'security deposit' for a fake government job offered over WhatsApp.",
    },
]


class ComplaintCorrelator:
    """
    Maps 1930/NCRP complaint references to bank accounts and vice versa.
    Identifies mule accounts that appear across multiple independent victim complaints —
    these are almost certainly part of an organized fraud syndicate.
    """

    def __init__(self):
        self._registry = COMPLAINT_REGISTRY
        # Build reverse index: account_id → [complaint_refs]
        self._account_to_complaints: Dict[str, List[str]] = {}
        self._account_to_imei: Dict[str, List[str]] = {}
        for complaint in self._registry:
            for acct in complaint["accounts_implicated"]:
                if acct not in self._account_to_complaints:
                    self._account_to_complaints[acct] = []
                    self._account_to_imei[acct] = []
                self._account_to_complaints[acct].append(complaint["complaint_ref"])
                for imei in complaint["imei_devices"]:
                    if imei not in self._account_to_imei[acct]:
                        self._account_to_imei[acct].append(imei)

    def get_accounts_for_complaint(self, complaint_ref: str) -> Dict[str, Any]:
        """
        Given a complaint reference (NCRP ACK, 1930 ticket, or FIR number),
        return all bank accounts implicated in that complaint.
        """
        # Normalize: allow partial match on NCRP ref, 1930 ticket, or FIR
        for complaint in self._registry:
            if (
                complaint["complaint_ref"] == complaint_ref
                or complaint["ticket_1930"] == complaint_ref
                or complaint.get("fir_number") == complaint_ref
            ):
                return {
                    "found": True,
                    "complaint_ref": complaint["complaint_ref"],
                    "ticket_1930": complaint["ticket_1930"],
                    "fir_number": complaint.get("fir_number"),
                    "district": complaint["district"],
                    "fraud_category": complaint["fraud_category"],
                    "victim_loss_inr": complaint["victim_loss_inr"],
                    "incident_date": complaint["incident_date"],
                    "accounts_implicated": complaint["accounts_implicated"],
                    "upi_handles": complaint["upi_handles"],
                    "imei_devices": complaint["imei_devices"],
                    "narrative": complaint["narrative"],
                    "accounts_detail": [
                        {
                            "account_id": acct,
                            "also_appears_in": [
                                r for r in self._account_to_complaints.get(acct, [])
                                if r != complaint["complaint_ref"]
                            ],
                            "shared_imei": self._account_to_imei.get(acct, []),
                            "cross_district_count": len(
                                self._account_to_complaints.get(acct, [])
                            ),
                        }
                        for acct in complaint["accounts_implicated"]
                    ],
                }
        return {"found": False, "complaint_ref": complaint_ref, "accounts_implicated": []}

    def get_complaints_for_account(self, account_id: str) -> Dict[str, Any]:
        """
        Given a bank account ID, return all complaints that reference it.
        If 3+ complaints reference the same account across different districts,
        this account is a high-confidence syndicate hub.
        """
        complaint_refs = self._account_to_complaints.get(account_id, [])
        complaints_detail = []
        total_loss_inr = 0.0
        districts = set()

        for complaint in self._registry:
            if account_id in complaint["accounts_implicated"]:
                complaints_detail.append({
                    "complaint_ref": complaint["complaint_ref"],
                    "ticket_1930": complaint["ticket_1930"],
                    "fir_number": complaint.get("fir_number"),
                    "district": complaint["district"],
                    "fraud_category": complaint["fraud_category"],
                    "victim_loss_inr": complaint["victim_loss_inr"],
                    "incident_date": complaint["incident_date"],
                })
                total_loss_inr += complaint["victim_loss_inr"]
                districts.add(complaint["district"])

        complaint_count = len(complaints_detail)

        # Risk classification based on complaint frequency
        if complaint_count >= 3:
            risk_tier = "CRITICAL_FREEZE"
            risk_label = "Confirmed Syndicate Hub — Immediate debit freeze via 1930 CFCFRMS"
        elif complaint_count == 2:
            risk_tier = "HIGH_REVIEW"
            risk_label = "Multi-Complaint Mule — Freeze with bank nodal officer notice"
        elif complaint_count == 1:
            risk_tier = "MEDIUM_WATCH"
            risk_label = "Single Complaint — Enhanced KYC and account monitoring"
        else:
            risk_tier = "CLEAR"
            risk_label = "No complaints found for this account"

        return {
            "account_id": account_id,
            "complaint_count": complaint_count,
            "total_victim_loss_inr": total_loss_inr,
            "districts_involved": list(districts),
            "risk_tier": risk_tier,
            "risk_label": risk_label,
            "shared_imei": self._account_to_imei.get(account_id, []),
            "complaints": complaints_detail,
        }

    def find_syndicate_hubs(self, min_complaint_count: int = 2) -> List[Dict[str, Any]]:
        """
        Find all accounts that appear in min_complaint_count or more independent complaints.
        These are the central mule hubs — the accounts that syndicates route funds through
        across many different victims and districts.
        Returns sorted by complaint count descending (highest-risk first).
        """
        hubs = []
        for account_id, complaint_refs in self._account_to_complaints.items():
            if len(complaint_refs) >= min_complaint_count:
                result = self.get_complaints_for_account(account_id)
                hubs.append(result)

        hubs.sort(key=lambda x: x["complaint_count"], reverse=True)
        return hubs

    def correlate_by_imei(self, imei: str) -> Dict[str, Any]:
        """
        Find all complaints and accounts linked to a specific IMEI/device.
        Syndicates often use the same phone to open multiple mule accounts.
        """
        linked_accounts = []
        linked_complaints = []
        total_loss = 0.0

        for complaint in self._registry:
            if imei in complaint["imei_devices"]:
                linked_complaints.append(complaint["complaint_ref"])
                for acct in complaint["accounts_implicated"]:
                    if acct not in linked_accounts:
                        linked_accounts.append(acct)
                total_loss += complaint["victim_loss_inr"]

        return {
            "imei": imei,
            "linked_accounts": linked_accounts,
            "linked_complaints": linked_complaints,
            "total_victim_loss_inr": total_loss,
            "risk_assessment": "HIGH — IMEI shared across multiple complaints indicates same operator controlling multiple mule accounts"
            if len(linked_complaints) >= 2
            else "MEDIUM — Single complaint link, monitor for further activity",
        }

    def get_portfolio_summary(self) -> Dict[str, Any]:
        """
        Portfolio-level summary of complaint correlations.
        Used by the Bihar Police command dashboard.
        """
        total_complaints = len(self._registry)
        total_loss_inr = sum(c["victim_loss_inr"] for c in self._registry)
        syndicate_hubs = self.find_syndicate_hubs(min_complaint_count=2)
        districts = set(c["district"] for c in self._registry)
        categories = {}
        for c in self._registry:
            cat = c["fraud_category"]
            categories[cat] = categories.get(cat, 0) + 1

        return {
            "total_complaints_loaded": total_complaints,
            "total_victim_loss_inr": total_loss_inr,
            "districts_covered": list(districts),
            "fraud_categories": categories,
            "syndicate_hub_accounts": len(syndicate_hubs),
            "top_hubs": syndicate_hubs[:3],
        }


# ---------------------------------------------------------------------------
# Module-level singleton
# ---------------------------------------------------------------------------
_correlator_instance: Optional[ComplaintCorrelator] = None


def get_correlator() -> ComplaintCorrelator:
    """Return a shared ComplaintCorrelator singleton."""
    global _correlator_instance
    if _correlator_instance is None:
        _correlator_instance = ComplaintCorrelator()
    return _correlator_instance


# ---------------------------------------------------------------------------
# Quick CLI test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    correlator = ComplaintCorrelator()

    print("=== COMPLAINT CORRELATOR — Bihar Police Demo ===\n")

    # Test 1: Look up accounts for a specific NCRP complaint
    result = correlator.get_accounts_for_complaint("NCRP/BH/2024/001234")
    print(f"Accounts linked to NCRP/BH/2024/001234:")
    print(json.dumps(result, indent=2))

    # Test 2: Look up all complaints for a shared mule account
    print(f"\nComplaints referencing account 9123456789_PNB:")
    acct_result = correlator.get_complaints_for_account("9123456789_PNB")
    print(json.dumps(acct_result, indent=2))

    # Test 3: Find syndicate hubs (accounts in 2+ complaints)
    print(f"\nSyndicate Hub Accounts (appearing in 2+ complaints):")
    hubs = correlator.find_syndicate_hubs(min_complaint_count=2)
    for hub in hubs:
        print(f"  {hub['account_id']}: {hub['complaint_count']} complaints, "
              f"₹{hub['total_victim_loss_inr']:,.0f} victim loss, "
              f"Districts: {', '.join(hub['districts_involved'])}")

    # Test 4: Portfolio summary
    print(f"\nPortfolio Summary:")
    summary = correlator.get_portfolio_summary()
    print(json.dumps(summary, indent=2, default=str))
