# Application Dockerfile
FROM python:{{cookiecutter.python_version}}-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Install dependencies first to cache them
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen
RUN uv tool install fastapi[standard]
ENV PATH="/root/.local/bin:${PATH}"

COPY . .

EXPOSE {{cookiecutter.app_port}}
CMD ["fastapi", "run", "new_project/main.py", "--host", "0.0.0.0", "--port", "8080"]
