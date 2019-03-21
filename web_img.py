import sys
from urllib.parse import urlsplit
import re
if (len(sys.argv)==1):
	print("Web Image Scrapper By Kevin Agusto")
	print("Usage: python web_img.py [https/http]://url")
	sys.exit(0)

url = sys.argv[1]
urls = urlsplit(url)
allimage = []
data = b""
sys.exit(0)
if (urls.scheme=="https"):
	import http.client as hc
	a = hc.HTTPSConnection(urls.netloc)
	a.request("GET", urls.path)
	data = a.getresponse().read()
else:
	import socket
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	con.connect((urls.netloc, 80))
	req = b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nCookie: ciNav=no\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
	con.send(req)
	data = con.recv(10000) #max is 10 mb
