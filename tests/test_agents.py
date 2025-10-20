from agents.prospect_search import ProspectSearchAgent
from agents.enrichment import DataEnrichmentAgent
from agents.scoring import ScoringAgent
from agents.outreach_content import OutreachContentAgent
from agents.outreach_executor import OutreachExecutorAgent
from agents.response_tracker import ResponseTrackerAgent
from agents.feedback_trainer import FeedbackTrainerAgent

def test_agents_basic_flow():
    # run each agent with mock data
    ps = ProspectSearchAgent()
    out1 = ps.run({})
    assert "leads" in out1

    enr = DataEnrichmentAgent()
    out2 = enr.run({"leads": out1["leads"]})
    assert "enriched_leads" in out2

    sc = ScoringAgent()
    out3 = sc.run({"enriched_leads": out2["enriched_leads"], "scoring_criteria": {"weights": {"revenue": 0.3}}})
    assert "ranked_leads" in out3

    oc = OutreachContentAgent()
    out4 = oc.run({"ranked_leads": out3["ranked_leads"]})
    assert "messages" in out4

    oe = OutreachExecutorAgent()
    out5 = oe.run({"messages": out4["messages"]})
    assert "campaign_id" in out5

    rt = ResponseTrackerAgent()
    out6 = rt.run({"campaign_id": out5["campaign_id"]})
    assert "responses" in out6

    ft = FeedbackTrainerAgent()
    out7 = ft.run({"responses": out6["responses"], "config": {}})
    assert "recommendations" in out7

    print("All mock agents ran OK")
