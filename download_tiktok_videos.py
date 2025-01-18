import os
import re
import requests

# File path to the Post.txt
file_path = 'Post.txt'

# Directory to save downloaded videos
output_dir = '/mnt/mediadrive/backups/tiktoks'
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

def download_video(video_url, output_path):
    try:
        print(f"Downloading: {video_url}")
        response = requests.get(video_url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded to: {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {video_url}: {e}")

# Read and parse the file
with open(file_path, 'r') as f:
    content = f.read()

# Extract full video links using regex
video_links = re.findall(r'(https://video-useast5-download.tiktokv.us[^\s]+)', content)

# Download each video
for idx, link in enumerate(video_links, start=1):
    output_file = os.path.join(output_dir, f'video_{idx}.mp4')
    download_video(link, output_file)
