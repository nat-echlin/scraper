from bs4 import BeautifulSoup
import requests, re

# s = requests.Session()

headers = {
    "User-Agent":"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

_source = requests.get("https://www.theregister.com/headlines.atom", headers=headers).content
soup = BeautifulSoup(_source, features="xml")

# print(soup.prettify())


entryList = soup.find_all('entry')
print(entryList.title.text)

def getRegister():
    titleList = soup.find_all("title")

# print(len(titleList))
# needs serious work here. xml feed seems to not work, error 403 : robot detected.
# https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file
# https://docs.python-requests.org/en/latest/api/#sessionapi
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36