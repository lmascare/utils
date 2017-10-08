#!/usr/bin/env python

from bs4 import BeautifulSoup

# xml_file = 'news_rss.xml'
# xml_file = 'site.xml'
xml_file = 'nytimes.xml'

f = open(xml_file.encode('utf-8').decode('ascii', 'ignore'), 'r')

soup = BeautifulSoup(f, "xml")
# print soup

# for item in soup.find_all('item'):
#     print item.title.text.encode('utf-8'), \
#         item.link.text.strip(), \
#         item.description.text.encode('utf-8'), \
#         item.content['url'] + "\n"

news_items = []
for item in soup.find_all('item'):
    news_item = {}
    news_item['title'] = item.title.text.encode('utf-8')
    news_item['link'] = item.link.text.strip()
    news_item['description'] = item.description.text.encode('utf-8')
    news_item['image'] = item.content['url']
    news_items.append(news_item)

print news_items