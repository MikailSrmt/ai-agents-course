# AI Agents Course - Hugging Face

This repository contains code and notebooks for the AI Agents course from Hugging Face.

## Setup

1. Clone this repository
2. Create a virtual environment:

```bash
# On macOS/Linux
python -m venv venv

# On Windows
python -m venv venv
```

3. Activate the virtual environment:

```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up environment variables:

```bash
# Copy the template file
cp .env.template .env

# Edit the .env file with your API keys and tokens
nano .env  # or use any text editor
```

## Project Structure

- `notebooks/`: Jupyter notebooks for the course
- `src/`: Source code for AI agents
- `.env.template`: Template for environment variables
- `.env`: Your personal environment variables (not committed to Git)

## Environment Variables

This project uses environment variables to manage API keys and configuration. The following variables are supported:

- `HUGGINGFACE_TOKEN`: Your Hugging Face API token
- `OPENAI_API_KEY`: Your OpenAI API key
- `MODEL_NAME`: The name of the model to use
- `EMBEDDING_MODEL`: The name of the embedding model to use
- `DATA_DIR`: Directory for data files
- `MODELS_DIR`: Directory for model files

You can add your own environment variables as needed.

## Getting Started

After setting up the environment, you can start by exploring the notebooks in the `notebooks/` directory.

You can also run the initialization script to set up everything automatically:

```bash
./init.sh  # On macOS/Linux
```

To test your environment variables setup, run:

```bash
python src/env_example.py
```

## Resources

- [Hugging Face Documentation](https://huggingface.co/docs)
- [Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) 