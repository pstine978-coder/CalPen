#!/usr/bin/env python3
"""Test script to verify OpenAI API key is working"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key and base URL from environment
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("MODEL_NAME", "gpt-4o")

print("=" * 60)
print("Testing OpenAI API Configuration")
print("=" * 60)
print(f"API Key: {api_key[:20]}...{api_key[-10:]}")
print(f"Base URL: {base_url}")
print(f"Model: {model_name}")
print("=" * 60)

try:
    # Initialize OpenAI client
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    print("\n[*] Sending test request to OpenAI API...")
    
    # Make a simple test request
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'API test successful!' if you receive this message."}
        ],
        max_tokens=50
    )
    
    # Print the response
    result = response.choices[0].message.content
    print(f"\n[✓] SUCCESS! API Response:")
    print(f"    {result}")
    print("\n[✓] API key is working correctly!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n[✗] ERROR: API test failed!")
    print(f"    Error message: {str(e)}")
    print("\n[!] Please check your API key and try again.")
    print("=" * 60)
    exit(1)
