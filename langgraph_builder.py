"""
Simple LangGraph builder + runner (mock mode).
Reads workflow.json and executes agents in sequence.
Replace or extend resolve_input and agent loading logic as needed.
"""

import json
import os
import importlib
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

WORKFLOW_FILE = "workflow.json"


class LangGraphBuilder:
    def __init__(self, workflow_path: str = WORKFLOW_FILE):
        with open(workflow_path, "r") as f:
            self.workflow = json.load(f)
        self.context = {"config": self.workflow.get("config", {})}
        self.logger = logger

    def resolve_input(self, value):
        """
        Resolves simple {{path.reference}} entries against self.context.
        Supports:
         - a string like "{{prospect_search.output.leads}}"
         - nested dicts and lists
        """
        if isinstance(value, str) and value.startswith("{{") and value.endswith("}}"):
            path = value[2:-2].strip().split(".")
            cur = self.context
            for p in path:
                if p == "output":
                    continue
                if isinstance(cur, dict) and p in cur:
                    cur = cur[p]
                else:
                    return None
            return cur
        elif isinstance(value, dict):
            return {k: self.resolve_input(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self.resolve_input(v) for v in value]
        else:
            return value

    def run(self):
        steps = self.workflow.get("steps", [])
        for step in steps:
            step_id = step["id"]
            agent_name = step["agent"]
            self.logger.info(f"=== Running step: {step_id} -> {agent_name} ===")
            # dynamic import; look for agents.<step_id> or agents.<agentname lower>
            try:
                module = importlib.import_module(f"agents.{step_id}")
            except ModuleNotFoundError:
                module = importlib.import_module(f"agents.{agent_name.lower()}")
            AgentClass = getattr(module, agent_name)
            # prepare inputs
            raw_inputs = step.get("inputs", {})
            resolved = {}
            for k, v in raw_inputs.items():
                resolved[k] = self.resolve_input(v)
            # expand tools config (env variable placeholders)
            tools = step.get("tools", [])
            for t in tools:
                cfg = t.get("config", {})
                for ck, cv in cfg.items():
                    if isinstance(cv, str) and cv.startswith("{{") and cv.endswith("}}"):
                        env_key = cv[2:-2].strip()
                        cfg[ck] = os.getenv(env_key)
            agent = AgentClass(config={"step": step, "tools": tools})
            try:
                output = agent.run(resolved or {})
            except Exception as e:
                self.logger.exception("Agent run failed", exc_info=e)
                output = {}
            # store output
            self.context.setdefault(step_id, {})["output"] = output
            self.logger.info(f"Step {step_id} output keys: {list(output.keys())}")

        self.logger.info("Workflow run complete.")
        return self.context


if __name__ == "__main__":
    builder = LangGraphBuilder()
    ctx = builder.run()
    print("Final context snapshot keys:", list(ctx.keys()))
