import redis
import base64
from clastic import Application, render_basic


def hello(url='please add the url'):
    encode = base64.b64encode(url)[:5]
    r.set(encode, url)
    return 'localhost:5000/mapping/' + encode


def shorten(request):
    for k in request.values:
        if k in "url":
            url = request.values[k]
            encode = base64.b64encode(url)[:8]
            r.set(encode, url)
            return 'localhost:5000/mapping/' + encode


def decode(encode=''):
    if encode is '':
        return 'No url to return'
    else:
        return r.get(encode)

routes = [('/', hello, render_basic),
          ('/shorten', shorten, render_basic),
          ('/mapping/<encode>', decode, render_basic)]
          # ,
          # ('/<url>', hello, render_basic)]

r = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Application(routes)
app.serve()
