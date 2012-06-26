import socket

def get_req(site,port):
	s=socket.socket()
	s.connect((site,port))
	s.send('GET / \r\n\r\n')
	response=s.recv(1024)
	response_bucket=[]	
	while response:
		response_bucket.append(response)
		response=s.recv(1024)
	bucket_join = "".join(response_bucket)	
	return bucket_join	

#print get_req('google.com',80)
server_socket=7000
def server_side():
	s=socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('10.242.11.81', server_socket))
	print 'ip to hit:'
	print '10.242.11.81:' + str(server_socket)
	s.listen(5)
	while True:	
		ephemeral, client_ip = s.accept()
		print "sending response"
		ephemeral.send('HTTP/1.1 200 OK \r\n\r\n Response!')
		ephemeral.close()

#should accept another response on the same port; needs to create another ephemeral 
#loop after listen
server_side()
