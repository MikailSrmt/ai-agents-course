"""
Script to fix Python path issues in Cursor.

This script adds the virtual environment's site-packages to sys.path,
which should help Cursor find installed packages.
"""

import sys
import os
from pathlib import Path

def fix_python_path():
    """
    Add the virtual environment's site-packages to sys.path.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get the project root directory
        project_root = Path(__file__).parent.parent
        
        # Path to the virtual environment
        venv_path = project_root / "venv"
        
        # Path to site-packages
        site_packages = venv_path / "lib" / "python3.13" / "site-packages"
        
        # Add to sys.path if it exists
        if site_packages.exists():
            sys.path.insert(0, str(site_packages))
            return True
        else:
            print(f"Warning: Site packages directory not found: {site_packages}")
            return False
    except Exception as e:
        print(f"Error fixing Python path: {e}")
        return False

# Fix the Python path
fix_successful = fix_python_path()

# Test importing huggingface_hub
try:
    import huggingface_hub
    print(f"Successfully imported huggingface_hub {huggingface_hub.__version__}")
except ImportError as e:
    print(f"Error importing huggingface_hub: {e}")
    
    # Print sys.path for debugging
    print("\nCurrent sys.path:")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")
    
    # Suggest solutions
    print("\nPossible solutions:")
    print("1. Make sure huggingface_hub is installed: pip install huggingface_hub")
    print("2. Configure Cursor to use your virtual environment's Python interpreter:")
    print("   - In Cursor, go to Settings/Preferences")
    print("   - Look for Python or Interpreter settings")
    print(f"   - Set the Python interpreter path to: {sys.executable}")
    print("3. Add the following code at the beginning of your script:")
    print("```python")
    print("import sys")
    print("import os")
    print("from pathlib import Path")
    print("project_root = Path(__file__).parent.parent")
    print("site_packages = project_root / 'venv' / 'lib' / 'python3.13' / 'site-packages'")
    print("sys.path.insert(0, str(site_packages))")
    print("```") 