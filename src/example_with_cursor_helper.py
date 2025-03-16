"""
Example script that uses the cursor_helper module to fix Python path issues.
"""

import sys
import os
from pathlib import Path

# Add the current directory to the path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import the cursor_helper module to fix Python path issues
import cursor_helper

# Now we can import modules installed in the virtual environment
try:
    import huggingface_hub
    print(f"Successfully imported huggingface_hub {huggingface_hub.__version__}")
    
    # Import other modules from the virtual environment
    import numpy as np
    print(f"Successfully imported numpy {np.__version__}")
    
    import pandas as pd
    print(f"Successfully imported pandas {pd.__version__}")
    
    # Add the parent directory to the path to import our own modules
    project_root = current_dir.parent
    sys.path.append(str(project_root))
    
    # Import our own modules
    from src.env_utils import get_env, load_env
    
    # Load environment variables
    load_env()
    
    print("\n=== Environment Variables ===")
    model_name = get_env("MODEL_NAME", "default-model")
    embedding_model = get_env("EMBEDDING_MODEL", "default-embedding-model")
    
    print(f"Model: {model_name}")
    print(f"Embedding Model: {embedding_model}")
    
except ImportError as e:
    print(f"Error importing modules: {e}")
    
    # Print sys.path for debugging
    print("\nCurrent sys.path:")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")
    
    print("\nIf you're still having issues, try the following:")
    print("1. Make sure all required packages are installed: pip install huggingface_hub numpy pandas")
    print("2. Configure Cursor to use your virtual environment's Python interpreter")
    print("3. Restart Cursor after making changes") 