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
    for storySoup in otherStoriesList:
        regexp = "^Video [0-9]+"
        if len(re.findall(regexp, storySoup.text)) == 0:
            title = storySoup.text
        else:
            title = storySoup.text.split('seconds')[1]
        _url = storySoup["href"]
        link = f"https://www.bbc.co.uk{_url}"
        stories.append(
            Article(title, link)
        )
    
def printTitles():
    for story in stories:
        print(story.title)   


# main story class:      gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor
# other storys class:    gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor
