# ydl1.py
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://youtu.be/Ra0jm7CXudY"])

