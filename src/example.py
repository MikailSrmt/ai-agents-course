"""
Example script demonstrating the use of utility functions.
"""

import sys
import os

# Add the parent directory to the path to import the utils module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import check_environment, load_hf_model, create_agent_environment

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
        env = create_agent_environment("CartPole-v1")
        
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
        print("Loading a small model from Hugging Face...")
        # Using a tiny model for demonstration
        tokenizer, model = load_hf_model("prajjwal1/bert-tiny")
        
        # Test the model with a simple input
        inputs = tokenizer("Hello, I'm learning about AI agents!", return_tensors="pt")
        outputs = model(**inputs)
        
        print(f"Model output shape: {outputs.last_hidden_state.shape}")
    except Exception as e:
        print(f"Error loading model: {e}")

if __name__ == "__main__":
    main() 