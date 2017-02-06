#!/usr/bin/python
#
import json

arr = [ 100, 500, 300, 200, 400 ]

print("Python Array element0 --> {}".format(arr[0]))

json_str = json.dumps(arr)
print("JSON String --> {}".format(json_str))

