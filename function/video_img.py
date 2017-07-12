import requests
from bs4 import BeautifulSoup
import  re

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
content = request.content
soup = BeautifulSoup(content,"html.parser")
for element in soup.find_all('a',{"rel": "spf-prefetch"}):
    img_value = element.get('href').split("=")[1]
    all_img =  soup.find_all('img',{"alt":True,"width":True,"height":True,"onload":True,"data-ytimg":True}) #True有就抓
    img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value),str(all_img))).strip("[\"\']")  #\S非空白字元 strip去除
    video_img = img.replace("&amp;","&") #replace替換
    print(video_img)
