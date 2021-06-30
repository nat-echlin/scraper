from bs4 import BeautifulSoup
import requests, re
from class_Article import Article


_source = requests.get("https://www.bbc.co.uk/news/technology").text
soup = BeautifulSoup(_source, 'lxml')
stories = []
        
# Scraping headline story

def getBbcHeadline():
    storySoup = soup.find('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"})
    title, _url = storySoup.text, storySoup["href"]
    link = f"https://www.bbc.co.uk{_url}"
   
    return Article(title, link, isHeadline=True)
    

# Scraping all other stories

def getBbcOthers():
    otherStoriesListSoup = list(set(soup.find_all('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})))
    
    otherStories = []
    for index, storySoup in enumerate(otherStoriesListSoup):
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
        otherStories.append(
            Article(title, link)
        )
    return otherStories

# main story class:      gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor
# other storys class:    gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor


# def init():
#     getBbcHeadline()
#     getBbcOthers()
#     printTitles()

# init()