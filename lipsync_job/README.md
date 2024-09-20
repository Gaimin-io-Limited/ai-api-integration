# GAIMIN LipSync Job Submission Tool

This Python script automates the process of submitting and monitoring LipSync jobs using the Gaimin API. It allows you to create LipSync jobs with face images or videos and audio files, check the job status, and download the results.

## Features

- Submit LipSync jobs with face images or videos and audio files
- Automatically determine face format and static/dynamic status based on input file
- Monitor job progress
- Download completed job results

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository or download the `__main__.py` script.

2. Install the required Python library:

   ```
   pip install -r requirements.txt
   ```

   or

   ```
   pip install requests
   ```

3. Set up your API credentials as environment variables:

   For Unix-like systems (Linux, macOS):
   ```
   export LIPSYNC_API_KEY="your_api_key_here"
   ```

   For Windows:
   ```
   set LIPSYNC_API_KEY=your_api_key_here
   ```

## Usage

Run the script from the command line, providing the paths to your face file (image or video) and audio file:

```
python __main__.py path/to/your/face/file.jpg path/to/your/audio/file.wav
```

or

```
python __main__.py path/to/your/face/file.mp4 path/to/your/audio/file.wav
```

The script will:
1. Submit the LipSync job
2. Monitor the job progress
3. Download the result when the job is completed

## Supported File Formats

- Face Input:
  - Images: .jpg, .jpeg, .png
  - Videos: .mp4, .avi, .mov
- Audio Input: .wav (other formats may work but are not explicitly supported)

## Error Handling

The script includes error handling for:
- Missing environment variables
- Non-existent input files
- Unsupported file formats
- API request errors

If an error occurs, the script will display an informative message and exit.

## Notes

- The script uses Basic Authentication for API requests. Ensure your credentials are kept secure.
- The download URL for the result is temporary. Download the result promptly after job completion.
- For production use, consider implementing additional error handling and logging.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Gaimin-io-Limited/ai-api-integration/issues) if you want to contribute.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

