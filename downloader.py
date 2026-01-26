import argparse
import os
import ssl
from pytubefix import YouTube, Stream
from pytubefix.cli import on_progress

# --- BYPASS SSL VERIFICATION ---
# This fixes the "CERTIFICATE_VERIFY_FAILED" error by ignoring strict certificate checks.
ssl._create_default_https_context = ssl._create_unverified_context
# -------------------------------

def main():
    parser = argparse.ArgumentParser(description="A simple YouTube video downloader.")
    parser.add_argument("url", type=str, help="URL of the YouTube video to download.")
    parser.add_argument("-o", "--output", type=str, default="./downloads", help="Output directory for the downloaded video.")
    parser.add_argument("-r", "--resolution", type=str, default="720p", choices=["2160p","1440p", "1080p", "720p", "480p", "360p", "240p", "144p"], help="Quality of the video to download.")
    
    # Use -a to enable. Do not pass "True" or "False".
    parser.add_argument("-a", "--audio_only", action="store_true", help="Download only the audio.")

    args = parser.parse_args()

    try:
        # Use oauth=False or True depending on if you need age-gated content, 
        # but usually default is fine. Added use_oauth=True just in case for stability.
        yt = YouTube(args.url, on_progress_callback=on_progress)

        print(f"Title:  {yt.title}")
        print(f"Views:  {yt.views:,}")
        print(f"Length: {yt.length // 60}m{yt.length % 60}s")
        print("-" * 30)

        if not args.audio_only:
            # "Progressive Streams" contain both audio and video in a single file.
            stream = yt.streams.filter(resolution=args.resolution, progressive=True).first()
            if not stream:
                print(f"Notice: {args.resolution} progressive stream not available.")
                choice = input(f"Would you like to download the highest available quality progressive stream? [y]/n: ").lower()
                if choice in ["", "y", "yes"]:
                    stream = yt.streams.get_highest_resolution(progressive=True)
                else:
                    print("Skipping download.")
                    return # Exit cleanly rather than raising a string exception

            if stream:
                print(f"Fetching: {stream.resolution} stream...")
                stream.download(output_path=args.output)
                print("\nDownload Complete!")
            else:
                print("Error: No downloadable streams found.")

        else:
            print(f"Fetching audio stream...")
            stream = yt.streams.get_audio_only()
            stream.download(output_path=args.output)
            print("\nDownload Complete!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()