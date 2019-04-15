# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:35:50 2013
@author: zbg
"""

import socket
import threading

inString = ''
outString = ''
nick = ''


def DealOut(s):
    global nick, outString
    while True:
        outString = input()
        outString = nick + ': ' + outString
        s.send(bytes(outString, encoding='utf-8'))


def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print(inString)

        except:
            break


nick = input("input your nickname: ")
ip = input("input the server's ip adrress: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 8888))
sock.send(bytes(nick, encoding='utf-8'))

thin = threading.Thread(target=DealIn, args=(sock,))
thin.start()
thout = threading.Thread(target=DealOut, args=(sock,))
thout.start()

# sock.close()