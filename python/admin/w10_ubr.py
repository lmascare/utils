#!/usr/local/bin/python3.7
r"""Script to create a Python Dict of Windows UBR versions."""

import requests
import bs4
import pprint

url_top_level = "https://docs.microsoft.com/en-us/windows/release-information/"
url = "https://winreleaseinfoprod.blob.core.windows.net/winreleaseinfoprod/en-US.html"
html_file = "/u/admin/tmp/win_build_ubr.html"


def dwnload_html(url, html_file):
    r"""Download the HTML page to a file."""

    with open(html_file, "w") as f:
        h = (requests.get(url)).text
        f.write(h)
    return (0)


def parse_win_table_v1(html_file):
    r"""Parse the HTML document, one tag at a time."""
    # Parse the downloaded file to reduce HTTP calls.
    with open(html_file, "r") as f:
        sauce = f.read()

    soup = bs4.BeautifulSoup(sauce, "html.parser")

    update = (soup.find('h3').find_next_sibling('p').next_sibling).split()[2]
    print (update)

    for x in soup.find_all('h4'):
        t = x.find_next_sibling('table')
        os_details = x.text.replace(')','').split()
        os_ver = os_details[2]
        os_build = os_details[5]
        if (os_ver == '1507'):
            os_build = os_details[-1]
        for t_row in t.find_all("tr")[1::]:
            t_data = t_row.find_all("td")
            (build, ubr) = t_data[0].text.split('.')
            release_date = t_data[1].text
            k = (t_data[3].text)
            if len(k) > 0:
                kb = k.split()[-1]
            else:
                kb = t_data[3].text
            print (os_ver, os_build, build, ubr, release_date, kb)
    exit()


def parse_win_table(html_file):
    r"""Parse the HTML document, one tag at a time."""
    # Parse the downloaded file to reduce HTTP calls.
    with open(html_file, "r") as f:
        sauce = f.read()

    soup = bs4.BeautifulSoup(sauce, "html.parser")

    update = (soup.find('h3').find_next_sibling('p').next_sibling).split()[2]
    print (update)

    build_dict = {}
    for x in soup.find_all('h4'):
        t = x.find_next_sibling('table')
        os_details = x.text.replace(')','').split()
        os_ver = os_details[2]
        os_build = os_details[5]
        if (os_ver == '1507'):
            os_build = os_details[-1]
        all_kbs = []
        ubr_dict = {}
        for t_row in t.find_all("tr")[1::]:
            t_data = t_row.find_all("td")
            (build, ubr) = t_data[0].text.split('.')
            release_date = t_data[1].text
            k = (t_data[3].text)
            if len(k) > 0:
                kb = k.split()[-1]
            else:
                kb = t_data[3].text
            all_kbs.append(kb)
            ubr_dict[ubr] = [release_date, kb, build]
            # print (os_ver, os_build, build, ubr, release_date, kb)
        ubr_dict["kbs"] = all_kbs
        build_dict[os_ver] = ubr_dict
        # pprint.pprint(build_dict)
        # exit()
    pprint.pprint(build_dict)
    exit()


def create_dict():
    build_ubr_dict_template = {
        "build": {
            "ubr": ["release_date", "kb", "os_build"],
            "kbs": ["all_kbs"]
        },
        "1909": {
            "116": ['2019-05-21', "4505057", "18362"],
            "kbs": ["4505057", "4497935", "4503293"]
        }
    }

def main():
    r"Fabled main where it all begins."

    # Enable as needed html_file = dwnload_html(url)
    os_ver_dict = parse_win_table(html_file)
    pprint.pprint(os_ver_dict)
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
