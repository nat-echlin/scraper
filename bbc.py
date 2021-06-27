from bs4 import BeautifulSoup
import requests, re

_source = requests.get("https://www.bbc.co.uk/news/technology").text
soup = BeautifulSoup(_source, 'lxml')
stories = []


class Article:
    def __init__(self, title, link, isHeadline=False):
        self.title = title
        self.link = link
        self.isHeadline = isHeadline
        
# Scraping headline story

def scrapeHeadline():
    storySoup = soup.find('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"})
    title, _url = storySoup.text, storySoup["href"]
    link = f"https://www.bbc.co.uk{_url}"

    stories.append(
        Article(title, link, isHeadline=True)
    )

# Scraping all other stories

def scrapeOthers():
    otherStoriesList = list(set(soup.find_all('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})))
    for index, storySoup in enumerate(otherStoriesList):
        regexp = "^Video [0-9]+"
        if re.search(regexp, storySoup.text):
            # title = storySoup.text
            title = storySoup.text.split('seconds')[1]
        else:
            # title = storySoup.text.split('seconds')[1]
            title = storySoup.text
            


        _url = storySoup["href"]
        if re.search('playlist', _url):
            link = _url
        else:        
            link = f"https://www.bbc.co.uk{_url}"
        stories.append(
            Article(title, link)
        )

# Fn to print all titles, numbered 

def printTitles():
    for number, story in enumerate(stories):
        if story.isHeadline:
            print(f"{number + 1}.   HEADLINE:   {story.title}\n")
        else:
            print(f"{number + 1}.    {story.title}\n")   


# main story class:      gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor
# other storys class:    gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor


def init():
    scrapeHeadline()
    scrapeOthers()
    printTitles()

    def getFollowInput(maxStory):    
        storyToFollowRaw = input("Please enter the number of the story you would like to follow up on!")
        if re.search('[a-zA-Z]', storyToFollowRaw) or int(storyToFollowRaw) < 1 or int(storyToFollowRaw) > maxStory:
            print(f"Please ONLY enter a number between 1 and {maxStory}")
            getFollowInput(maxStory)
        else:
            return int(storyToFollowRaw)

    toFollow = getFollowInput(len(stories))
    print(stories[toFollow - 1].link)
    
init()
    
# address bug: link is wrong when story has a video
