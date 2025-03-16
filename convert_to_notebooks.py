#!/usr/bin/env python
"""
Convert Python scripts with cell markers to Jupyter notebooks.

This script converts Python files with cell markers (# %%) to Jupyter notebooks.
It searches for Python files in the notebooks directory and converts them to .ipynb files.
"""

import os
import sys
import subprocess
import glob

def convert_scripts_to_notebooks():
    """Convert Python scripts with cell markers to Jupyter notebooks."""
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    notebooks_dir = os.path.join(script_dir, "notebooks")
    
    # Find all Python files in the notebooks directory
    python_files = glob.glob(os.path.join(notebooks_dir, "*.py"))
    
    if not python_files:
        print("No Python files found in the notebooks directory.")
        return
    
    print(f"Found {len(python_files)} Python files to convert.")
    
    # Convert each Python file to a notebook
    for py_file in python_files:
        nb_file = py_file.replace(".py", ".ipynb")
        
        # Skip if the notebook already exists and is newer than the Python file
        if os.path.exists(nb_file) and os.path.getmtime(nb_file) > os.path.getmtime(py_file):
            print(f"Skipping {os.path.basename(py_file)} (notebook is up to date)")
            continue
        
        print(f"Converting {os.path.basename(py_file)} to notebook...")
        try:
            subprocess.run(
                ["jupyter", "nbconvert", "--to", "notebook", "--execute", py_file],
                check=True
            )
            print(f"Successfully converted {os.path.basename(py_file)}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {os.path.basename(py_file)}: {e}")
        except FileNotFoundError:
            print("Error: jupyter command not found. Please make sure Jupyter is installed.")
            print("You can install it with: pip install jupyter")
            return

if __name__ == "__main__":
    convert_scripts_to_notebooks() 