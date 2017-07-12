import youtube_dl

#目前 youtube_dl 還是有這問題!可能以後會修正。
#但可以使用它內建的參數 youtube_dl search (nocheckcertificate) 讓它不驗證憑證 !
ydl_opts = {'outtmpl': './video/%(title)s.%(ext)s','nocheckcertificate':True} #放到其他資料夾可以在這修改

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BEULybZnLO8'])