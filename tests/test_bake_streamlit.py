from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture
def baked_project(tmp_path: Path) -> Path:
    """Fixture to generate a project using Cookiecutter."""

    app_type = "streamlit"
    output_dir = tmp_path / app_type
    cookiecutter(
        ".",
        no_input=True,
        extra_context={"app_type": app_type},
        output_dir=output_dir,
    )
    return output_dir


def test_project_baked(baked_project):
    """Check if the project was baked successfully."""

    project_dir = baked_project / "new_project"
    readme = project_dir / "README.md"
    tasks_json = project_dir / ".vscode" / "tasks.json"
    dockerfile = project_dir / "Dockerfile"

    assert readme.exists()
    assert tasks_json.exists()
    assert dockerfile.exists()
