import requests
from bs4 import BeautifulSoup
import  re
import youtube_dl

def find_search_content(search):
    request = requests.get("https://www.youtube.com/results?search_query={}".format(search))
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    return soup

def find_page_content(search):
    request = requests.get("https://www.youtube.com/results?{}".format(search))
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    return soup

def find_video(soup, all_item, i = 1):
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get('title')
        video_link = element.get('href')  # 裡面不是完整的網址

        img_value = element.get('href').split("=")[1]
        all_img = soup.find_all('img', {"alt": True, "width": True, "height": True, "onload": True,
                                        "data-ytimg": True})  # True有就抓
        img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip(
            "[\"\']")  # \S非空白字元 strip去除
        video_img = img.replace("&amp;", "&")  # replace替換

        all_item['{}'.format(i)] = {"title":video_title, "link":"https://www.youtube.com{}".format(video_link),"img":video_img}
        i = i + 1
    return all_item

def video_time(soup, all_item, i = 1):
    for time in soup.find_all('span', {"class": "video-time"}):
        all_item.get('{}'.format(i))['time'] = time.text
        i = i + 1
    return all_item

def every_video(soup):
    all_item = {}
    find_video(soup, all_item, i=1)
    video_time(soup, all_item, i=1)
    return all_item

def page_bar(soup):
    page = {}  # 一個字典

    for page_value in soup.find_all('a', {"class": True, "data-sessionlink": True, "data-visibility-tracking": True,
                                          "aria-label": True}):
        page['{}'.format(page_value.text)] = page_value.get('href')

    return page

def download_mp3(url):
    ydl_opts = {'format': 'bestaudio/best', 'outtmpl': './music/%(title)s.%(ext)s', 'nocheckcertificate': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_mp4(url):
    # 目前 youtube_dl 還是有這問題!可能以後會修正。
    # 但可以使用它內建的參數 youtube_dl search (nocheckcertificate) 讓它不驗證憑證 !
    ydl_opts = {'format': 'best', 'outtmpl': './video/%(title)s.%(ext)s', 'nocheckcertificate': True}  # 放到其他資料夾可以在這修改

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])