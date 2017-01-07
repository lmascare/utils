#!/usr/bin/env python3

import json

data = {
        'name' : 'Acme',
        'shares' : 50,
        'price' : 542.33
        }

json_str = json.dumps(data)

print(json_str)

data1 = json.loads(json_str)
print(data1)
