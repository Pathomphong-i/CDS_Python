# import server_pc 
import socket 
import Queue
import threading

"""
Status of car model
"""
SYSTEM_STATUS = 0 

"""

"""
CURRENT_SPEED = 0
CURRENT_GEAR = "N"
CURRENT_WHEEL_ANGLES = 0

"""
Static Value
"""
DEFALUT_SPEED = 0
DEFALUT_GEAR = "N"

"""
Queue of order from data reciever
"""
TASK_QUEUE = Queue.Queue() 

"""
Phone Object socket
"""
PHONE = None

"""
Driving SIMULATOR set Object socket
"""
SIMULATOR_SET = None

"""
Current Driver Object socket 
"""
DRIVER = None

""" 
Determine 
0 = Phone Control
1 = Driver Control
None = No Client 
"""
CONTROL_MODE = None

CLIENT = []

THREAD_POOL = []

HOST = "192.168.137.1"

def socketAuth(message):
	pass

def socketRegistrar(addr, driver):
	global PHONE, SIMULATOR_SET, CLIENT
	new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	new_sock.settimeout(5)
	new_sock.bind(( HOST, 7789))

	if driver is "PHONE":
		PHONE = (conn, addr)
		return True

	elif driver is "SIMULATORSET" :
		SIMULATOR_SET = (conn, addr)
		return True

	else:
		return False


def socketAuthenticate(conn, addr):
	conn.settimeout(0.5)
	conn.send("-c Who're you")
	auth_data = conn.recv(1024)

	try:
		if auth_data == "-a PHONE":
			socketRegistrar(addr, "PHONE")

		elif auth_data == "-a SIMULATORSET" :
			socketRegistrar(addr, "SIMULATORSET")

		else:
			return None 
	except:
		print addr," connection failed to Authenticate"
			
def changeModeControl(current, to):
	if DRIVER == current :
		DRIVER = to
		return "Done"
	else:
		return None

def ManageDriving():
	if DRIVER != None :
		new_thread = threading.Thread(name="Driver",target)
		THREAD_POOL.append(new_thread)
	else:
		CURRENT_SPEED = DEFALUT_SPEED 

"""
Set Current Speed 
"""
def CurrentSpeedControl(driver):

	global CURRENT_SPEED
	global CONTROL_MODE
	global TASK_QUEUE

	try:
		while True:
			data = driver.recv(128)
			print data
	except:
		print "something is wrong"




"""
Command Motor By CURRENT_SPEED
"""
def MotorControl(var):
	## 
	pass

def SystemCommand(command):
	global SYSTEM_STATUS
	if command == "shutdown":
		SYSTEM_STATUS = 0
	elif command == "start":
		SYSTEM_STATUS =1
	else:
		pass


if __name__ == '__main__':

	SystemCommand("start")


	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind( (HOST, 7769) )
	sock.listen(4)
	while True: 
		conn, addr = sock.accept()

		print "New Connection from ", addr 

		new_thread = threading.Thread(name="Socket Command", target=socketAuthenticate, args=(conn, addr) )

		THREAD_POOL.append(new_thread)
		new_thread.start()



	# thread socket

	# thread controller

	#Test Commit