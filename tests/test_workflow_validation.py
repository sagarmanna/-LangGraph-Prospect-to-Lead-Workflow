import json
from utils.schemas import validate_workflow_schema

def test_workflow_load_and_validate():
    with open("workflow.json", "r") as f:
        w = json.load(f)
    validate_workflow_schema(w)
    print("workflow validated")
