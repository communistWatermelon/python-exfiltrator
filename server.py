import socket
import threading
import sys

# change this port to whatever you like, just make sure you forward the ports from your router to your computer on the same one, 
# or else you won't be able to recive data from the internet
port = 1337   

# this function will be called as a thread, so that the server can handle multiple clients at the same time
# all this server will do right now is accept connections, print out the ip address of the client, and await data
def serverThread(clientSocket, clientAddress):
	print("Connection from: ", clientAddress)

	# loop forever, getting data
	while True:
		# get 16 characters from the client at a time
		data = clientSocket.recv(16)

		# if you actually got any data
		if data:
			# print it out
			# the '\t' is just the tab character, making the output look a bit better
			print '\t',  data

				# if you wanted to, you could instead write the data to a log file

		else:
			# otherwise, close the connection
			break

	# after you are done getting 
	clientSocket.close()

def startServer():
	# create the server socket (AF_INET is the address family you need for IP sockets, 
		# while SOCK_STREAM indicates that you want to use TCP)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# bind the socket to a specific port, on your machine
	server.bind(('', port))

	# begin listening for connection requests on the server socket
	server.listen(1)

	# loop forever, waiting for connections
	while True:
		# this is a blocking call, so you won't move past this line of code until you get a connection
		client, address = server.accept()
		
		# this is multithreading stuff, making it so your program can handle multiple clients at the same time
			# it just passes the client socket and the client address to the function above, but as a seperate thread
		clientThread = threading.Thread(target=serverThread, args = (client, address))
		# the daemon bit is optional, but it just closes the thread as soon as the program ends. Zombie threads are bad threads.
		clientThread.daemon = True
		clientThread.start();


startServer()