from bs4 import BeautifulSoup
import requests, re

_source = requests.get("https://www.theregister.com").content
soup = BeautifulSoup(_source, 'lxml')

# scienceSoup = soup.find('div', attrs={"class":"article_text_elements"})
# print(scienceSoup)

articleSoup = soup.find_all("article")
print(len(articleSoup))