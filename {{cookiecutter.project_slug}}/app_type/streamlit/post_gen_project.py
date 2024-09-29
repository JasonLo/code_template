import json
from pathlib import Path

# Inject into devcontainer post_create.sh
POST_CREATE_INJECTION = """
uv add {{cookiecutter.app_type}}
uv tool install {{cookiecutter.app_type}}
"""

# Inject into Dockerfile
DOCKER_INJECTION = """
RUN uv tool install streamlit
CMD ["streamlit", "run", "{{cookiecutter.package_name}}/main.py", "--server.port", "{{cookiecutter.app_port}}"]
"""

# For VSCode tasks.json
DEV_RUN_COMMAND = "streamlit run {{ cookiecutter.package_name }}/main.py"
DOCKER_RUN_COMMAND = "docker build -t {{ cookiecutter.package_name }} . && docker run --rm -p {{cookiecutter.app_port}}:{{cookiecutter.app_port}} {{ cookiecutter.package_name }}"


def make_tasks_json(dev_run_command: str, docker_run_command: str) -> None:
    """Create a tasks.json file for VSCode."""

    tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "dev-run",
                "type": "shell",
                "command": dev_run_command,
            },
            {
                "label": "docker-run",
                "type": "shell",
                "command": docker_run_command,
            },
        ],
    }

    with open(Path(".vscode/tasks.json"), "w") as f:
        f.write(json.dumps(tasks, indent=4))


def inject(file: Path, content: str, placeholder: str = "POST_GEN_INJECTION") -> None:
    """Inject content into a file at the placeholder."""

    with open(file, "r") as f:
        text = f.read()
    text = text.replace(placeholder, content)
    with open(file, "w") as f:
        f.write(text)


def copy(source: Path, destination: Path) -> None:
    """Copy a file from source to destination."""
    with open(source, "r") as f:
        text = f.read()
    with open(destination, "w") as f:
        f.write(text)


def main() -> None:
    copy(
        source=Path("app_type/{{cookiecutter.app_type}}/main.py"),
        destination=Path("{{cookiecutter.package_name}}/main.py"),
    )
    make_tasks_json(
        dev_run_command=DEV_RUN_COMMAND, docker_run_command=DOCKER_RUN_COMMAND
    )
    inject(file=Path(".devcontainer/post_create.sh"), content=POST_CREATE_INJECTION)
    inject(file=Path("Dockerfile"), content=DOCKER_INJECTION)


if __name__ == "__main__":
    main()
