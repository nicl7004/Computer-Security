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
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
  (buf, addr) = s.recvfrom(65565)

  #got this IP after inspecting my traffic with wireshark
  if "54.85.9.24" in addr:
    print("got one")

    # eth = dpkt.ethernet.Ethernet(byte)

    eth = dpkt.ethernet.Ethernet(buf)
    print(eth)
    # print 'Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type
    #
    # # Make sure the Ethernet frame contains an IP packet
    # if not isinstance(eth.data, dpkt.ip.IP):
    #     print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
    #     continue
    #
    # # Now unpack the data within the Ethernet frame (the IP packet)
    # # Pulling out src, dst, length, fragment info, TTL, and Protocol
    # ip = eth.data
    #
    # # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
    # do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
    # more_fragments = bool(ip.off & dpkt.ip.IP_MF)
    # fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
    #
    #
    # print(eth)
