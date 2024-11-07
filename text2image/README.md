# Gaimin.ai Text2Image CLI Tool

This tool is a command-line interface (CLI) for interacting with Gaimin.ai's Text-to-Image API. The script sends a prompt and generation options to the API, which returns a generated image based on the input parameters.

## Features

- **Prompt-based Image Generation**: Send custom text prompts to the API.
- **Customizable Generation Options**: Control image dimensions, guidance scale, inference steps, and more via command-line arguments.
- **Version Display**: The tool displays its current version, defined in `version.py`.

## Requirements

- Python 3.6 or higher
- `requests` library for making HTTP requests.

You can install the necessary libraries using:

```bash
pip install requests
```
Project Structure

```
text2image/
├── generate_image.py   # Main script for the Text2Image CLI tool
├── version.py          # Contains version information for the tool
└── README.md           # This documentation file
```

## Setup

1.	Clone the repository or download the files.
2.	Install the dependencies with:
```
pip install requests
```

3.	Ensure version.py contains the correct version information for your tool by defining __version__ in version.py.

Usage

Run the script with the following syntax:

```
python generate_image.py <api_key> <prompt> [--options <options_json>]
```

## Arguments

	<api_key>: Your API key for Gaimin.ai’s API.
	<prompt>: A descriptive text prompt for image generation, e.g., "A cat holding a sign that says hello world".

## Optional Arguments

	•	--options: A JSON string specifying additional generation parameters. If not provided, default values are used.


## Example

```
python generate_image.py your_api_key_here "A cat holding a sign that says hello world" --options '{"guidance_scale": "0.", "height": 512, "width": 512, "num_inference_steps": 10, "max_sequence_length": 128}'
```

## Default options Values

If --options is not specified, the following defaults are used:

```
{
    "guidance_scale": "0.",
    "height": 768,
    "width": 1360,
    "num_inference_steps": 8,
    "max_sequence_length": 256
}
```
