import socket
import scapy
import dpkt
# import binascii

''' capture packets
then look for http request to free.xyz


once we see a request generate a resoponse to that request

inject that response




look in wire shark at get request'''


'''part3
if number of synax recived is less than 1/3 then throw an error'''


import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP,)

# receive a packet
while True:
  (byte, addr) = s.recvfrom(65565)
  print(byte,addr)
  if "54.85.9.24" in addr:
    print("got one")

    eth = dpkt.ethernet.unpack(byte)


    print(eth)
