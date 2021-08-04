import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def findAllTheLinks(url):
    if url == "" or None:
        return ""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    extract_links = []
    for link in soup.find_all('a'):
        extract_links.append(link.get('href'))

    internal_links = ["<ul>"]
    external_links = ["<ul>"]
    for link in extract_links:
        if link[0] == "/":
            internal_links.append('<li>'+link+'</li>')
        elif "http" in link:
            external_links.append('<li>'+link+'</li>')
    internal_links.append('</ul>')
    external_links.append('</ul>')
    allTheLinks = {"internal": internal_links, "external": external_links}
    return allTheLinks
