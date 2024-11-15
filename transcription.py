# transcription.py

import yt_dlp
from transformers import pipeline
import logging
import os

logging.basicConfig(level=logging.INFO)

def download_audio(video_url):
    """
    Downloads the audio from YouTube and saves it as 'audio.wav'.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        audio_path = 'audio.wav'
        if not os.path.exists(audio_path):
            raise FileNotFoundError("Audio file not found after download.")
        return audio_path
    except Exception as e:
        logging.error(f"Failed to download audio: {e}")
        raise

def transcribe_with_whisper(audio_path):
    """
    Transcribes the audio using Whisper.
    """
    try:
        whisper_pipeline = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-base",
            chunk_length_s=30
        )
        result = whisper_pipeline(audio_path)
        text = result['text']
        # For simplicity, we assume each sentence is a segment
        segments = text.split('. ')
        transcript = []
        current_time = 0.0  # Starting timestamp
        for segment in segments:
            transcript.append((current_time, segment.strip()))
            # Increment timestamp estimate (this is a simplification)
            current_time += 30.0  # Assuming each segment is about 30 seconds
        return transcript
    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        raise
