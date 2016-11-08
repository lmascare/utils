#!/usr/bin/python3

# From the archive, follow each link, find the image in that
# linked page, and download the image

# Concepts
# 1. Downloading stuff --> urllib
# 2. Parsing stuff out of HTML --> BeautifulSoup

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "http://apod.nasa.gov/apod/archivepix.html"
#base_url = "http://web.mit.edu/jesstess/www/scraper_test/"
download_dir = "apod_pictures"

to_visit = set((base_url,))
visited = set()

while to_visit:
  # Pick a link to visit
  # Visit the link
  current_page = to_visit.pop()
  print("Visiting:", current_page)
  visited.add(current_page)
  content = urllib.request.urlopen(current_page).read()

  # For each link on the index page
  for link in BeautifulSoup(content, "lxml").findAll("a"):
     # print("Following link:", link)
     absolute_link = urljoin(current_page,link["href"])
     if absolute_link not in visited:
       to_visit.add(absolute_link)
     else:
       print("Already visited:", absolute_link)

  # Follow the link and pull down the image on that linked page
  for img in BeautifulSoup(content, "lxml").findAll("img"):
       img_href = urljoin(current_page, img["src"])
       print("Downloading image:", img_href)
       img_name = img_href.split("/")[-1]
       urllib.request.urlretrieve(img_href, os.path.join(download_dir, img_name))

