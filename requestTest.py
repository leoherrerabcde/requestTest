
import requests
import socket

url = "http://192.168.8.102:3000/api/areas"

print "The url is:"
print url

r = requests.get(url)

print "The get request response is:"
print (r.text)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = socket.gethostbyname('127.0.0.1') 
s.connect((host_ip, 4000))


print "the socket has successfully connected on port == %s" %(host_ip)
