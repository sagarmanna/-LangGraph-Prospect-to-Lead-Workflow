"""
FeedbackTrainerAgent: Analyze campaign results and write recommendations (mock).
Replace Google Sheets write logic using gspread or Google Sheets API.
"""

from .base_agent import BaseAgent


class FeedbackTrainerAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        responses = inputs.get("responses", []) or []
        config = inputs.get("config", {})
        total = len(responses)
        replies = len([r for r in responses if r.get("event") == "reply"])
        open_events = len([r for r in responses if r.get("event") == "open"])
        recommendations = []
        reply_rate = (replies / max(total, 1)) if total else 0.0
        open_rate = (open_events / max(total, 1)) if total else 0.0

        if reply_rate < 0.05:
            recommendations.append({
                "area": "subject_line",
                "suggestion": "Test subject lines focusing on urgent pain points (e.g., 'Cut sales cycle by 20%')"
            })
        if open_rate < 0.15:
            recommendations.append({
                "area": "sender",
                "suggestion": "Try sending from a named account (e.g., 'Jane from Analytos.ai') or vary send times"
            })
        # MOCK: write to Google Sheets -> just echo recommendations
        return {"recommendations": recommendations, "metrics": {"total": total, "replies": replies, "open_rate": open_rate, "reply_rate": reply_rate}}
