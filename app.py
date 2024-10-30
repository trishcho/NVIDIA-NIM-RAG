import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Retrieve NVIDIA API key from environment variables
nvidia_api_key = os.getenv("NVIDIA_API_KEY")

# Check if the API key was loaded successfully
if not nvidia_api_key:
    raise ValueError("NVIDIA_API_KEY not found. Please ensure it's defined in the .env file.")

# Initialize the OpenAI client with NVIDIA API details
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=nvidia_api_key
)

# Create a completion request
completion = client.chat.completions.create(
    model="nvidia/llama-3.1-nemotron-70b-instruct",
    messages=[{"role": "user", "content": "Hi"}],
    temperature=0.5,
    top_p=1,
    max_tokens=1024,
    stream=True
)

# Stream and print response
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
