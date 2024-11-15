# main.py

from transcription import transcribe_with_whisper, download_audio
from key_detection import detect_key_moments
from snapshots import capture_frames, download_video
from pdf_generator import create_pdf_with_snapshots

def create_step_by_step_guide(video_url):
    try:
        # Step 1: Download the audio from YouTube
        audio_path = download_audio(video_url)
        print("Audio downloaded successfully.")

        # Step 2: Transcribe the audio using Whisper
        transcript = transcribe_with_whisper(audio_path)
        print("Transcription completed.")

        # Step 3: Detect key moments in the transcript
        steps = detect_key_moments(transcript)
        print("Key moments detected.")

        # Step 4: Download the video for snapshot capture
        video_path = download_video(video_url)
        print("Video downloaded successfully.")

        # Step 5: Capture video frames at key moments
        snapshots = capture_frames(video_path, steps)
        print("Snapshots captured.")

        # Step 6: Create a PDF with text and snapshots
        create_pdf_with_snapshots(snapshots)
        print("PDF generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the guide creation
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=q047DlB04tw&ab_channel=PixelEasel"  # Replace with your video URL
    create_step_by_step_guide(video_url)
