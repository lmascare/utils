#!/usr/bin/env python

import feedparser

def main():
    # url = 'http://wptavern.com/feed'
    url='http://www.reddit.com/r/python/.rss'
    d = feedparser.parse(url)

    print len(d['entries'])
    for post in d.entries:
        print(post.title + " | " + post.link + " | \n")


if __name__ == "__main__":
    main()