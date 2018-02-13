#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

import random

try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		numero = str(random.randint(0, 3122332432))
		print('HTTP request received:')
		print(recvSocket.recv(1024))
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    	"<html><body><p>Hola. " + 
                    	'<a href=' + "http://localhost:1234/" + numero + '"' +
						'>' + 
                    	"Dame otra<\n>" +
                    	"</p></body></html>" +
                    	"\r\n", 'utf-8'))
		recvSocket.close()
except KeyboardInterrupt:
	print("Closing binded socket")
	mySocket.close()
