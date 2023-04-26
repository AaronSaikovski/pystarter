#!/bin/sh

#PIP Install
#setup the virtual environment
python3 -m venv .venv 

#activate the virtual environment
source .venv/bin/activate

#install packages
pip install -r requirements.txt

#upgrade PIP
pip install --upgrade pip


#Miniconda setup

#To create an environment - Replace myenv with the environment name
#specifying python will install python latest version 
conda create --name <myenv> python

#Activate a given environment
conda activate <envname> 

#Export your active environment to a new file - make sure the environment is activated first!!
conda env export > environment.yml

#to install a package via Conda
conda install <PACKAGE_NAME>