#!/bin/sh

#Creates a new virtual environment in the current project folder.
python3 -m venv .venv 

#Activates the virtual environment
source .venv/bin/activate

#To install packages into the virtual environment, run
python3 -m pip install <package-name>

#check if the enviromment is setup correctly
pip list

#once installed all the libraries needed - generate a requirements.txt for dependencies.
pip freeze > requirements.txt

#To install dependencies, run:
pip install -r requirements.txt

#to deactivate the virtual environment, run:
deactivate
