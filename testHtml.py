import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

uri = 'http://192.168.8.102:3000'
path = '/api/areas'

print "The url is:"
print uri+path

target = urlparse(uri+path)
method = 'GET'
body = ''

print "The target:"
print target

h = http.Http()

# If you need authentication some example:
#if auth:
#    h.add_credentials(auth.user, auth.password)

response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)

# assume that content is a json reply
# parse content with the json module
data = json.loads(content)
