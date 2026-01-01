from pytubefix import YouTube
from sys import argv

url = argv[1]

yt = YouTube(url)

print(f"Title: {yt.title}\nViews: {yt.views}\nLength: {yt.length}")

if yt.streams.get_by_resolution("1080p") is not None:
    yt.streams.get_by_resolution("1080p").download("./downloads")
else:
    yt.streams.get_highest_resolution().download("./downloads")