"""
Workflow schema validation (light).
For production, replace with a robust jsonschema definition and use jsonschema.validate.
"""

def validate_workflow_schema(workflow: dict):
    assert "workflow_name" in workflow
    assert "steps" in workflow and isinstance(workflow["steps"], list)
    # very light checks for each step
    for s in workflow["steps"]:
        assert "id" in s and "agent" in s

