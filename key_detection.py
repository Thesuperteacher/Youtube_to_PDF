# key_detection.py

from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)

def detect_key_moments(transcript):
    """
    Summarizes each transcript segment while preserving timestamps.
    """
    try:
        summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        steps = []
        for start_time, text in transcript:
            if len(text.strip()) == 0:
                continue  # Skip empty segments
            summary = summarization_pipeline(text, max_length=50, min_length=5, do_sample=False)
            summarized_text = summary[0]['summary_text']
            steps.append((start_time, summarized_text))
        return steps
    except Exception as e:
        logging.error(f"Key moment detection failed: {e}")
        raise
