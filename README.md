# Cookiecutter Code Template

A personal cookiecutter template designed to streamline project setup and development.

## Key Features

- **Devcontainer**: Instantly set up a fully configured Python development environment using [devcontainer]({{cookiecutter.project_slug}}/.devcontainer/devcontainer.json).
- **uv Dependency Management**: Simplify and accelerate your Python dependency management with [uv](https://docs.astral.sh/uv/), ensuring efficient workflows.
- **Docker Support**: Seamlessly run and deploy your app with [Docker]({{cookiecutter.project_slug}}/Dockerfile), enabling portability across various environments.
- **VSCode Tasks**: Leverage pre-configured [VSCode tasks]({{cookiecutter.project_slug}}/.vscode/tasks.json) to automate common development tasks and improve productivity.

## Getting Started

1. **Install Cookiecutter**: `python -m pip install --user cookiecutter`
2. **Generate a Project**: `cookiecutter gh:jasonlo/code-template`
3. **Open project in vscode**: `code <project_name>`, click "Reopen in Container".
4. **Run**: Click `dev-run` or `docker-run` on status bar.

## License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.
