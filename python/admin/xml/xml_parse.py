#!/usr/bin/env python

import urllib
import bs4 as bs

def main():
    # url = 'https://pythonprogramming.net/parsemencparseface/'
    # url = 'https://pythonprogramming.net/'
    # url = 'https://apod.nasa.gov/apod/archivepix.html'
    url = 'https://pythonprogramming.net/sitemap.xml'

    sauce = urllib.urlopen(url).read()
    # print sauce
    #soup = bs.BeautifulSoup(sauce, "lxml")
    soup = bs.BeautifulSoup(sauce, "xml")
    # print soup

    # print(soup.find_all('p'))
    # for para in soup.find_all('p'):
    #     print(para.text)
    #
    # for url in soup.find_all('a'):
    #     print(url.get('href'))

    for url in soup.find_all('loc'):
        print(url.text)


if __name__ == "__main__":
    main()