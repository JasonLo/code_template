# Cookiecutter Code Template

A personal cookiecutter template designed to streamline project setup and development.

## Key Features

- **Devcontainer**: Instantly set up a fully configured Python development environment using [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).
- **uv Dependency Management**: Simplify and accelerate your Python dependency management with [uv](https://docs.astral.sh/uv/), ensuring efficient workflows.
- **Docker Support**: Seamlessly run and deploy your app with [Docker](https://docs.docker.com/), enabling portability across various environments.
- **VSCode Tasks**: Leverage pre-configured [VSCode tasks](https://code.visualstudio.com/docs/editor/tasks) to automate common development tasks and improve productivity.
- **Template Options**: Choose a different `app_type` when creating a project with cookiecutter. Currently supports `fastapi` and `streamlit`.

## Getting Started

1. **Install Cookiecutter**
    ```bash
    pip install --user cookiecutter
    ```
2. **Generate a Project**
    ```bash
    cookiecutter gh:jasonlo/code-template
    ```
3. **Open project in vscode**
    ```bash
    code <project_name>
    ```
    Then click "Reopen in Container".
4. **Run**

    Click `dev-run` or `docker-run` on status bar.

## License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.
