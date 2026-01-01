# YouTube Downloader

A simple command-line tool to download YouTube videos using Python.

## Features

- Download videos by providing a URL.
- Select video resolution (default: 720p).
- Specify custom output directory.
- Displays video metadata (Title, Views, Length).
- Progress bar during download.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

```bash
python downloader.py [URL] [OPTIONS]
```

### Arguments

- `url`: The URL of the YouTube video to download (Required).
- `-o`, `--output`: Output directory for the downloaded video (Default: `./downloads`).
- `-r`, `--resolution`: Quality of the video to download (Default: `720p`).

### Examples

**Download a video with default settings (720p):**
```bash
python downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Download a video at 360p:**
```bash
python downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -r 360p
```

**Save to a specific folder:**
```bash
python downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o "C:/My/Videos"
```

## Limitations

- Currently downloads "progressive" streams (video + audio in one file), which are typically limited to 720p. Higher resolutions (1080p, 4K) often require downloading video and audio separately and merging them, which is a planned feature.
