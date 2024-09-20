import json
import requests
import time
import os
import argparse
import mimetypes
from version import __version__

# API endpoints
CREATE_JOB_URL = "https://api.gaimin.gg/api/lip-sync/jobs"
GET_JOB_INFO_URL = "https://api.gaimin.gg/api/lip-sync/jobs/{job_id}"

# File type configurations
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png'}
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov'}

def get_auth_header():
    api_key = os.environ.get('LIPSYNC_API_KEY')
    return {"Authorization": f"Basic {api_key}"}

def get_face_info(file_path):
    _, ext = os.path.splitext(file_path.lower())
    face_format = ext[1:]
    is_static = ext in IMAGE_EXTENSIONS
    
    if ext not in IMAGE_EXTENSIONS and ext not in VIDEO_EXTENSIONS:
        raise ValueError(f"Unsupported file format for face input: {ext}")
    
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        mime_type = 'application/octet-stream'
    
    return face_format, is_static, mime_type

def get_audio_info(file_path):
    _, ext = os.path.splitext(file_path.lower())
    audio_format = ext[1:]
    
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        mime_type = 'audio/wav'  # Default to wav if unable to determine
    
    return audio_format, mime_type

def create_lipsync_job(face_file_path, audio_file_path):
    try:
        headers = get_auth_header()

        face_format, is_static, face_mime_type = get_face_info(face_file_path)
        audio_format, audio_mime_type = get_audio_info(audio_file_path)
    
        json_data = {
            "face_format": face_format,
            "static": is_static
        }
        
        files = {
            "json": (None, json.dumps(json_data), 'application/json'),
            "face": (f'face.{face_format}', open(face_file_path, "rb"), face_mime_type),
            "audio": (f'audio.{audio_format}', open(audio_file_path, "rb"), audio_mime_type)
        }
            
        response = requests.post(CREATE_JOB_URL, headers=headers, files=files)
        response.raise_for_status()
        
        if response.json()['success']:
            return response.json()["data"]["uuid"]
        else:
            print(f"API Error: '{response.json()['error']['type']}' Description: '{response.json()['error']['description']}'.")
            exit(1)
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")

def get_job_status(job_id):
    headers = get_auth_header()
    
    response = requests.get(GET_JOB_INFO_URL.format(job_id=job_id), headers=headers)
    response.raise_for_status()
    return response.json()["data"]

def download_result(url, output_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)

def main(face_file_path, audio_file_path):
    try:
        print("Submitting LipSync job...")
        job_id = create_lipsync_job(face_file_path, audio_file_path)
        print(f"Job submitted. ID: {job_id}")
        
        while True:
            print(f"Checking job ('{job_id}') status...")
            job_info = get_job_status(job_id)
            status = job_info["status"]
            print(f"Current status: {status}")
            
            if status == "COMPLETED":
                result_url = job_info["result_url"]
                output_file = f"lipsync_result.mp4"
                print(f"Job completed. Downloading result to {output_file}...")
                download_result(result_url, output_file)
                print("Download complete.")
                break
            elif status == "FAILED":
                print("Job failed. Please check the error and try again.")
                break
            
            print("Waiting 10 seconds before next check...")
            time.sleep(10)
    except ValueError as e:
        print(f"Error: {str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")

def validate_env_vars():
    api_key = os.environ.get('LIPSYNC_API_KEY')
    
    if not api_key:
        print("Error: LIPSYNC_API_KEY environment variable is not set.")
        return False
    return True

if __name__ == "__main__":
    if not validate_env_vars():
        exit(1)
    parser = argparse.ArgumentParser(description="Submit a LipSync job with face (image or video) and audio files.")
    parser.add_argument("face_file", help="Path to the face image file")
    parser.add_argument("audio_file", help="Path to the audio file")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    if not os.path.exists(args.face_file):
        print(f"Error: Face file '{args.face_file}' does not exist.")
        exit(1)
    if not os.path.exists(args.audio_file):
        print(f"Error: Audio file '{args.audio_file}' does not exist.")
        exit(1)

    print(f"Gaimin.ai LipSync Job Submission Tool v{__version__}")
    main(args.face_file, args.audio_file)