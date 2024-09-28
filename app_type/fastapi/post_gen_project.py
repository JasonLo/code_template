from pathlib import Path

# Devcontainer post_create.sh
post_create_file = Path("{{cookiecutter.project_slug}}/.devcontainer/post_create.sh")
post_create_injection = """
echo "Installing fastapi as uv tool..."
uv add fastapi[standard]
uv tool install fastapi[standard]
"""

# Dockerfile (for Docker-run)
docker_file = Path("{{cookiecutter.project_slug}}/Dockerfile")
docker_injection = """
RUN uv tool install fastapi[standard]
CMD ["fastapi", "run", "{{cookiecutter.package_name}}/main.py", "--port", "{{cookiecutter.app_port}}"]
"""

main_file_source = Path("app_type/fastapi/main.py")
main_file_destination = Path(
    "{{cookiecutter.project_slug}}/{{cookiecutter.package_name}}/main.py"
)

tasks_file_source = Path("app_type/fastapi/tasks.json")
tasks_file_destination = Path("{{cookiecutter.project_slug}}/.vscode/tasks.json")


def inject(
    file: Path, content: str, placeholder: str = "{{ POST_GEN_INJECTION }}"
) -> None:
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
    copy(source=main_file_source, destination=main_file_destination)
    copy(source=tasks_file_source, destination=tasks_file_destination)
    inject(file=post_create_file, content=post_create_injection)
    inject(file=docker_file, content=docker_injection)


if __name__ == "__main__":
    main()
