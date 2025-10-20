# 🚀 LangGraph Prospect-to-Lead Workflow

![Workflow Diagram](https://via.placeholder.com/800x300?text=LangGraph+Prospect-to-Lead+Workflow+Diagram)  
*Visual representation of the modular AI-driven workflow.*

## Project Overview

This project implements an **autonomous AI-driven prospect-to-lead workflow** using **LangGraph + LangChain**. The system dynamically orchestrates multiple agents to:

- Discover B2B prospects  
- Enrich lead data  
- Score leads according to configurable ICP criteria  
- Generate and send personalized outreach  
- Track responses  
- Optimize campaign performance via feedback  

The workflow is fully configurable via `workflow.json` and is modular, allowing extensions with custom agents, APIs, and scoring logic.

---

## 🧩 Background

- **Target Audience:** B2B companies in the USA with $20M–$200M revenue  
- **Goal:** Automate outbound lead generation and outreach using AI  
- **Approach:** Each workflow step is a modular **LangGraph node** constructed dynamically from JSON configuration

---

## ⚙️ Core Components

| Step | Agent | Description | Tools |
|------|-------|------------|-------|
| Prospect Search | `ProspectSearchAgent` | Searches for companies & contacts matching ICP | Clay API, Apollo API |
| Data Enrichment | `DataEnrichmentAgent` | Enriches leads with LinkedIn / Clearbit data | Clearbit API |
| Scoring | `ScoringAgent` | Scores leads based on configurable criteria | - |
| Outreach Content | `OutreachContentAgent` | Generates personalized email content | OpenAI GPT |
| Send Outreach | `OutreachExecutorAgent` | Sends emails & logs delivery | SendGrid / Apollo API |
| Response Tracking | `ResponseTrackerAgent` | Tracks opens, clicks, replies | Apollo API |
| Feedback Trainer | `FeedbackTrainerAgent` | Analyzes performance & suggests improvements | Google Sheets API |

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/langgraph-prospect-to-lead.git
cd langgraph-prospect-to-lead

# Install dependencies
pip install -r requirements.txt
