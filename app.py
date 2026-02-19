"""
Gemini Historical Artifact Description App
Milestone 1: Requirements Specification Demo
"""

import os
import requests
from transformers import pipeline

def describe_artifact():
    """
    Generates a historical-style description of the Gemini artifact.
    """
    # Use Hugging Face model for text generation
    generator = pipeline("text-generation", model="gpt2")

    prompt = (
        "Create a scholarly description of the Gemini twin-faced bronze statuette, "
        "1st–2nd Century AD, symbolizing duality and unity from Roman mythology."
    )

    result = generator(prompt, max_length=120, num_return_sequences=1)
    description = result[0]['generated_text']

    print("🗿 Gemini Artifact Description:\n")
    print(description)

if __name__ == "__main__":
    print("🔹 Starting Gemini Historical Artifact Description App...\n")
    describe_artifact()
