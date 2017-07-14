#!/usr/bin/python

import urllib2

req = urllib2.Request('http://python.org')
response = urllib2.urlopen(req)
html_page = response.read()
print html_page