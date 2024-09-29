#!/bin/bash

if command -v python3 &>/dev/null; then
    python3 app_type/{{cookiecutter.app_type}}/post_gen_project.py
elif command -v python &>/dev/null; then
    python app_type/{{cookiecutter.app_type}}/post_gen_project.py
else
    echo "Neither python3 nor python is installed."
    exit 1
fi

# clean up
rm -rf app_type
