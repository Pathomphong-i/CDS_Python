import socket
import sys
import struct
from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM, SERVO
from time import sleep

board = Arduino('/dev/ttyS0')
board.digital[3].mode = PWM
board.digital[12].mode = SERVO


global accelerator,brake,gear,forwardSpeed,reverseSpeed,forwardPWM,reversePWM
accelerator = 0.0
brake = 0.0
gear = 'd'
forwardSpeed = 0.0
reverseSpeed = 0.0
forwardPWM = 0.0
reversePWM = 0.0


########################################################
def server():
	server_addr = '192.168.100.1'
	server_port = 7789 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.bind((server_addr, server_port))
	sock.listen(4)

	return sock

########################################################

def decode(param):
	in_head = ''
	in_data = ''

	decode = ""
	__header__ = ['a','b','t','g']

	_len = len(param)

	if( _len <= 4):

		for h in range( _len ):

			if param[h] in __header__ :
				#print 'decode :'+in_head +in_data
				
				#in_data = '' #setdatanull
				in_head = param[h] #sethead
				
			else:
				in_data = in_data+param[h]	
				if h == _len-1:
					sprit(in_head,in_data)
					#print 'decode:' +in_head +in_data
				## decode done

	else: 
	
		for h in range( _len ):
			#print param[h]
			
			if param[h] in __header__:
				#print 'decode :'+in_head +in_data
				in_data = '' #setdatanull
				in_head = param[h] #sethead
				
			else:
				in_data = in_data+param[h]	


			#sprit(in_head,in_data)
			# elif (param[h] in __header__ ) & (in_data != ''):
			# 	print 'decode :'+in_head +in_data
			# 		# 	in_data = ''
			# 		# 	in_head = param[h]
			# 		# 	#sprit(in_head,in_data)
			
		
		
	#inputData(in_head,in_data)
#######################################################

def sprit (in_head,in_data):
	
	if in_head == 'a':
		a = float(in_data)
		#calDegree_180(a)
		#input_status(in_head,a)
		global accelerator 
		accelerator= a


	elif in_head == 'b':
		b = float(in_data)
		#input_status(in_head,b)
		global brake
		brake = b
	
	elif in_head == 't':
		t = int(in_data)
		#print ' spritT' + t
		calDegree_to_car(t) #TestMobileClient0-180
	
	elif in_head == 'g':
		g= str(in_data)
		global gear
		gear = g
		#input_status(in_head,g)
	


##################Turn##########################################################
###########Turn#############Turn################################################
def calDegree_180(turnPercen):
	degree=(turnPercen*180)/100
	calDegree_to_car(degree)
	
def calDegree_to_car(degree180):
	left = 65
	right = 115
	carDegree = left+(((right-left)*degree180)/180)
	board.digital[12].write(carDegree)

#############################################################################
##################RUN####RUN###RUN#####RUN###################################

def MoterControl(accelerator,brake,gear):
	
	if gear == 'd':
		gearD(accelerator,brake)
		
	# elif gear == 'r':
	# 	gearR(accelerator,brake)
	# elif gear == 'p':
	# 	gearP()
	# elif gear == 'n':
	# 	gearN()
	
	global decreaseSpeed
	decreaseSpeed=5.0
	global forwardMaxSpeed 
	forwardMaxSpeed= 100.0
	global reverseMaxSpeed 
	reverseMaxSpeed= 30.0
	global motorPeriod 
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

def driveD(forwardSpeed):
	if forwardSpeed < 5:
		pwmForword = 0.0
	else:
		pwmForword= 0.2+((0.8/120)*forwardSpeed)
	
	board.digital[3].write(pwmForword)
	print pwmForword
	# MoterRange = 1

	# timePuse = (MoterRange * forwardSpeed)/120
	# timeSleep = MoterRange - timePuse
	
	# board.digital[9].write(1)
	# sleep (timePuse)
	# board.digital[9].write(0)
	# sleep(timeSleep+0.1)

	# board.digital[9].write(1)
	# sleep ((forwardSpeed/forwardMaxSpeed)*motorPeriod)
	# board.digital[9].write(0)
	# sleep(motorPeriod-((forwardSpeed/forwardMaxSpeed)*motorPeriod))

# def gearR(accelerator,brake):
# 	if reverseSpeed == 0.0 and accelerator == 0.0 and brake != 0.0: #unAcc+brake
# 			reverseSpeed = 0.0
		
# 	elif reverseSpeed == 0.0 and accelerator == 0.0 and brake == 0.0:#unAcc+unBrake
# 		reverseSpeed=defaultSpeed
	
	
# 	else:
# 		reverseSpeed = reverseSpeed+accelerator-brake-decreaseSpeed
# 		if reverseSpeed > reverseMaxSpeed:
# 			reverseSpeed = reverseMaxSpeed
# 		elif reverseSpeed <= defaultSpeed and brake == 0.0:
# 			reverseSpeed = defaultSpeed
# 		elif reverseSpeed < 0.0:
# 			reverseSpeed=0.0


# 	board.digital[13].write(1)
# 	sleep ((reverseSpeed/reverseMaxSpeed)*motorPeriod)
# 	board.digital[13].write(0)
# 	sleep(motorPeriod-((reverseSpeed/reverseMaxSpeed)*motorPeriod))

# def gearP():
# 	board.digital[9].write(1)
# 	sleep(10)
# 	board.digital[9].write(0)
# 	sleep(motorPeriod-10)

# def gearN():

# 	board.digital[9].write(0)
# 	board.digital[10].write(0)
##############################################################################



def run():

	sock = server()

	print >> sys.stderr, 'waiting for data'
	connection, client_address = sock.accept()


	try:
		print >> sys.stderr, 'conncet form' ,client_address

		while True:
			
			
			data = connection.recv(1024)
			
			# print "data: "+type(data),"utf: "+utf,"asc: "+asc ;
			# print int(data.decode('hex'))
			
			decode(data)
			# MoterControl(accelerator,brake,gear)
			#print 'input :' +data
			#print accelerator
			#print brake
			# print forwardSpeed
			#driveD(5)
			MoterControl(accelerator,brake,gear)
			driveD(forwardSpeed)
			
	except KeyboardInterrupt:
		sys.exit()
		connection.close()
		sock.close()

	finally:
		print "Close"
		connection.close()
		sock.close()
		run()
###############################################################


run()