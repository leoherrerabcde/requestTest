
import requests

url = "http://192.168.8.102:3000/api/areas"

print "The url is:"
print url

r = requests.get(url)

print "The get request response is:"
print (r.text)
