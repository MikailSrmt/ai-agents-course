"""
Example script demonstrating how to use environment variables.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path to import the modules
sys.path.append(str(Path(__file__).parent.parent))
from src.env_utils import get_env, require_env, load_env

def main():
    """
    Main function to demonstrate the use of environment variables.
    """
    # Load environment variables (this is already done when env_utils is imported,
    # but we're doing it explicitly here for demonstration)
    load_env()
    
    print("=== Environment Variables Example ===\n")
    
    # Get environment variables with default values
    model_name = get_env("MODEL_NAME", "default-model")
    embedding_model = get_env("EMBEDDING_MODEL", "default-embedding-model")
    
    print(f"Using model: {model_name}")
    print(f"Using embedding model: {embedding_model}")
    
    # Try to get API keys (these might not be set)
    huggingface_token = get_env("HUGGINGFACE_TOKEN")
    openai_api_key = get_env("OPENAI_API_KEY")
    
    print("\n=== API Keys Status ===")
    print(f"HuggingFace Token: {'Set' if huggingface_token else 'Not set'}")
    print(f"OpenAI API Key: {'Set' if openai_api_key else 'Not set'}")
    
    # Example of how to use require_env (commented out to avoid errors if not set)
    print("\n=== Using Required Environment Variables ===")
    try:
        # This will raise an error if the variable is not set
        # required_var = require_env("REQUIRED_VARIABLE")
        # print(f"Required variable: {required_var}")
        print("Example commented out to avoid errors.")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== All Environment Variables ===")
    # Print all environment variables that start with specific prefixes
    # (filtering to avoid printing sensitive information or system variables)
    prefixes = ["MODEL_", "EMBEDDING_", "DATA_", "MODELS_"]
    for key, value in os.environ.items():
        if any(key.startswith(prefix) for prefix in prefixes):
            print(f"{key}: {value}")

if __name__ == "__main__":
    main() 