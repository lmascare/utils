#!/usr/bin/python
#

from flask import Flask, url_for, request, json

app = Flask(__name__)

@app.route('/messages', methods = ['POST'])
def api_message():

  if request.headers['Content-Type'] == 'text/plain':
    return "Text Message: " + request.data

  elif request.headers['Content-Type'] == 'application/json':
    return "JSON Message: " + json.dumps(request.json)

  elif request.headers['Content-Type'] == 'application/octet-stream':
    f = open('./binary', 'wb')
    f.write(request.data)
    f.close()
    return "Binary message written"

  else:
    return "415 Unsupported Media type ;)"

if __name__ == '__main__':
    app.run()
