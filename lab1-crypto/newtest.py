import urllib2
req = urllib2.urlopen('https://ecen5032.org/project1/api?token=d0c7a65c690cf624cdc94dc551cc1c5c&user=admin&command1=ListFiles&command2=NoOp')

try:
    urllib2.urlopen(req)
    html = response.read()
    print(the_page)

except URLError, e:
     print e.code
     print e.read()
