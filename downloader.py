import argparse
import os
from pytubefix import YouTube, Stream
from pytubefix.cli import on_progress

def main():
    parser = argparse.ArgumentParser(description="A simple YouTube video downloader.")
    parser.add_argument("url", type=str, help="URL of the YouTube video to download.")
    parser.add_argument("-o", "--output", type=str, default="./downloads", help="Output directory for the downloaded video.")
    parser.add_argument("-r", "--resolution", type=str, default="720p", choices=["2160p","1440p", "1080p", "720p", "480p", "360p", "240p", "144p"],help="Quality of the video to download.")
    
    # parser.add_argument("-a", "--audio_only", type=bool, default=False, help="Download only the audio.")  TODO: Implement this.
    
    args = parser.parse_args()

    try:
        yt = YouTube(args.url, on_progress_callback=on_progress)
    
        print(f"Title:  {yt.title}")
        print(f"Views:  {yt.views:,}")
        print(f"Length: {yt.length // 60}m{yt.length % 60}s")
        print("-" * 30)
        
        # "Progressive Streams" contain both audio and video in a single file. Only available at 720p and below. TODO: Implement 1080p video with sound included.
        stream = yt.streams.filter(resolution=args.resolution, progressive=True).first()

        if stream is None:
            print(f"Notice: {args.resolution} progressive stream not available.")
            print("Defaulting to the highest available progressive stream (usually 720p)...")
            stream = yt.streams.get_highest_resolution()
        
        if stream:
            print(f"Fetching: {stream.resolution} stream...")
            # The on_progress callback will handle the printing of the progress bar
            stream.download(output_path=args.output)
            print("\nDownload Complete!")
        else:
            print("Error: No downloadable streams found.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()