#!/bin/bash

# Setup script for AI Agents Course

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create Jupyter kernel
echo "Creating Jupyter kernel..."
python -m ipykernel install --user --name=ai_agents_course --display-name="AI Agents Course"

echo "Setup complete! You can now run 'source venv/bin/activate' to activate the environment."
echo "To start Jupyter, run 'jupyter notebook' or 'jupyter lab'." 