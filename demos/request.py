import requests
import re

r = requests.get('https://www.taobao.com/')
print(type(r))
print(r.text)
