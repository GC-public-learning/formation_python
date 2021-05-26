#coding:utf-8

import socket

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# conf host and port (tuple)
	socket_1.connect(("127.0.0.1", 1234))

	print("client connected...")

	# send data
	data = "hi ééé!"
	socket_1.sendall(data.encode("utf8"))

except  ConnectionRefusedError as e:
	print("Error ! : ", e)

except:
	print("Unknown Error ! : Connexion server failed") 
finally:
	socket_1.close()
	print("socket closed")

