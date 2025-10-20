"""
DataEnrichmentAgent (mock).
Replace with Clearbit / PeopleDataLabs calls.
"""

from .base_agent import BaseAgent


class DataEnrichmentAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        leads = inputs.get("leads", [])
        enriched = []
        for l in leads:
            # MOCK: add role, company_size, and detected technologies
            enriched.append({
                "company": l.get("company"),
                "contact_name": l.get("contact_name"),
                "email": l.get("email"),
                "role": "CEO" if "Alice" in l.get("contact_name", "") else "Head of Sales",
                "company_size": 250,
                "revenue_estimate": 50000000,
                "technologies": ["Stripe", "AWS"]
            })
        return {"enriched_leads": enriched}
