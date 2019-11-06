#!/usr/local/bin/python3.7
r"""Script to create a Python Dict of Windows UBR versions."""

import requests
import bs4
from collections import defaultdict

url_top_level = "https://docs.microsoft.com/en-us/windows/release-information/"
url = "https://winreleaseinfoprod.blob.core.windows.net/winreleaseinfoprod/en-US.html"

def parse_win_table(url):
    # print(url)
    sauce = requests.get(url)
    # print(sauce.content)
    soup = bs4.BeautifulSoup(sauce.content, "html.parser")
    # soup = bs4.BeautifulSoup(sauce.content, "html5lib")
    # print(soup.prettify())

    # lu = soup.find(text="Last Updated:")
    # print (lu)
    # exit()

    # for meta in soup.select('body'):
    #     print (meta)

    # Get the Last published date
    # p = soup.find('h3')
    # q = p.find_next_sibling('p')
    # r = q.next_sibling
    # print (r.split()[2])

    s = (soup.find('h3').find_next_sibling('p').next_sibling).split()[2]
    print (s)

    b = soup.find('body')
    c = (b.find_all('h3'))[1]
    # print (c[1].text)
    print (c.text)
    # exit()


    # l = b.find_all('table')
    # print(l[2])

    # for table in b.find_all('table'):
    #     print(table.extract())
    # exit()

    # Working code
    for t_row in b.find_all("tr")[1::]:
        t_data = t_row.find_all("td")
        if len(t_data) > 0:
            build_ubr = t_data[0].text
            release_date = t_data[1].text
            kb = t_data[3].text
            print ("{} {} {}".format(build_ubr, release_date, kb))

    # t = soup.find_all('h3')
    # print (t)
    # for h3 in t:
    #     if h3.text == "Windows 10 release history":
    #         print ("Gotcha!")

    exit()

    for meta in soup.select('body', text="Last Updated:"):
        print (meta.text)

    # if meta['style'] == "margin-top:0px;":
    #     # for meta in soup.find_all()
    #     print (meta.text)


def create_dict():
    build_ubr_dict_template = {
        "build": {
            "ubr": ["release_date", "kb"],
            "kbs": ["all_kbs"]
        }
    }

def main():
    r"Fabled main where it all begins."
    parse_win_table(url)
    exit()

    ubr = "/u/tmp/16299.lst"
    win10_ubr = create_dict()
    build_dict = {}
    ubr_dict = {}
    all_kbs = []
    with open (ubr, 'r') as f:
        for line in f:
            data = line.split()
            (build, ubr) = data[0].split('.')
            release_date = data[1]
            kb = data[-1]
            all_kbs.append(kb)
            ubr_dict[ubr] = [release_date, kb]
        build_dict[build] = ubr_dict
        build_dict["kbs"] = all_kbs
        # print (build_dict)
    print (build_dict["kbs"])
    print(build_dict["16299"]["431"])

if __name__ == "__main__":
    main()
