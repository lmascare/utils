#!/usr/bin/python


import urllib
import urllib2

'''
TODO
    - Send username / password tokens to download data
      Complete
      
    - Use proxies
      Complete
'''

'''
Introducing urllib and encoding data
'''
def url_data():
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {
        "Name"      : "Michael Foord",
        "location"  : "Northampton",
        "language"  : "Python"
    }
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    print data, headers

    req = urllib2.Request(url,data, headers)
    response = urllib2.urlopen(req)

'''
Work with a Proxy
'''
def url_proxy():
    url = 'http://www.ibm.com'
    proxy = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080',
                                     'https': 'https://127.0.0.1:8080'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    urllib2.urlopen(url)

'''
Work with username and password
'''
def url_passwd():
    # Create a password manager
    passwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Added the username and password
    # If we know the realm, use it instead of None
    url = 'http://www.example.org/foo.html'
    passwd_mgr.add_password(None, url, 'username', 'password')
    handler = urllib2.HTTPBasicAuthHandler(passwd_mgr)

    # Create an opener (OpenerDirector Instance)
    opener = urllib2.build_opener(handler)

    # Use the opener to fetch the URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener
    urllib2.install_opener(opener)

    html_page = urllib2.urlopen(url)


'''
Work with errors
'''
def url_httperrors():
    url = 'http://123.python.org/fish.html'
    req = urllib2.Request(url)

    try:
        urllib2.urlopen(req)

    except urllib2.HTTPError as e:
        print "Code --> {}".format(e.code)
        #print e.read()

    except urllib2.URLError as u:
        print "Reason --> {}".format(u.reason)

    else:
        html_page = response.read()



'''
Here we simply send a URL and receive the page. Introductory
'''
def read_page():
    req = urllib2.Request('http://python.org')
    response = urllib2.urlopen(req)
    html_page = response.read()
    #print html_page


'''
The fabled Main. Where it all begins.
'''
def main():
    #read_page()
    #url_data()
    #url_httperrors()
    url_passwd()


if __name__ == "__main__":
    main()