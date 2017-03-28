import socket
import Queue


class Server(object):

	"""docstring for Server"""
	def __init__(self):
		super(Server, self).__init__()		
		self.SYSTEM_STATUS = 0 

		"""
		Status of car model
		"""
		self.CURRENT_SEED = 0
		self.CURRENT_GEAR = "N"
		self.CURRENT_WHEEL_ANGLES = 0

		"""
		Sueue of order from data reciever  
		"""
		self.TASK_QUEUE = Queue.Queue() 

		"""
		Phone Object socket
		"""
		self.PHONE = None

		"""
		Driver suit Object socket 
		"""
		self.DRIVER = None
		""" 
		Determine 
		0 = Phone Control
		1 = Driver Control
		None = No Client 
 		"""
		self.CONTROL_MODE = None

	def start(self):
		self.SYSTEM_STATUS = 1
		print "Start System"

	def start_service(self):
		while SYSTEM_STATUS == 1 :
			handleSocket()
			hardwarExcutor()

	def taskManager(self, param):
		in_head, in_value = '',''
		__header__ = ['a','b','t','g']
		_len = len(param)


		if( _len <= 4):
			for h in range( _len ):
				if param[h] in __header__ :
					in_head = param[h] #sethead			
				else:
					in_value = in_value+param[h]	
					if h == _len-1: 
						TASK_QUEUE.put( (in_head, in_value) )
		else: 	
			for h in range( _len ):
				if param[h] in __header__:
					in_value = '' #setdatanull
					in_head = param[h] #sethead				
				else:
					in_value = in_value+param[h]

	def speedControl(self, param):
		
		while True :
			if CURRENT_GEAR not in ["N", "P"]:
				pass
			elif CURRENT_GEAR is "P":
				pass
			elif CURRENT_GEAR is "R":
				pass
			else:
				pass 

	def hardwarExcutor(self):
		while SYSTEM_STATUS == 1 :
			if not self.TASK_QUEUE.empty():
				task = TASK_QUEUE.get();


	def changeModeControl(self, mode):
		
		if mode != CONTROL_MODE :
			self.CONTROL_MODE = mode
		
	def tcp(self):
		

	def handleSocket(self):
		tcp_server = TCPSocket.start()
		while True :



class TCPSocket(object):
	"""docstring for TCPSocket"""

	def __init__(self, addr, port):
		super(TCPSocket, self).__init__()
		self.addr = addr
		self.port = port
		
		
	def start(self):
		server_info = (addr, port)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(server_info)
		sock.listen(2)

	def guard(self, client):
		client.sendall("Whoareyou")

		data = client.recv(128);
		if( data == "ImPhone"):
			pass
		elif( data == "ImDriver"):
				pass
