import json
from pathlib import Path

APP_PYPI = "fastapi[standard]"

# Inject into devcontainer post_create.sh
POST_CREATE_INJECTION = f"""
uv add {APP_PYPI}
uv tool install {APP_PYPI}
"""

# Inject into Dockerfile
DOCKER_INJECTION = """
RUN uv tool install {APP_PYPI}
CMD ["fastapi", "run", "{{cookiecutter.package_name}}/main.py", "--port", "{{cookiecutter.app_port}}"]
""".format(APP_PYPI=APP_PYPI)

# For VSCode tasks.json
DEV_RUN_COMMAND = "fastapi dev {{ cookiecutter.package_name }}/main.py"
DOCKER_RUN_COMMAND = (
    "docker build -t {{ cookiecutter.package_name }} . && "
    "docker run --rm -p {{cookiecutter.app_port}}:{{cookiecutter.app_port}} "
    "{{ cookiecutter.package_name }}"
)


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

    Path(".vscode").mkdir(exist_ok=True)
    with open(Path(".vscode/tasks.json"), "w") as f:
        f.write(json.dumps(tasks, indent=4))


def inject(
    file_path: Path, content: str, placeholder: str = "POST_GEN_INJECTION"
) -> None:
    """Inject content into a file at the placeholder."""

    text = file_path.read_text()
    text = text.replace(placeholder, content)
    file_path.write_text(text)


def copy(source: Path, destination: Path) -> None:
    """Copy a file from source to destination."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(source.read_text())


def main() -> None:
    copy(
        source=Path("app_type/{{cookiecutter.app_type}}/main.py"),
        destination=Path("{{cookiecutter.package_name}}/main.py"),
    )
    make_tasks_json(
        dev_run_command=DEV_RUN_COMMAND, docker_run_command=DOCKER_RUN_COMMAND
    )
    inject(
        file_path=Path(".devcontainer/post_create.sh"), content=POST_CREATE_INJECTION
    )
    inject(file_path=Path("Dockerfile"), content=DOCKER_INJECTION)


if __name__ == "__main__":
    main()
