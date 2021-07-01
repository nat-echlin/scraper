from bs4 import BeautifulSoup
import requests, re

# s = requests.Session(   )

_source = requests.get("").content
soup = BeautifulSoup(_source, features="xml")

print(_source)


# needs serious work here. xml feed seems to not work, error 403 : robot detected.
# https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file
# https://docs.python-requests.org/en/latest/api/#sessionapi