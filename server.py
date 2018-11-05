#import socket module
from socket import *
import sys # In order to terminate the program
import threading


class ServerThreading(threading.Thread):
	
	def __init__(self, client, ip, port):
		threading.Thread.__init__(self)
		self.connectionSocket = client
		self.ip = ip
		self.port = port
		
	def run(self):
		try:
			message = connectionSocket.recv(1024)
			filename = message.split()[1]
			f = open(filename[1:])
			outputdata = f.readlines()
			#Send one HTTP header line into socket
			connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
			connectionSocket.send("Content-Type: text/html\r\n".encode())

			#Send the content of the requested file to the client
			for i in range(0, len(outputdata)):
				connectionSocket.send(outputdata[i].encode())
			connectionSocket.send("\r\n".encode())

			connectionSocket.close()
		except IOError:
			#Send response message for file not found
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
			#Close client socket
			connectionSocket.close()
		


server = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
HOST = "192.168.1.5"
PORT = 12345
serverName = "John Michael's Server"
server.bind((HOST, PORT))
server.listen()

while True:
	#Establish the connection
	print('Ready to serve...')
	(connectionSocket, (ip, port)) = server.accept()
	thread = ServerThreading(connectionSocket, ip, port)
	thread.start()

		
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data 


