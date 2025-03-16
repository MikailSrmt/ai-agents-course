#!/bin/bash

# Initialization script for AI Agents Course

echo "=== AI Agents Course Initialization ==="
echo "This script will set up your environment and run a simple example."

# Run setup script
echo -e "\n=== Setting up environment ==="
./setup.sh

# Run example
echo -e "\n=== Running example ==="
./run_example.sh

# Convert notebooks
echo -e "\n=== Converting notebooks ==="
python convert_to_notebooks.py

echo -e "\n=== Initialization complete! ==="
echo "You can now start exploring the notebooks in the notebooks/ directory."
echo "To activate the environment manually, run: source venv/bin/activate" 