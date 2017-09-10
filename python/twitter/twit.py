#!/usr/bin/python

import twitter

CONSUMER_KEY = 'ujwr34Ctuz9QD1QWSrNIwncHp'
CONSUMER_SECRET = 'cENs3wRlTpNlHoCBCE7dns71q1dG2m3wWPricnBlyxyxd5AMm9'
OAUTH_TOKEN = '4268137473-KxAreuRmYiglsBylN6eUNsSApaZzDVTKoDNSYZ4'
OAUTH_TOKEN_SECRET = 'zhoGAbXvFHLfhTduIGnJ2PCrsVfg8X0VLSCK4H4u3LXKS'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)