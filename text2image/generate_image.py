import argparse
import requests
import json
from typing import Dict, Any
from version import __version__


def generate_image(api_key: str, url: str, prompt: str, options: Dict[str, Any]):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
    }
    data = {
        "prompt": prompt,
        "options": options
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def main():
    parser = argparse.ArgumentParser(description="Execute Text2Image request")
    parser.add_argument("api_key", help="API Key for gaimin ai")
    parser.add_argument("prompt", help="Prompt for text generation")
    parser.add_argument("--options", type=str, help="JSON string for options")

    args = parser.parse_args()

    # API request setup
    api_key = args.api_key
    url = "https://api.cloud.gaimin.io/ai/text-2-image/generate"
    prompt = args.prompt

    # Load options from JSON string or use defaults
    if args.options:
        options = json.loads(args.options)
    else:
        options = {
            "guidance_scale": "0.",
            "height": 768,
            "width": 1360,
            "num_inference_steps": 8,
            "max_sequence_length": 256
        }

    # Version and response
    print(f"Gaimin.ai Text2Image Tool v{__version__}")
    response = generate_image(api_key, url, prompt, options)
    print(response)

if __name__ == "__main__":
    main()