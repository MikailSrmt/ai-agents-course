"""
Simplified example script demonstrating the use of environment variables.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path to import the modules
sys.path.append(str(Path(__file__).parent.parent))
from src.env_utils import get_env, require_env, load_env

def check_simple_environment():
    """
    Check basic environment information without requiring PyTorch.
    
    Returns:
        dict: Information about the environment
    """
    import sys
    import platform
    
    env_info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "os_name": os.name,
    }
    
    # Check for API tokens
    env_info["huggingface_token"] = "Available" if get_env("HUGGINGFACE_TOKEN") else "Not set"
    env_info["openai_api_key"] = "Available" if get_env("OPENAI_API_KEY") else "Not set"
    
    return env_info

def main():
    """
    Main function to demonstrate the use of environment variables.
    """
    # Load environment variables
    load_env()
    
    print("=== Simple Environment Check ===")
    env_info = check_simple_environment()
    for key, value in env_info.items():
        print(f"{key}: {value}")
    
    print("\n=== Environment Variables ===")
    
    # Get environment variables with default values
    model_name = get_env("MODEL_NAME", "default-model")
    embedding_model = get_env("EMBEDDING_MODEL", "default-embedding-model")
    gym_env = get_env("GYM_ENV", "CartPole-v1")
    debug_mode = get_env("DEBUG_MODE", "false")
    
    print(f"Model: {model_name}")
    print(f"Embedding Model: {embedding_model}")
    print(f"Gym Environment: {gym_env}")
    print(f"Debug Mode: {debug_mode}")
    
    # Get API configuration
    api_timeout = get_env("API_TIMEOUT", "10")
    api_retries = get_env("API_RETRIES", "1")
    
    print(f"\n=== API Configuration ===")
    print(f"API Timeout: {api_timeout} seconds")
    print(f"API Retries: {api_retries}")
    
    # Get data and model directories
    data_dir = get_env("DATA_DIR", "./data")
    models_dir = get_env("MODELS_DIR", "./models")
    
    print(f"\nData Directory: {data_dir}")
    print(f"Models Directory: {models_dir}")
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)
    
    print(f"\nCreated directories:")
    print(f"- {data_dir}")
    print(f"- {models_dir}")
    
    # Print all custom environment variables
    print("\n=== All Custom Environment Variables ===")
    prefixes = ["MODEL_", "EMBEDDING_", "DATA_", "MODELS_", "GYM_", "DEBUG_", "API_"]
    for key, value in os.environ.items():
        if any(key.startswith(prefix) for prefix in prefixes):
            print(f"{key}: {value}")

if __name__ == "__main__":
    main() 