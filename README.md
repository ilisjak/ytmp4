# YouTube Video & Playlist Downloader

This Python script allows you to download **YouTube videos and playlists** in the **highest quality (1080p+ or 4K)**. It automatically downloads separate **video and audio streams** and merges them using **FFmpeg**.

## 📌 Features
- ✅ **Full 1080p+ video quality** (bypasses YouTube's progressive stream limit of 720p)
- ✅ **Downloads both video & audio separately** and merges them automatically
- ✅ **Supports YouTube playlists** (downloads all videos in a playlist)
- ✅ **Can download audio-only files** (useful for music or podcasts)
- ✅ **Cross-platform support** (Works on Windows, Linux, and macOS)

---

## 📥 Installation

### 1️⃣ Install Python & Dependencies
Ensure you have **Python 3+** installed.

Install the required Python package:
```bash
pip install pytubefix
```

### 2️⃣ Install FFmpeg (Required for Merging Video & Audio)
FFmpeg is needed to merge separate video and audio streams.

#### 🔹 **Linux (Ubuntu/Debian)**
```bash
sudo apt install ffmpeg
```

#### 🔹 **Windows**
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Add FFmpeg to the system **PATH**.

#### 🔹 **Mac (Homebrew)**
```bash
brew install ffmpeg
```

---

## 🚀 How to Use

### 🎥 **Download a Single Video (Full Quality)**
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 🎵 **Download Audio Only (MP3-like format)**
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID" -a
```

### 📂 **Download an Entire Playlist**
```bash
python script.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

### 🏷 **Change Download Directory**
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID" -o "custom_folder"
```

---

## 🛠️ Troubleshooting

### ❌ **Videos Stuck at 360p or 720p?**
YouTube delivers **high-quality (1080p, 4K) videos in separate streams**, so the script downloads **video and audio separately** and merges them using **FFmpeg**.

### ❌ **FFmpeg Not Found?**
Make sure **FFmpeg** is installed and added to your system's `PATH`.

### ❌ **Permission Issues?**
Try running the script with **admin/root** privileges:
```bash
sudo python script.py "URL"
```

---

## 📜 License
This script is **open-source** and can be modified or redistributed freely.

Happy downloading! 🚀

