#!/usr/bin/python
#
from flask import Flask, Response, json

app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def api_hello():
  data = {
      'hello': 'world',
      'number': 3
      }
  js = json.dumps(data)

  resp = Response(js, status=200, mimetype = 'application/json')
  resp.headers['Link'] = 'http://github.com'

  return resp

if __name__ == '__main__':
  app.run()

