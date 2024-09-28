# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Quick Start

Dev mode: `fastapi dev {{ cookiecutter.package_name }}/main.py`, or click `dev-run` on status bar.

Docker mode: `docker build -t {{ cookiecutter.package_name }} . && docker run --rm -p {{cookiecutter.app_port}}:{{cookiecutter.app_port}} {{ cookiecutter.package_name }}`, or click `docker-run` on status bar.
