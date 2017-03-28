from multiprocessing import Process, Value
import socket
import time	
import threading
from threading import Thread,Event
import sys

CURRENT_SPEED = 0

class CarSystem(object):
	# from multiprocessing import Process
	"""docstring for CarSystem"""

	DEVICE_MOBILE = None #Mobile device
	DEVICE_DRIVING = None	#Driving device

	def __init__(self):
		# super(CarSystem, self).__init__()

		self.CURRENT_SPEED = 0
		self.CURRENT_GEAR = 0
		self.CURRENT_WHEELS_ANGLES = 0

		self.CONTROL_MODE = 0
		self.STATUS = "on"

	def getSpeed(self):
		return self.CURRENT_SPEED

	def bindSocket(self, connection):
		try:
			while True:
				
		except:
			raise
		finally:
			connection.close()

	def main(self):
		socket1 = self.Server("",7789)
		for sock in socket:
			conn, addr = sock.accept()


	def gearHandler(client, request):

		if request != self.CURRENT_GEAR: 
			client = SocketResponse(client, request)
			return "1"

		else :
			return "0"

	def monitor(self):
		while True:
			print "Speeds: ",self.CURRENT_SPEED
			print "Gear: ",self.CURRENT_GEAR
			print "Angles: ",self.CURRENT_WHEELS_ANGLES
			print "\n"
			time.sleep(1)

	def dataHandler(param):
				in_head, in_data = '',''
				__header__ = ['a','b','t','g']
				_len = len(param)
				if( _len <= 4): #short data
					for h in range( _len ):
						if param[h] in __header__ :
							in_head = param[h] #sethead			
						else:
							in_data = in_data+param[h]	
							if h == _len-1:
								task(in_head, in_data)
				else: #long data
					for h in range( _len ):
						if param[h] in __header__:
							in_data = '' #setdatanull
							in_head = param[h] #sethead				
						else:
							in_data = in_data+param[h]	
		

# Server Class 

	class Server(object):
		def __init__(self, hostname, port):
			import logging
			self.logger = logging.getLogger("server")
			self.hostname = hostname
			self.port = port

		def taskManager(data):
			if in_head == 'a':
				raise
			elif in_head == 'b':
				raise
			elif in_head == 't':
				raise
			elif in_head == 'g':
				gearHandler(in_data)
			else:
				raise	    

		def socketHandler(self, connection, address):
			while True:
				data = connection.recv(1024)
				self.dataHandler(data)

		






if __name__ == "__main__":
	import logging
	import multiprocessing

	taskQueue = Qu
	msys = CarSystem()

	msys.main()



	# logging.basicConfig(level=logging.DEBUG)
	# server = Server("", 7789)
	# try:
	#     logging.info("Listening")
	#     server.start()
	# except:
	#     logging.exception("Unexpected exception")
	# finally:
	#     logging.info("Shutting down")
	#     for process in active_children():
	#         logging.info("Shutting down process %r", process)
	#         process.terminate()
	#         process.join()
	# logging.info("All done")


### global Variable
var SYSTEM_STATUS
var CURRENT_SEED, CURRENT_GEAR, CURRENT_WHEEL_ANGLES
var CONTROL_MODE


### main process 

fun runner :
	stand by
	controller

### stand by module
stand by for connection
	if (have some connection)
		check is device ?
			yes :
				put into device controller
			now : 
				decline package


### controller module
var mode is in [phone, driver]

# Object of device by Socket connection
var client = [] 