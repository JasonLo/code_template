#!/bin/bash

# run app_type specific post_gen_project.py
python app_type/{{cookiecutter.app_type}}/post_gen_project.py

# clean up
rm -rf app_type
