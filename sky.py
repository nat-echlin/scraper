from bs4 import BeautifulSoup
import requests, re

from class_Article import Article

_source = requests.get("https://news.sky.com/technology").text
soup = BeautifulSoup(_source, 'lxml')
# stories = []

def getSkyHeadline():
    headlineSoup = soup.find("a", attrs={"class":"sdc-site-tile__headline-link"})
    title, _url = headlineSoup.span.text, headlineSoup["href"]
    
    
    # print(headlineSoup.span.text)# REMOVE ME
    # print("x")# REMOVE ME
    # print(headlineSoup.text)# REMOVE ME

    # title = title.strip("/n/t/r") # REMOVE ME
    link = f"https://news.sky.com{_url}"
    
    return Article(title, link, isHeadline=True)
    
getSkyHeadline() # remove me




# print(getSkyHeadline())

def getSkyOthers():
    othersSoup = soup.find_all("a", attrs={"class":"sdc-site-tile__headline-link"})

    # urls = [story["href"] for story in othersSoup]

    listOfStoriesWithNoVideos = []
    for index, storySoup in enumerate(othersSoup):
        if not re.search("video", storySoup["href"]):
            listOfStoriesWithNoVideos.append(othersSoup[index])
        else:
            # if video, do nothing (ie dont add to new list)
            pass

    otherStories = []   # list of stories to return
    for story in listOfStoriesWithNoVideos:
        title, _url = story.span.text, story["href"]
        link = f"https://news.sky.com{_url}"
        otherStories.append(
            Article(title, link)
        )
    
    return otherStories




# getSkyOthers()
# for x in stories:
#     print(x.title)
