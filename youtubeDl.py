from __future__ import unicode_literals
import youtube_dl
ydl_opts = {}
with youtube_dl.YouTubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/ubTNgeIYN9E'])
