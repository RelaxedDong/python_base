from socket import *


HOST = '127.0.0.1'
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
print('...waiting for message..')

while True:
    data, address = s.recvfrom(1024)
    print(data, address)
    print(address)
    s.sendto(bytes('this is the UDP server', encoding='utf-8'), address)