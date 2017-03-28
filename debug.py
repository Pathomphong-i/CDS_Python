import socket 
from threading import Thread
# from multiprocessing
import time	
"""

from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM, SERVO
##### Arduino #####
board = Arduino('/dev/ttyS0')
board.digital[3].mode = PWM #forward
board.digital[10].mode = PWM #revers

board.digital[12].mode = SERVO
##### End Arduino #####
"""
SYSTEM_STATUS = 1

CURRENT_GEAR = "N"
CURRENT_SPEED = 0
CURRENT_BREAK = 0
CURRENT_WHEELS_ANGLES = 0

accelerator = 0.0
brake = 0.0
forwardSpeed = 0.0
reverseSpeed = 0.0
forwardPWM = 0.0
reversePWM = 0.0


class Socker(object):
	"""docstring for Socker"""
	def __init__(self):
		return None

	def setSocket(self, host, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((host, port))
		sock.listen(1)
		return sock 

def gear(socket):
	try:
		while SYSTEM_STATUS != 0:
			conn, addr = socket.accept()
			gearSocketHandle(conn, addr)
	except:
		socket.close()
	finally: 
		print "Closed "

def speed_control(socket):
	try:
		while SYSTEM_STATUS != 0:
			conn, addr = socket.accept()
			movingSocketHandler(conn, addr)
	except:
		socket.close()
	finally: 
		print "Closed "


def movingSocketHandler(conn, addr):
	print "Connected Control", addr	
	try:
		while SYSTEM_STATUS != 0:
			raw_data = conn.recv(1024)
			dataHandler(raw_data)

	except :
		print "Controll is close"
		conn.close()

def gearSocketHandle(conn, addr):
	print "Connectd Gear ", addr
	try:
		while SYSTEM_STATUS != 0:
			raw_data = conn.recv(1024)
			if changeGearRequestDecoder(raw_data): #if gear can Change
				global CURRENT_GEAR 
				print "CURRENT GEAR is  ", CURRENT_GEAR
				changeGearReply(conn, "Yes")
				
			else:	#if gear Cant 
				print "Can not do this", raw_data
				changeGearReply(conn, "No")	
				
	except:
		conn.close()
		"Change Gear Closed"


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
					taskManager(in_head, in_data)
	else: #long data
		for h in range( _len ):
			if param[h] in __header__:
				in_data = '' #setdatanull
				in_head = param[h] #sethead				
			else:
				in_data = in_data+param[h]	


def taskManager(in_head, in_value):
	global CURRENT_SPEED
	global CURRENT_BREAK
	global CURRENT_WHEELS_ANGLES


	if in_head == 'a':
		print in_head, in_value

		a = float(in_value)
		#calDegree_180(a)
		#input_status(in_head,a)
		global accelerator 
		accelerator= a

	elif in_head == 'b':
		b = float(in_value)
		#input_status(in_head,b)
		global brake
		brake = b

	elif in_head == 't':
		t = int(in_value)
		#print ' spritT' + t
		calDegree_to_car(t) #TestMobileClient0-180


def changeGearRequestDecoder(data):
	if len(data) >= 2 and data[0] == "g":
		return setGear( data[1])
	else: 
		return False

def changeGearReply(conn, message):
	conn.sendall(message)


#####
def setGear(request):
	global CURRENT_GEAR 
	print "o" 

	if CURRENT_GEAR != request:
		print "i" 
		g = request
		CURRENT_GEAR = g
		return True
	else:
		return False

##### END NETCOM #####


##### MONITOR #####

def monitor():
	while True:
		print "Speeds: ",CURRENT_SPEED
		print "BREAK: ",CURRENT_BREAK
		print "Gear: ",CURRENT_GEAR
		print "Angles: ",CURRENT_WHEELS_ANGLES
		print "\n"
		time.sleep(1)
##### END  MONITOR #####

##### EMBED #####

def calDegree_to_car(degree180):
	left = 65
	right = 115
	carDegree = left+(((right-left)*degree180)/180)
	board.digital[12].write(carDegree)
### EMBED ###
def MoterControl():

	while SYSTEM_STATUS != 0:
		global accelerator, brake
		global decreaseSpeed
		global reverseMaxSpeed 	
		global forwardMaxSpeed 
		global motorPeriod 
		global CURRENT_GEAR
		if CURRENT_GEAR == 'D':
			gearD(accelerator,brake)
			
		# elif gear == 'r':
		# 	gearR(accelerator,brake)
		# elif gear == 'p':
		# 	gearP(accelerator,brake)
		# elif gear == 'n':
		# 	gearN(accelerator,brake)
		
		decreaseSpeed=5.0
		forwardMaxSpeed= 100.0
		reverseMaxSpeed= 30.0
		motorPeriod= 1.000
	


def gearD(accelerator,brake):


	defaultSpeed = 5.0
	decreaseSpeed = 0.5
	forwardMaxSpeed = 120.0
	global forwardSpeed

	
	accelerator_percent = accelerator/100
	#print accelerator_percent
	brake_percent = brake/100
	brake_percent
	
	if forwardSpeed == 0 and accelerator == 0 and brake != 0: #unAcc+brake
		
		forwardSpeed = 0
		
	elif forwardSpeed == 0 and accelerator == 0 and brake == 0:#unAcc+unBrake
		forwardSpeed = defaultSpeed
	
	
	else:
		
		forwardSpeed = forwardSpeed + accelerator_percent - brake_percent- decreaseSpeed
		#forwardSpeed = forwardSpeed + accelerator - brake -decreaseSpeed
		if forwardSpeed > forwardMaxSpeed:
			forwardSpeed = forwardMaxSpeed
		elif forwardSpeed <= defaultSpeed and brake == 0:
			forwardSpeed = defaultSpeed
		elif forwardSpeed < 0:
			forwardSpeed = 0


def driveD():
	while SYSTEM_STATUS != 0:
		global forwardSpeed
		if forwardSpeed < 5:
			pwmForword = 0.0
		else:
			pwmForword= 0.2+((0.8/120)*forwardSpeed)
		# print pwmForword
		board.digital[3].write(pwmForword)
	

def gearR(accelerator,brake):
	defaultSpeed = 5.0
	decreaseSpeed = 0.5
	reverseMaxSpeed = 40.0
	global reverseSpeed
	
	accelerator_percent = accelerator/100
	#print accelerator_percent
	brake_percent = brake/100
	brake_percent
	
	if reverseSpeed == 0 and accelerator == 0 and brake != 0: #unAcc+brake
		
		reverseSpeed = 0
		
	elif reverseSpeed == 0 and accelerator == 0 and brake == 0:#unAcc+unBrake
		reverseSpeed = defaultSpeed
	
	
	else:
		
		reverseSpeed = reverseSpeed + accelerator_percent - brake_percent- decreaseSpeed
		#forwardSpeed = forwardSpeed + accelerator - brake -decreaseSpeed
		if reverseSpeed > reverseMaxSpeed:
			reverseSpeed = reverseMaxSpeed
		elif reverseSpeed <= defaultSpeed and brake == 0:
			reverseSpeed = defaultSpeed
		elif reverseSpeed < 0:
			reverseSpeed = 0

def driveR():
	while SYSTEM_STATUS != 0:
		global reverseSpeed
		if reverseSpeed < 5:
			pwmReverse = 0.0
		else:
			pwmReverse= 0.2+((0.8/120)*reverseSpeed)
		
		board.digital[10].write(pwmReverse)
	

def gearP():
	board.digital[9].write(0.1)
	

def gearN():
	board.digital[10].write(0)

##############################################################################




if __name__ == '__main__':
	
	sock1 = Socker().setSocket("",7790)
	sock2 = Socker().setSocket("",7789)

	try:
		thread1 = Thread(target=gear, args=(sock1, ))

		thread2 = Thread(target=speed_control, args=(sock2, ))

		thread3 = Thread(target=monitor)

		thread4 = Thread(target=MoterControl )

		thread5 = Thread(target=driveD)

		thread6 = Thread(target=driveR)


# socket Gear Action
		thread1.start()
# socket Control Action
		# thread2.start()
		# thread3.start()# monitor

		# thread4.start()# 
		# thread5.start()# 
		# thread6.start()# 


		while True:
			inp = raw_input("_> ")
			if inp == "exit":
				sock1.close()
				sock2.close()
				
				SYSTEM_STATUS = 0

	except:
		sock1.close()
		sock2.close()
		print "Closeds"
	
