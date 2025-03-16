"""
Utility functions for loading environment variables.
"""

import os
import sys
from pathlib import Path
from typing import Dict, Optional

def load_env_file(env_path: str) -> Dict[str, str]:
    """
    Load environment variables from a .env file.
    
    Args:
        env_path (str): Path to the .env file
        
    Returns:
        Dict[str, str]: Dictionary of environment variables
    """
    env_vars = {}
    
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Parse key-value pairs
                if '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Warning: Environment file {env_path} not found.")
    
    return env_vars

def load_env(env_file: Optional[str] = None) -> Dict[str, str]:
    """
    Load environment variables from a .env file and set them in os.environ.
    
    Args:
        env_file (Optional[str]): Path to the .env file. If None, will look for .env in the project root.
        
    Returns:
        Dict[str, str]: Dictionary of loaded environment variables
    """
    # If no env_file is specified, look for .env in the project root
    if env_file is None:
        # Get the project root directory (assuming this file is in src/)
        project_root = Path(__file__).parent.parent
        env_file = project_root / '.env'
    
    # Load environment variables from the file
    env_vars = load_env_file(str(env_file))
    
    # Set environment variables
    for key, value in env_vars.items():
        os.environ[key] = value
    
    return env_vars

def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get an environment variable.
    
    Args:
        key (str): The environment variable key
        default (Optional[str]): Default value if the key is not found
        
    Returns:
        Optional[str]: The value of the environment variable or the default
    """
    return os.environ.get(key, default)

def require_env(key: str) -> str:
    """
    Get a required environment variable. Raises an error if not found.
    
    Args:
        key (str): The environment variable key
        
    Returns:
        str: The value of the environment variable
        
    Raises:
        ValueError: If the environment variable is not set
    """
    value = os.environ.get(key)
    if value is None:
        raise ValueError(f"Required environment variable '{key}' is not set. "
                         f"Please set it in your .env file or environment.")
    return value

# Load environment variables when this module is imported
if __name__ != "__main__":
    load_env() 