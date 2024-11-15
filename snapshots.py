# snapshots.py

import yt_dlp
from moviepy.editor import VideoFileClip
import logging
import os

logging.basicConfig(level=logging.INFO)

def download_video(video_url):
    """
    Downloads the video from YouTube and saves it as 'video.mp4'.
    """
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        video_path = 'video.mp4'
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video file not found after download.")
        return video_path
    except Exception as e:
        logging.error(f"Failed to download video: {e}")
        raise

def capture_frames(video_path, steps):
    """
    Captures video frames at specified timestamps.
    """
    try:
        clip = VideoFileClip(video_path)
        duration = clip.duration
        snapshots = []
        for timestamp, description in steps:
            # Adjust timestamp if it's beyond video duration
            timestamp = min(timestamp, duration - 1)
            frame = clip.get_frame(timestamp)
            snapshots.append((timestamp, description, frame))
        clip.close()
        return snapshots
    except Exception as e:
        logging.error(f"Snapshot capture failed: {e}")
        raise
