import os
import re
import requests

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory to save downloaded videos (same as script location)
output_dir = current_dir
print(f"Videos will be saved in: {output_dir}")

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

# File path to the Posts.txt (assumes Posts.txt is in the same folder as the script)
file_path = os.path.join(current_dir, 'Posts.txt')

# Read and parse the Posts.txt file
with open(file_path, 'r') as f:
    content = f.read()

# Extract video links using regex
video_links = re.findall(r'(https://video-useast5-download.tiktokv.us[^\s]+)', content)

# Download each video
for idx, link in enumerate(video_links, start=1):
    output_file = os.path.join(output_dir, f'video_{idx}.mp4')
    download_video(link, output_file)