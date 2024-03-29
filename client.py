# -*- coding: utf-8 -*-
import socket
import sys

HOST = sys.argv[1]
PORT = sys.argv[2]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, int(PORT)))
	request = "GET /" + sys.argv[3] + " HTTP/1.0\nHost: " + HOST + "\r\n"
	print("Connecting to server with request: \n", request)
	s.sendall(request.encode())
	data = s.recv(4096)
	print("Response: \n")
	print(data.decode())
	data = s.recv(4096)
	print(data.decode())
	s.close()

	