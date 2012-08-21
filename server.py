import socket #this library allows Python to interface with the operating system's socket API

def get_req(site,port):
	s=socket.socket() #socket() returns a socket object and assigns it to the variable s
	s.connect((site,port)) #tells the socket object to connect at a particular socket address
	s.send('GET / \r\n\r\n') #not sure if i need the \r's here for universal new line support (http://docs.python.org/library/functions.html#open)
	response=s.recv(1024) #the socket object receives requests on port 1024, and returns a string which is assigned to response
	response_bucket=[]
	while response: #while there is a response string
		response_bucket.append(response) #append response to response_bucket
		response=s.recv(1024) #updates value of response to avoid infinite loop
	bucket_join = "".join(response_bucket)	#concatenates elements in the response_bucket list
	return bucket_join #returns a string	

server_socket=7000
def server_side():
	s=socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #setsockopt takes socket.setsockopt(level, optname, value) 
	s.bind(('10.242.11.81', server_socket)) #binds the socket object to an IP address (first parameter) at a particular port (second parameter)
	print 'ip to hit:'
	print '10.242.11.81:' + str(server_socket)
	s.listen(5)
	while True:	
		ephemeral, client_ip = s.accept() #s.accept() returns a port and an ip address
		print "sending response"
		ephemeral.send('HTTP/1.1 200 OK \r\n\r\n Response!')
		ephemeral.close()

#should accept another response on the same port; needs to create another ephemeral 
#loop after listen
server_side()
