"""
OutreachContentAgent: Generate personalized messages (mock).
Replace with OpenAI calls (openai.ChatCompletion or openai.Chat API).
"""

from .base_agent import BaseAgent


class OutreachContentAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        ranked = inputs.get("ranked_leads", []) or []
        persona = inputs.get("persona", "SDR")
        tone = inputs.get("tone", "friendly")
        messages = []
        for lead in ranked:
            subj = f"Quick question about {lead.get('company')}"
            body = (
                f"Hi {lead.get('contact_name')},\n\n"
                f"I'm an SDR at Analytos.ai — we help {lead.get('company')} find qualified buyers by enriching signals like hiring and funding. "
                f"Given your role as {lead.get('role')}, I thought it'd be useful to share a quick 15-minute idea.\n\n"
                f"Would you be open to a short call?\n\nBest,\nSDR"
            )
            messages.append({
                "lead_id": lead.get("email"),
                "email_subject": subj,
                "email_body": body
            })
        return {"messages": messages}

