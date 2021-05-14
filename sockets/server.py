#coding:utf-8

import socket
import threading

# make a thread to manage several connexions in the same time
class ThreadforClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.conn = conn
	def run(self):

		# retrieve the client data and display it
		# choose a buffer size (number squared)
		data = self.conn.recv(1024)
		print(data.decode("utf8"))




# configure socket
socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conf adress and port (tuple)
socket_1.bind(("", 1234))

print("server started...")

while True:
	# allow such number of connexion failures (5) before deny 
	# (optional after python 3.5)
	socket_1.listen(5)
	conn, addr = socket_1.accept()
	print("one client has just connected")

	my_thread = ThreadforClient(conn)
	my_thread.start()


# always close the connexion and the socket
conn.close()
socket_1.close()