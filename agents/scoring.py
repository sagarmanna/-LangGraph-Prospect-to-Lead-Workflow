"""
ScoringAgent: assigns scores to enriched leads according to scoring config.
"""

from .base_agent import BaseAgent


class ScoringAgent(BaseAgent):
    def run(self, inputs: dict) -> dict:
        enriched = inputs.get("enriched_leads", [])
        scoring_cfg = inputs.get("scoring_criteria", {"weights": {}})
        weights = scoring_cfg.get("weights", {})
        ranked = []
        for e in enriched:
            score = 0.0
            # revenue
            rev = e.get("revenue_estimate", 0)
            if rev >= 20000000:
                score += weights.get("revenue", 0)
            # company size
            size = e.get("company_size", 0)
            if 100 <= size <= 1000:
                score += weights.get("employee_count", 0)
            # technologies match
            if e.get("technologies"):
                score += weights.get("technologies", 0)
            # signals placeholder (we can't see original signal here; assume true)
            score += weights.get("signals", 0) * 0.5
            e_copy = dict(e)
            e_copy["score"] = round(score, 3)
            ranked.append(e_copy)
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return {"ranked_leads": ranked}
