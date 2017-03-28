from pyfirmata import Arduino, util
from time import sleep
 
board = Arduino('/dev/ttyS0')
print "car driving simmulator"
from pyfirmata import INPUT, OUTPUT, PWM, SERVO
from time import sleep
board = Arduino('/dev/ttyS0')

board.digital[3].mode = PWM
while True:
	
	board.digital[3].write(0.7)