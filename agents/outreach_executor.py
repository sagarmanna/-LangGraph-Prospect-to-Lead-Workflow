"""
OutreachExecutorAgent: sends messages (mock).
Replace with SendGrid or Apollo send API calls.
"""

from .base_agent import BaseAgent
import uuid


class OutreachExecutorAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        messages = inputs.get("messages", []) or []
        sent_status = []
        campaign_id = f"camp_{uuid.uuid4().hex[:8]}"
        for m in messages:
            # MOCK: pretend we queued the email
            sent_status.append({"lead_id": m.get("lead_id"), "status": "queued"})
        return {"sent_status": sent_status, "campaign_id": campaign_id}
