# YouTube Video & Playlist Downloader

A Python script to download YouTube videos & playlists in **full quality (1080p/4K)** with **automatic merging** using `yt-dlp` and `FFmpeg`.

## 📥 Installation
```bash
git clone https://github.com/ilisjak/ytmp4
cd ytmp4
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Install FFmpeg (Required)
- **Linux:** `sudo apt install ffmpeg`
- **Mac:** `brew install ffmpeg`
- **Windows:** [Download & add to PATH](https://ffmpeg.org/download.html)

## 🚀 Usage
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID"
```
- **Download Audio Only:** `python script.py "URL" -a`
- **Download a Playlist:** `python script.py "PLAYLIST_URL"`
- **Change Output Folder:** `python script.py "URL" -o "folder_name"`

## 🛠 Troubleshooting
- **Videos stuck at 360p/720p?** Uses separate video/audio streams—FFmpeg merges them.
- **FFmpeg not found?** Ensure it’s installed and in `PATH`.
- **Permission Issues?** Try `sudo python script.py "URL"`.

## 📜 License
Open-source & free to modify.

