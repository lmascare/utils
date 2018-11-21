#!/usr/local/bin/python3
"""Script to watch Adobe Security page

This script looks at https://helpx.adobe.com/security.html and parses the
html file for all the products. It then determines if the page was updated
from the last check.
"""

import urllib.request
import bs4 as bs

url = "https://helpx.adobe.com/security.html"

def main():
    """Fabled main, where it all begins."""
    print (url)
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, "html.parser")

    # metatags = soup.find_all('meta', attrs = {'name': 'publishDate'})
    # for tag in metatags:
    #     print (tag)
    #     exit(0)

    #for meta in soup.find_all('meta', itemprop = 'publishDate'):
    for meta in soup.find_all('meta', attrs = {'name': 'publishDate'}, content=True):
        # print (type(meta))
        print ("Published Date : {}".format(meta.get('content')))
        # exit(0)
    #     # print (meta.get("content"))
               # meta = soup.find_all("meta", itemprop="publishDate")
    # print (meta)
    # print (soup.title.string)
    # print (soup.find_all("a"))
    # bulletin_items = soup.find(class_="current-article")
    bulletin_items = soup.find(class_="noHeader")
    # print (type(bulletin_items))

    b_href = bulletin_items.find_all("a")
    # print (type(b_href))
    # print (b_href)
    # print (type(b_h   ref))
    # Print the HREF records
    # for rec in b_href:
    #     print (rec.get("href"))
    #     exit(0)

    # Loop through the Table records
    for t_row in bulletin_items.find_all("tr")[1::]:
        t_data = t_row.find_all("td")
        # print (t_data[0])
        # print (t_data)

        # print (t_row)
        link = t_row.find_all("a")
        # print (link[0].get("href"))
        # #
        print ("Link    : {}\n"
               "Title   : {}\n"
               "Posted  : {}\n"
               "Updated : {}\n".format(link[0].get("href"), t_data[0].text, t_data[1].text, t_data[2].text))
        #exit(0)

    # a_recs = soup.find_all("a")

    # for rec in a_recs:
    #     print (rec)
    # # for link in soup.find_all("a"):
    #      print(link.get("href"))

if __name__ == "__main__":
    main()