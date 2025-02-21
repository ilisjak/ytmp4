import argparse
import os
import subprocess
from yt_dlp import YoutubeDL
from tqdm import tqdm

# Default download directory
DOWNLOAD_DIR = "downloads"

def merge_video_audio(video_path, audio_path, output_path):
    """Merges video and audio using FFmpeg with a progress bar and better error handling."""
    try:
        print(f"Merging video: {video_path} with audio: {audio_path} into {output_path}")

        cmd = [
            "ffmpeg", "-i", video_path, "-i", audio_path,
            "-c:v", "copy", "-c:a", "aac", "-strict", "experimental",
            "-y", output_path  # "-y" ensures no overwrite prompts
        ]

        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
        )

        with tqdm(total=100, desc="Merging Progress", unit="%") as pbar:
            for line in process.stderr:
                if "time=" in line:
                    parts = line.split()
                    for part in parts:
                        if "time=" in part:
                            time_str = part.split("=")[1]
                            time_parts = time_str.split(":")
                            seconds = (
                                int(time_parts[0]) * 3600
                                + int(time_parts[1]) * 60
                                + float(time_parts[2])
                            )
                            progress = min(int((seconds / 60) * 100), 100)
                            pbar.update(progress - pbar.n)

        process.wait()

        if process.returncode != 0:
            print(f"⚠️ FFmpeg error: {process.stderr.read()}")
        else:
            print("✅ Merging completed successfully!")

            # Cleanup temporary files
            os.remove(video_path)
            os.remove(audio_path)

    except Exception as e:
        print(f"❌ Error merging files: {e}")

def download_video(url, save_path=DOWNLOAD_DIR, audio_only=False):
    """Downloads a YouTube video in the highest quality (1080p+) with separate audio."""
    try:
        options = {
            "format": "bestaudio/best" if audio_only else "bestvideo+bestaudio",
            "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
        }
        
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print(f"Download completed: {url}\n")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_playlist(url, save_path=DOWNLOAD_DIR, audio_only=False):
    """Downloads all videos from a YouTube playlist in highest quality."""
    try:
        options = {
            "format": "bestaudio/best" if audio_only else "bestvideo+bestaudio",
            "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
        }
        
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Playlist download completed!\n")
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def main():
    """Handles command-line arguments and initiates downloads."""
    parser = argparse.ArgumentParser(description="YouTube Video & Playlist Downloader")
    parser.add_argument("urls", nargs="+", help="YouTube video or playlist URLs")
    parser.add_argument("-a", "--audio", action="store_true", help="Download audio only")
    parser.add_argument("-o", "--output", default=DOWNLOAD_DIR, help="Output directory")

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    for url in args.urls:
        if "playlist?list=" in url:
            download_playlist(url, args.output, args.audio)
        else:
            download_video(url, args.output, args.audio)

if __name__ == "__main__":
    main()
