import urllib.request
from urllib.parse import urlsplit as spl

import requests

#print(urllib.request.urlopen("http://192.168.43.171").read())
#print(requests.get("http://192.168.43.171", headers={"user-agent": "Firefox-5.0"}))
print(spl("http://127.0.0.1/kevin"))
#requests.post("http://192.168.43.171", data={"Username": "kevin", "password": "otsuganivek"})
