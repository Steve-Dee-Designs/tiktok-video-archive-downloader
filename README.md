# TikTok Video Archive Downloader
A simple Python script to download your TikTok videos using the data from your TikTok Data Archive. This script is tested on Debian and requires Python 3.

---

## Getting Started

### 1. Install the Script and Dependencies

1. Clone or download this repository to your computer:
   ```
   git clone https://github.com/Steve-Dee-Designs/tiktok-video-archive-downloader.git
   cd tiktok-video-archive-downloader
   ```
2. Install the required Python library:
   ```
   pip install requests
   ```

---

### 2. Request Your TikTok Data Archive

1. Visit TikTok's [Download Your Data](https://www.tiktok.com/setting/download-your-data) page.
2. Under the **Request Data** tab:
   - Select **TXT format**.
   - Click the **Request Data** button.

3. TikTok may take some time to prepare your export. Once it’s ready, you’ll receive a notification.
4. Return to the **Download Data** tab on the same page and click the **Download** button to download a ZIP file named something like `TikTok_Data_####.zip`.

---

### 3. Extract and Prepare Your Data

1. Extract the downloaded ZIP file.
2. Locate the file at `TikTok/Posts/Posts.txt` inside the extracted folder.
3. Replace the default `Posts.txt` file in this repository with your own `Posts.txt` file.

---

### 4. Run the Script

1. Open a terminal or command prompt in the folder containing the script.
2. Run the following command:
   ```
   python3 download_tiktok_videos.py
   ```
3. The videos will be saved to the default output folder (`tiktok_videos`) or a specified directory based on the script configuration.

---

### Notes

- Ensure Python 3 is installed on your system.
- If you encounter issues downloading videos (e.g., authentication errors), the TikTok links may have expired. Re-request your data archive to get updated links.
- This script is designed for personal use to download your own content. Do not use it to download videos without permission.
