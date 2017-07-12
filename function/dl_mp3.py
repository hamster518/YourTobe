import youtube_dl

ydl_opts = {'format': 'bestaudio/best', 'outtmpl': './video/%(title)s.%(ext)s','nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BEULybZnLO8'])