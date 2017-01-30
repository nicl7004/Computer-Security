


import httplib, urlparse, sys
import urllib
from pymd5 import md5, padding

# url = sys.argv[1]
# Your code to modify url goes here
url ="https://ecen5032.org/project1/api?token=d0c7a65c690cf624cdc94dc551cc1c5c&user=admin&command1=ListFiles&command2=NoOp"
# find the toekn on a variable length url
location = url.index('token')
location += 6
messageLocation = url.index('&user')
messageLength = len(url) - messageLocation

print("\n\n")
print(messageLength)
print("\n\n")

token = ''
end = location+32
i = location

while (i < end):
    token += url[i]
    i +=1

print token
print url
#do the hashiing

h = md5()

h = md5(state=token.decode("hex"), count=512)

h.update('&command3=DeleteAllFiles')


token=h.hexdigest()
i=0
print("\n\n")
print token
print("\n\n")
url = list(url)

while(i<32):
    url[location+i]=token[i]
    i+=1

strurl = ''.join(url)
print strurl


m = "Use HMAC, not hashes"
h = md5()
h.update(m)
print("\n\n")
print("\n\n")
print h.hexdigest()
print("\n\n")
h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)
print(len(m))

newPad = padding(len(m)*8)

generatePad = ''
for each in range(0,(448-(len(m)*8)),1):
    if each ==0:
        generatePad +='\\x80'

    else:
        generatePad += '\\x00'

generatePad += '\\xa0'#str(hex(len(m)*8))
print("Pad = \n")
print(generatePad)
x = "Good advice"
newMd5 = md5(m + newPad +x )

print newMd5.hexdigest()


h.update(x)
print h.hexdigest()
print("\n\n")
