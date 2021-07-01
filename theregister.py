from bs4 import BeautifulSoup
import requests, re

_source = requests.get("").content
soup = BeautifulSoup(_source, features="xml")

print(_source)


# needs serious work here. xml feed seems to not work, error 403 : robot detected.