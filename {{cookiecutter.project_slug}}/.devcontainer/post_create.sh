#!/bin/bash

set -e

config_git() {
    echo "Configuring Git..."
    git config --global --add safe.directory /workspace/{{cookiecutter.package_name}}
    git config --global user.name "{{cookiecutter.author_name}}"
    git config --global user.email "{{cookiecutter.author_email}}"
    git config --global pull.rebase true
    git config --global core.filemode false
    git config --global core.eol lf
    git config --global credential.helper store
    echo "Git configured."
}

maybe_init_git() {
    git config --global --add safe.directory $(pwd)
    if [ ! -d .git ]; then
        echo "Initializing a new Git repository..."
        git init -b main
        git add .
        git commit -m "Initial commit"
        echo "Git repository initialized."
    else
        echo "Git repository already initialized."
    fi
}

maybe_init_uv() {
    # Create the virtual environment if it doesn't exist
    if [ ! -d .venv ]; then
        echo "Creating the virtual environment..."
        uv venv
        echo "Virtual environment created."
    else
        echo "Virtual environment already exists."
    fi
    
    # Initialize the uv project if it doesn't exist
    if [ ! -f pyproject.toml ]; then
        echo "Initializing a uv project..."
        uv init
        echo "uv project initialized."
    else
        echo "uv project already initialized."
    fi
}

install_fastapi() {
    echo "Installing fastapi as uv tool..."
    uv add fastapi[standard]
    uv tool install fastapi[standard]
}

install_streamlit() {
    echo "Installing streamlit as uv tool..."
    uv add streamlit
    uv tool install streamlit
}   

# Configure development tools
config_git
maybe_init_git
maybe_init_uv

# Install the uv tool for the app type, you may want to lock the version
APP_TYPE="{{ cookiecutter.app_type }}"
if [ "$APP_TYPE" == "fastapi" ]; then
    install_fastapi
elif [ "$APP_TYPE" == "streamlit" ]; then
    install_streamlit
else
    echo "Unknown app type: $APP_TYPE"
    exit 1
fi

echo "Post-create script complete."
