"""
Utility functions for the AI Agents course.
"""

import os
import torch
from transformers import AutoTokenizer, AutoModel
from pathlib import Path
import sys

# Add the parent directory to the path to import the env_utils module
sys.path.append(str(Path(__file__).parent.parent))
from src.env_utils import get_env

def check_environment():
    """
    Check if the environment is properly set up.
    
    Returns:
        dict: Information about the environment
    """
    import sys
    import platform
    import torch
    import transformers
    
    env_info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "transformers_version": transformers.__version__,
    }
    
    if torch.cuda.is_available():
        env_info["cuda_version"] = torch.version.cuda
        env_info["gpu_name"] = torch.cuda.get_device_name(0)
    
    # Check for API tokens
    env_info["huggingface_token"] = "Available" if get_env("HUGGINGFACE_TOKEN") else "Not set"
    env_info["openai_api_key"] = "Available" if get_env("OPENAI_API_KEY") else "Not set"
    
    return env_info

def load_hf_model(model_name, device=None):
    """
    Load a model from Hugging Face.
    
    Args:
        model_name (str): Name of the model on Hugging Face Hub
        device (str, optional): Device to load the model on. Defaults to None.
    
    Returns:
        tuple: (tokenizer, model)
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    print(f"Loading {model_name} on {device}...")
    
    # Get HuggingFace token from environment variables
    hf_token = get_env("HUGGINGFACE_TOKEN")
    
    # Use token if available
    if hf_token:
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
        model = AutoModel.from_pretrained(model_name, token=hf_token).to(device)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name).to(device)
    
    return tokenizer, model

def create_agent_environment(env_name):
    """
    Create a simple agent environment using Gymnasium.
    
    Args:
        env_name (str): Name of the Gymnasium environment
    
    Returns:
        gym.Env: The created environment
    """
    import gymnasium as gym
    
    env = gym.make(env_name)
    print(f"Created environment: {env_name}")
    print(f"Action space: {env.action_space}")
    print(f"Observation space: {env.observation_space}")
    
    return env 