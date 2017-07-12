import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
content = request.content
soup = BeautifulSoup(content,"html.parser")
for time in soup.find_all('span',{"class": "video-time"}):
    print(time.text) #<span aria-hidden="true" class="video-time">3:55</span>  <---原本加上.text是為了只要顯示文字