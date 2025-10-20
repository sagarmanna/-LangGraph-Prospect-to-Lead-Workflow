"""
BaseAgent: minimal class all agents inherit from.
Add logging, tool access helpers, and common utilities here.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class BaseAgent:
    def __init__(self, config: dict = None):
        self.config = config or {}
        # tools is list of dicts in config["tools"]
        tools_list = self.config.get("tools", [])
        # convert to dict for easy access
        self.tools = {t["name"]: t.get("config", {}) for t in tools_list}
        self.logger = logger

    def run(self, inputs: dict) -> dict:
        raise NotImplementedError("Agents must implement run(inputs) -> dict")

    def log(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

