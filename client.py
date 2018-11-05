# -*- coding: utf-8 -*-
import socket
import sys


HOST = "192.168.1.5"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	message = "GET /HelloWorld.html HTTP/1.1\nHost: 192.168.1.5\n\n"
	s.sendall(str.encode(message))
	data = s.recv(1024)
	print('Received message from', (data.decode()))
	s.close()
