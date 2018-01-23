import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 502
MESSAGE = input("Input your number: ")

print "UDP IP:", UDP_IP
print "UDP port:", UDP_PORT
print "number:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print 'Answer from server: ' + data


