"""
ResponseTrackerAgent: poll for responses (mock).
Replace by polling SendGrid events, webhooks, or Apollo tracking.
"""

from .base_agent import BaseAgent
import time


class ResponseTrackerAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        campaign_id = inputs.get("campaign_id")
        # MOCK: pretend we observed events
        now = int(time.time())
        responses = [
            {"lead_id": "alice@democo.com", "event": "open", "timestamp": now - 360},
            {"lead_id": "bob@betasoft.com", "event": "reply", "timestamp": now - 120}
        ]
        return {"responses": responses}

