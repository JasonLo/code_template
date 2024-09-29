# Application Dockerfile
FROM python:{{cookiecutter.python_version}}-slim

WORKDIR /app
EXPOSE {{cookiecutter.app_port}}

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
ENV PATH="/root/.local/bin:${PATH}"

# Copy the application
COPY . .

# Inject app_type specific commands
POST_GEN_INJECTION
