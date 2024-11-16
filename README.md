# YouTube to Step-by-Step PDF Guide Converter

Convert YouTube instructional videos into detailed, step-by-step PDF guides.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [Running the Program](#running-the-program)
- [Modules Explanation](#modules-explanation)
  - [`main.py`](#mainpy)
  - [`transcription.py`](#transcriptionpy)
  - [`key_detection.py`](#key_detectionpy)
  - [`snapshots.py`](#snapshotspy)
  - [`pdf_generator.py`](#pdf_generatorpy)
- [Troubleshooting](#troubleshooting)
- [Additional Notes](#additional-notes)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project transforms a YouTube instructional video into a comprehensive, step-by-step PDF guide. It automates the following workflow:

1. **Download Video and Audio**: Utilizes `yt-dlp` to download the video and extract the audio stream.
2. **Transcribe Audio**: Employs Hugging Face's Whisper model to transcribe the audio content.
3. **Detect Key Moments**: Summarizes the transcription to identify crucial instructional steps.
4. **Capture Video Frames**: Extracts frames from the video at timestamps corresponding to the key steps.
5. **Generate PDF**: Compiles the text and images into a neatly formatted PDF document.

---

## Features

- **Automated Workflow**: Seamlessly converts instructional videos into PDF guides without manual intervention.
- **Accurate Transcription**: Uses state-of-the-art models for high-quality audio transcription.
- **Dynamic Summarization**: Identifies key steps by summarizing transcribed text.
- **Visual Aids**: Captures relevant video frames to enhance understanding.
- **Portable Output**: Generates a PDF that can be easily shared and printed.

---

## Project Structure

The project directory `youtube_to_pdf` is organized as follows:

```
youtube_to_pdf/
├── main.py            # Main script to run the workflow
├── transcription.py   # Module for transcription functions
├── key_detection.py   # Module for detecting key steps from transcript
├── snapshots.py       # Module for capturing video frames
├── pdf_generator.py   # Module for assembling PDF
├── requirements.txt   # Dependencies list
```

---

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **FFmpeg** installed and added to your system's PATH
  - [FFmpeg Download](https://ffmpeg.org/download.html)
- **pip** package manager

### Install Dependencies

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your_username/youtube_to_pdf.git
cd youtube_to_pdf
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Ensure all dependencies are installed without errors.

---

## Usage

### Running the Program

1. Open `main.py` and replace the placeholder URL with your desired YouTube video URL:

   ```python
   video_url = "https://www.youtube.com/watch?v=your_video_id"  # Replace with your video URL
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. The program will process the video and generate a PDF file named `step_by_step_tutorial.pdf` in the project directory.

---

## Modules Explanation

### `main.py`

- **Purpose**: Orchestrates the entire workflow by coordinating all modules.
- **Function**: `create_step_by_step_guide(video_url)`
  - Downloads audio and video from YouTube.
  - Transcribes audio using Whisper.
  - Detects key moments in the transcript.
  - Captures video frames at key moments.
  - Generates a PDF document with text and images.

### `transcription.py`

- **Purpose**: Handles downloading audio and transcribing it.
- **Functions**:
  - `download_audio(video_url)`: Downloads audio from YouTube and saves it as `audio.wav`.
  - `transcribe_with_whisper(audio_path)`: Transcribes audio using Hugging Face's Whisper model and splits it into timed segments.

### `key_detection.py`

- **Purpose**: Summarizes the transcript to extract key instructional steps.
- **Function**: `detect_key_moments(transcript)`
  - Summarizes each transcript segment while preserving timestamps.
  - Dynamically adjusts `max_length` and `min_length` for summarization based on input length.

### `snapshots.py`

- **Purpose**: Downloads the video and captures frames at specified timestamps.
- **Functions**:
  - `download_video(video_url)`: Downloads video from YouTube and saves it as `video.mp4`.
  - `capture_frames(video_path, steps)`: Captures frames from the video at the timestamps corresponding to each step.

### `pdf_generator.py`

- **Purpose**: Compiles the extracted text and images into a PDF document.
- **Function**: `create_pdf_with_snapshots(steps)`
  - Creates a PDF with each step's description and corresponding snapshot.
  - Handles image scaling to maintain aspect ratio.

---

## Troubleshooting

### 1. Permission Errors on Windows

- **Issue**: Encountering `PermissionError` when accessing temporary files.
- **Solution**: The `pdf_generator.py` module uses `tempfile` to handle temporary files correctly. Ensure that files are properly closed and deleted after use.

### 2. Download Errors with `yt-dlp`

- **Issue**: Errors occur when downloading audio or video streams.
- **Solutions**:
  - Update `yt-dlp` to the latest version:

    ```bash
    pip install --upgrade yt-dlp
    ```

  - Check internet connectivity and verify the video URL.
  - If HTTP 403 errors persist, clear the cache:

    ```bash
    yt-dlp --rm-cache-dir
    ```

  - Modify `ydl_opts` in the download functions to include a user-agent header if necessary.

### 3. Warnings from Transformers

- **Issue**: Warnings about `max_length` during summarization.
- **Solution**: The `detect_key_moments` function adjusts `max_length` and `min_length` dynamically to match the input size, preventing warnings and errors.

---

## Additional Notes

- **Performance Considerations**: Processing large videos may be resource-intensive. Ensure your system has adequate memory and CPU capacity.
- **Error Handling**: The code includes try-except blocks and logging for easier debugging.
- **Logging**: Execution progress and errors are logged to the console for transparency.
- **Dependencies Versions**: Specific versions are listed in `requirements.txt` to maintain compatibility.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add your feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- [FPDF for Python](http://pyfpdf.readthedocs.io/en/latest/)
- [MoviePy](https://zulko.github.io/moviepy/)

---

**Enjoy converting your favorite instructional videos into handy PDF guides!**