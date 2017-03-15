import socket
''' capture packets
then look for http request to free.xyz


once we see a request generate a resoponse to that request

inject that response




look in wire shark at get request'''


'''part3
if number of synax recived is less than 1/3 then throw an error'''

#step 1

#create an INET, STREAMing socket
#serversocet.recve (socket.af_packet socket.sock_raw, eithernet)
# serversocket = socket.socket(
#     socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#
# #bind the socket to a public host,
# # and a well-known port
#
# # serversocket.bind((socket.gethostname(), 80))
# #become a server socket
# # serversocket.recv()
# # socket.create_connection(("54.85.9.24", 80))
# # serversocket.listen(5)
# # server_ip = "54.85.9.24"
# # client_ip = socket.gethostbyname(socket.gethostname())
# while 1:
#     x , y = serversocket.recvfrom(65565)
#     print(x,y)

    # print(worked)

    #accept connections from outside
    #packet = socket.recv(socekt)
    #1.a = capture packets

    #1.b = wait for request to the website
    #use hostname to find the stuff u want



    # (clientsocket, address) = serversocket.accept()
    # print(clientsocket, address)
    # if freeaeskey.xyz in packet:
    #     print("Got one")
    # #now do something with the clientsocket
    # #in this case, we'll pretend this is a threaded server
    # print("hello")
    # ct = client_thread(clientsocket)
    # ct.run()


#Packet sniffer in python
#For Linux

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
  print s.recvfrom(65565)
