"""
Test script to verify that the huggingface_hub package works.
"""

import sys
from pathlib import Path

# Add the parent directory to the path to import the modules
sys.path.append(str(Path(__file__).parent.parent))
from src.env_utils import get_env, load_env

def main():
    """
    Main function to test the huggingface_hub package.
    """
    # Load environment variables
    load_env()
    
    print("=== Testing Hugging Face Hub ===")
    
    try:
        import huggingface_hub
        print(f"huggingface_hub version: {huggingface_hub.__version__}")
        print("huggingface_hub imported successfully!")
        
        # Get the Hugging Face token from environment variables
        hf_token = get_env("HUGGINGFACE_TOKEN")
        if hf_token:
            print("Hugging Face token is set in environment variables.")
            
            # Create a Hugging Face API client
            from huggingface_hub import HfApi
            api = HfApi(token=hf_token)
            
            # Test a simple API call (this will work even with an invalid token)
            print("\nTesting API call to list models...")
            try:
                # Just get a few models to test the API
                models = api.list_models(limit=5)
                print(f"Successfully retrieved {len(models)} models!")
                print("First few models:")
                for i, model in enumerate(models):
                    if i < 3:  # Just show the first 3
                        print(f"- {model.id}")
            except Exception as e:
                print(f"Error making API call: {e}")
        else:
            print("Hugging Face token is not set in environment variables.")
            print("Set HUGGINGFACE_TOKEN in your .env file to test API calls.")
    
    except ImportError as e:
        print(f"Error importing huggingface_hub: {e}")
        print("\nPossible solutions:")
        print("1. Make sure huggingface_hub is installed: pip install huggingface_hub")
        print("2. Check if your virtual environment is activated")
        print("3. Verify that Cursor is using the correct Python interpreter")

if __name__ == "__main__":
    main() 