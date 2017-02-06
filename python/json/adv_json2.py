#!/usr/bin/python
#

import json

with open('lm.json') as f:
    name = json.load(f)
    print len(name), name[0]['LastName'] 
    type(name)
    for details in name:
        print details['FirstName'], details['LastName']
        print details
