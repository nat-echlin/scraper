from bs4 import BeautifulSoup
import requests, re

from requests.api import head
from bbc import Article


_source = requests.get("https://news.sky.com/technology").text
soup = BeautifulSoup(_source, 'lxml')
stories = []

def getSkyHeadline():
    headlineSoup = soup.find("a", attrs={"class":"sdc-site-tile__headline-link"})
    title, _url = headlineSoup.text, headlineSoup["href"]
    link = f"https://news.sky.com{_url}"
    stories.append(
        Article(title, link, isHeadline=True)
    )

def getSkyOthers():
    othersSoup = soup.find_all("a", attrs={"class":"sdc-site-tile__headline-link"})

    # urls = [story["href"] for story in othersSoup]


    for index, storySoup in enumerate(othersSoup):
        if re.search("video", storySoup["href"]):
            othersSoup.pop(index)


    for x in othersSoup:
        print(x["href"])
        pass    


getSkyOthers()

# headline class: sdc-site-tile__headline-link
# elon sdc-site-tile__headline-link
# mask sdc-site-tile__headline-link