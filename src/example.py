"""
Example script demonstrating the use of utility functions.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path to import the utils module
sys.path.append(str(Path(__file__).parent.parent))
from src.utils import check_environment, load_hf_model, create_agent_environment
from src.env_utils import get_env, require_env

def main():
    """
    Main function to demonstrate the utility functions.
    """
    # Check the environment
    print("Checking environment...")
    env_info = check_environment()
    for key, value in env_info.items():
        print(f"{key}: {value}")
    
    print("\n" + "="*50 + "\n")
    
    # Create a simple agent environment
    try:
        env_name = get_env("GYM_ENV", "CartPole-v1")
        print(f"Using environment from config: {env_name}")
        env = create_agent_environment(env_name)
        
        # Run a few random steps
        observation, info = env.reset(seed=42)
        for i in range(5):
            action = env.action_space.sample()  # Random action
            observation, reward, terminated, truncated, info = env.step(action)
            print(f"Step {i+1}: Action={action}, Reward={reward}")
        
        env.close()
    except ImportError:
        print("Gymnasium not installed. Skipping environment creation.")
    
    print("\n" + "="*50 + "\n")
    
    # Load a small model from Hugging Face (if needed)
    try:
        # Get model name from environment variables or use default
        model_name = get_env("EMBEDDING_MODEL", "prajjwal1/bert-tiny")
        print(f"Loading model from config: {model_name}")
        
        # Check if HuggingFace token is available
        hf_token = get_env("HUGGINGFACE_TOKEN")
        if hf_token:
            print("Using HuggingFace token from environment variables")
        else:
            print("No HuggingFace token found in environment variables")
        
        # Load the model
        tokenizer, model = load_hf_model(model_name)
        
        # Test the model with a simple input
        inputs = tokenizer("Hello, I'm learning about AI agents!", return_tensors="pt")
        outputs = model(**inputs)
        
        print(f"Model output shape: {outputs.last_hidden_state.shape}")
    except Exception as e:
        print(f"Error loading model: {e}")

if __name__ == "__main__":
    main() 