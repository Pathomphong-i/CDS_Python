import socket
import threading
import sys

IP = "192.168.137.1"
PORT1 = 7769
PORT2 = 7789

message = "-a phone"

cmd_list = [
	'-a', #auth
	'-cm', #change cotrol mode 
	'-cg' #change gear
]
class Client(threading.Thread):
	"""docstring for Client"""

	def __init__(self, name):
		super(Client, self).__init__()
		self.name = name

	def driverSocketResponse(self):
		while True:
			raw_data = self.driver_server.recv(1024)
			print raw_data

	def commandReciever(self):

		while True:
			raw_data = command_server.recv(1024)
			print raw_data
			
	def driverSender(self):

		self.driver_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.driver_server.connect((IP, PORT2))	
		self.driver_server.send(self.name)
		t2 = threading.Thread(target=self.driverSocketResponse)
		t2.start()


		while True:
			inp = raw_input("_>")

			if inp.split()[0] in cmd_list:
				self.command_server.send(inp)

			else:
				self.driver_server.send(inp)


	def run(self):
		global PORT1, PORT2
		command_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.command_server = command_server

		# Send Command socket
		self.command_server.connect((IP, PORT1))
		auth_message = "-a "+self.name
		self.command_server.send(auth_message)

		# Create Thread
		t1 = threading.Thread(target=self.driverSender)
		
		t1.start()
		
		
		
if __name__ == '__main__':

	inp =  str(sys.argv[1])

	if inp == None :
		inp = "PHONE"

	Client(inp).start()
