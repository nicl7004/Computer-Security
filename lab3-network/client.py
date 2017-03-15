import urllib.request
response = urllib.request.urlopen('http://freeaeskey.xyz/')
html = response.read()
print(html)
