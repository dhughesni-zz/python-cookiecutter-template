"""
Script used to make and update basic helm chart
"""
import os
from pyaml import yaml
project_name = '{{cookiecutter.project_name}}'
helmChartPath = os.getcwd() + "/chart/" + project_name
os.system("helm create " + helmChartPath)
print("Successfully added Helm Chart to cookiecutter: " + project_name)
