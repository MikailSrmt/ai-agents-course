"""
# Introduction to AI Agents

This script introduces the concept of AI agents and demonstrates basic examples.
You can run this as a Python script or convert it to a Jupyter notebook.

To convert to a notebook, run:
```
jupyter nbconvert --to notebook --execute 01_introduction_to_agents.py
```
"""

# %% [markdown]
# # Introduction to AI Agents
# 
# AI agents are systems that can perceive their environment, make decisions, and take actions to achieve specific goals.
# In this notebook, we'll explore the basic concepts of AI agents and implement simple examples.

# %% [markdown]
# ## Setup
# 
# First, let's import the necessary libraries and check our environment.

# %%
import sys
import os

# Add the parent directory to the path to import the utils module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import check_environment

# Check the environment
env_info = check_environment()
for key, value in env_info.items():
    print(f"{key}: {value}")

# %% [markdown]
# ## What is an AI Agent?
# 
# An AI agent is a system that:
# 
# 1. **Perceives** its environment through sensors
# 2. **Processes** information and makes decisions
# 3. **Acts** upon the environment through actuators
# 4. **Learns** from experience (in many cases)
# 
# Agents can be classified based on their capabilities:
# 
# - **Simple reflex agents**: Act based on current percepts
# - **Model-based agents**: Maintain an internal state
# - **Goal-based agents**: Work towards specific goals
# - **Utility-based agents**: Maximize a utility function
# - **Learning agents**: Improve performance over time

# %% [markdown]
# ## Simple Reflex Agent Example
# 
# Let's implement a simple reflex agent that responds to its environment.

# %%
class SimpleReflexAgent:
    """A simple reflex agent that responds to its environment."""
    
    def __init__(self, name):
        self.name = name
        self.percepts = []
    
    def perceive(self, percept):
        """Receive a percept from the environment."""
        self.percepts.append(percept)
        print(f"{self.name} perceives: {percept}")
    
    def act(self):
        """Decide on an action based on the current percept."""
        if not self.percepts:
            return "Do nothing"
        
        current_percept = self.percepts[-1]
        
        # Simple reflex rules
        if current_percept == "too hot":
            return "Turn on the fan"
        elif current_percept == "too cold":
            return "Turn on the heater"
        elif current_percept == "dark":
            return "Turn on the light"
        else:
            return "Do nothing"

# Test the simple reflex agent
agent = SimpleReflexAgent("ThermoBot")
agent.perceive("too hot")
action = agent.act()
print(f"{agent.name} decides to: {action}")

agent.perceive("too cold")
action = agent.act()
print(f"{agent.name} decides to: {action}")

# %% [markdown]
# ## Model-Based Agent Example
# 
# A model-based agent maintains an internal state of the world.

# %%
class ModelBasedAgent:
    """A model-based agent that maintains an internal state."""
    
    def __init__(self, name):
        self.name = name
        self.internal_state = {
            "temperature": 22,  # in Celsius
            "light_level": "bright",
            "time_of_day": "day"
        }
    
    def update_state(self, percept):
        """Update the internal state based on a percept."""
        if "temperature" in percept:
            self.internal_state["temperature"] = percept["temperature"]
        
        if "light_level" in percept:
            self.internal_state["light_level"] = percept["light_level"]
        
        if "time_of_day" in percept:
            self.internal_state["time_of_day"] = percept["time_of_day"]
        
        print(f"{self.name} updated state: {self.internal_state}")
    
    def act(self):
        """Decide on an action based on the internal state."""
        actions = []
        
        # Temperature control
        if self.internal_state["temperature"] > 25:
            actions.append("Turn on the AC")
        elif self.internal_state["temperature"] < 18:
            actions.append("Turn on the heater")
        
        # Light control
        if (self.internal_state["light_level"] == "dark" and 
            self.internal_state["time_of_day"] == "day"):
            actions.append("Turn on the lights")
        elif (self.internal_state["light_level"] == "dark" and 
              self.internal_state["time_of_day"] == "night" and 
              self.internal_state["temperature"] > 0):  # Only if not freezing
            actions.append("Turn on dim lights")
        
        if not actions:
            return "Do nothing"
        return ", ".join(actions)

# Test the model-based agent
agent = ModelBasedAgent("HomeBot")
agent.update_state({"temperature": 28, "light_level": "bright"})
action = agent.act()
print(f"{agent.name} decides to: {action}")

agent.update_state({"temperature": 16, "light_level": "dark", "time_of_day": "night"})
action = agent.act()
print(f"{agent.name} decides to: {action}")

# %% [markdown]
# ## Using Reinforcement Learning for Agents
# 
# In more complex scenarios, we can use reinforcement learning to train agents.
# Let's see a simple example using the Gymnasium library.

# %%
try:
    import gymnasium as gym
    import numpy as np
    
    # Create a simple environment
    env = gym.make("CartPole-v1")
    observation, info = env.reset(seed=42)
    
    # Define a simple policy (not trained, just for demonstration)
    def simple_policy(observation):
        """A simple policy that tilts the cart in the direction of the pole's lean."""
        # If the pole is leaning to the right (positive angle), move right
        # If the pole is leaning to the left (negative angle), move left
        pole_angle = observation[2]
        return 1 if pole_angle > 0 else 0
    
    # Run a few steps with our simple policy
    total_reward = 0
    for i in range(100):
        action = simple_policy(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        
        if i < 5:  # Print only the first 5 steps to avoid clutter
            print(f"Step {i+1}: Action={action}, Reward={reward}, Observation={observation}")
        
        if terminated or truncated:
            break
    
    print(f"Episode finished after {i+1} steps with total reward {total_reward}")
    env.close()
    
except ImportError:
    print("Gymnasium not installed. Skipping reinforcement learning example.")

# %% [markdown]
# ## Next Steps
# 
# In the next notebooks, we'll explore:
# 
# 1. Using language models as agents
# 2. Multi-agent systems and communication
# 3. Advanced reinforcement learning for agent training
# 4. Building agents with memory and planning capabilities 