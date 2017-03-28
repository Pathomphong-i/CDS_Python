import threading 
import time
import Queue

VAR = 0 

def increase():

	while True: 
		time.sleep(0.5)
		global VAR 
		VAR = VAR+1 

def show():
	while True:
		time.sleep(1)
		global VAR
		print VAR

if __name__ == '__main__':
	
	inc = threading.Thread(target=increase)
	shw = threading.Thread(target=show )

	try:
		inc.start()
		shw.start()
	except KeyboardInterrupt as e:
		inc.exit()
		shw.exit()
