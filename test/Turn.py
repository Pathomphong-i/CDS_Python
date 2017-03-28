import socket
import sys
import struct
from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM, SERVO
from time import sleep
board = Arduino('/dev/ttyS0')
board.digital[9].mode = PWM
board.digital[10].mode = PWM
board.digital[12].mode = SERVO
#board.digital[12].write(90) #set 90 middle

#print "car driving simmulator"


def server():
	server_addr = '192.168.100.1'
	server_port = 7789 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.bind((server_addr, server_port))
	sock.listen(4)

	return sock



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


def sprit (in_head,in_data):
	
	#print in_head,in_data
	# a = 0.0
	# b = 0.0
	# t = 0.0
	# g = ''
	
	
	if in_head == 'a':
		a = float(in_data)
		
		
		
		
	elif in_head == 'b':
		b = float(in_data)
	
	elif in_head == 't':
		t = float(in_data)
		calDegree_to_car(t)
		

	elif in_head == 'g':
		g= str(in_data)

	

##################Turn###########################
###########Turn#############Turn##################
def calDegree_180(turnPercen):
	degree=(turnPercen*180)/100
	calDegree_to_car(degree)
	
def calDegree_to_car(degree180):
	left = 65
	right = 115
	carDegree = left+(((right-left)*degree180)/180)
	#Turn(carDegree)
	print carDegree
	board.digital[12].write(carDegree)
# def Turn(degree):
# 	sevoRange = 0.002

# 	timePuse = (sevoRange * degree)/180
# 	timeSleep = sevoRange - timePuse
# 	board.digital[13].write(1)
# 	sleep (timePuse)
# 	board.digital[13].write(0)
# 	sleep(timeSleep+0.018)
	
# def Turn(degree):
# 	servoT = 0.020 #T20ms
# 	servoStart = 0.001 #1ms
# 	servoStop = 0.002 #2ms
# 	servoWidth = servoStop - servoStart

# 	timePuse =   servoStart + ((servoWidth*degree)/180)
# 	timeSleep = servoT - timePuse

# 	print timePuse 
# 	board.digital[13].write(1)
# 	sleep (timePuse)
# 	board.digital[13].write(0)
# 	sleep(timeSleep)					
	

###################################################




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
				
			
					
	except KeyboardInterrupt:
		sys.exit()
		connection.close()
		sock.close()

	finally:
		print "Close"
		connection.close()
		sock.close()
		run()
 


run()