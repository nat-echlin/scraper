from bs4 import BeautifulSoup
import requests, re

from requests.api import get
from class_Article import Article

# s = requests.Session()

headers = {
    "User-Agent":"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

_source = requests.get("https://www.theregister.com/headlines.atom", headers=headers).content
soup = BeautifulSoup(_source, features="xml")

# print(soup.prettify())
    


def getRegister():
    stories = []
    entryList = soup.find_all('entry')
    for entry in entryList:
        title = entry.title.text
        link = entry.link["href"]
        stories.append(
            Article(title, link)
        )
    return stories

# print(getRegister()[5].link)






# entry = soup.find('entry')
# print(f"title : {entry.title.text}")
# print(f"link : {entry.link['href']}")


# https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file
# https://docs.python-requests.org/en/latest/api/#sessionapi
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36


# got round bot protection by using user agent headers!!! thanks sol 

