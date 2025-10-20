"""
ProspectSearchAgent (Apollo API Integration)
Fetches real B2B contacts using Apollo.io API.
"""

import os
import requests
from dotenv import load_dotenv
from .base_agent import BaseAgent

load_dotenv()

class ProspectSearchAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        self.log("ProspectSearchAgent: inputs=%s", inputs)
        api_key = os.getenv("jaHPQ1bfivOrCkn2uHAgiw")
        if not api_key:
            raise ValueError("Missing APOLLO_API_KEY in .env")

        icp = inputs.get("icp", {})
        industry = icp.get("industry", "Software")
        location = icp.get("location", "USA")

        # Apollo API endpoint
        url = "https://api.apollo.io/v1/mixed_people/search"

        payload = {
            "api_key": api_key,
            "q_keywords": industry,
            "person_locations": [location],
            "page": 1,
            "per_page": 5
        }

        response = requests.post(url, json=payload)
        if response.status_code != 200:
            self.log("Apollo API Error: %s", response.text)
            return {"leads": []}

        data = response.json()
        people = data.get("people", [])
        leads = []
        for p in people:
            leads.append({
                "company": p.get("organization", {}).get("name", "N/A"),
                "contact_name": f"{p.get('first_name', '')} {p.get('last_name', '')}".strip(),
                "email": p.get("email", ""),
                "linkedin": p.get("linkedin_url", ""),
                "signal": "apollo_result"
            })

        self.log(f"Found {len(leads)} leads")
        return {"leads": leads}

