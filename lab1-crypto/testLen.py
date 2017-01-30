from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib

m = "Use HMAC, not hashes"
h = md5()
h.update(m)

print "\nInital message hash is:"
print h.hexdigest()
print "\n"

h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)

print(len(m))

paddedLength = (len(m) + len(padding(len(m)*8)))*8
pad = padding(len(m)*8)
print(paddedLength)
addition = "Good advice"
h.update(addition)
print "\nFinal message hash is:"
print h.hexdigest()
print"Hash of message + padding + suffix is:"
newMd5 = md5()
newMd5.update(m+pad+addition)
print newMd5.hexdigest()
print"##################################################################\n\n"

url ="https://ecen5032.org/project1/api?token=d0c7a65c690cf624cdc94dc551cc1c5c&user=admin&command1=ListFiles&command2=NoOp"
# find the toekn on a variable length url
location = url.index('token=')
location += 6
messageLocation = url.index('&user')
messageLength = len(url) - messageLocation
print("Original message length:")
print(messageLength)
print("\n")

token = ''
end = location+32
i = location

while (i < end):
    token += url[i]
    i +=1
print"Token is:"
print token
print"\nURL is:"
print url
newAddition = "&command3=DeleteAllFiles"
# pad = padding(messageLength+8+len(newAddition))

#do the hashiing

newH = md5(state=token.decode("hex"), count=512)
newH.update(newAddition)
newtoken=h.hexdigest()
print"\nNew token is:"
print newtoken

url += newAddition

url = url.replace(token, newtoken)

print "\n New URL is:"
# url = urllib.quote(url)
print url

# check = md5(state=token.decode("hex"), count=512)
# checkMessage = ''
# for each in range(messageLocation+5,len(url)):
#     checkMessage += url[each]
# print("\nMessage is:")
# print checkMessage
#
# check.update(checkMessage)
# #5d28a0a45dea4e9c9f702542ce5c6d48
# finalCryp = check.hexdigest()
#
# print"\n Check hash is:"
# print finalCryp

parsedUrl = urlparse.urlparse(url)
# print(parsedUrl)
conn = httplib.HTTPSConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print"\n Server Response:"
print conn.getresponse().read()
