"""
Helper module to fix Python path issues in Cursor.

Import this module at the beginning of your scripts to ensure that
packages installed in the virtual environment are available.

Example usage:
```python
import sys
import os
from pathlib import Path

# Add the current directory to the path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import the cursor_helper module to fix Python path issues
import cursor_helper

# Now you can import modules installed in the virtual environment
import huggingface_hub
```
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
            if str(site_packages) not in sys.path:
                sys.path.insert(0, str(site_packages))
                return True
            return True  # Already in sys.path
        else:
            print(f"Warning: Site packages directory not found: {site_packages}")
            return False
    except Exception as e:
        print(f"Error fixing Python path: {e}")
        return False

# Automatically fix the Python path when this module is imported
fix_successful = fix_python_path() 