import socket

IP = "192.168.137.1"
PORT = 7769

message = "-a phone"

if __name__ == '__main__':
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.connect((IP, PORT))
		server.send(message)

		while True:
			data = server.recv(1024)
			print data

			if data == "Succeed" :
				inp = raw_input(">_")
				server.send(inp)




	except Exception as e:
		raise e
	finally:
		pass


		#test 3

		#asdsads
