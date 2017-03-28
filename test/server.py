import multiprocessing
import thread 
import socket

def reply(client, data):
	try: 
		clinet.sendall()
	except:
		passs

def gearHandler(request):
	if requesta != "": 
		return "1"

	else :
		return "2"

def response(connection, data):
	try:
		connection.sendall(data)
	except Exception as e:
		raise e
	finally:
		logger.debug("Response have sent to "+connection)


def handle(connection, address):
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Connected %r at %r", connection, address)
        while True:
            data = connection.recv(1024)
            taskManager(data)
            logger.debug("Received data %r", data)
            # connection.sendall(data)
            # logger.debug("Sent data")
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()


	
class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):

        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Got connection")
            process = multiprocessing.Process(target=handle, args=(conn, address))
            
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)

def taskManager(param):
	in_head, in_data = '',''
	decode = ""
	__header__ = ['a','b','t','g']
	_len = len(param)

	if( _len <= 4):
		for h in range( _len ):
			if param[h] in __header__ :
				in_head = param[h] #sethead			
			else:
				in_data = in_data+param[h]	
				if h == _len-1:
					task(in_head, in_data)
	else: 	
		for h in range( _len ):
			if param[h] in __header__:
				in_data = '' #setdatanull
				in_head = param[h] #sethead				
			else:
				in_data = in_data+param[h]	

def task(in_head,in_data):
	
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
		gearHandler(in_data)

	else:
		raise

# STATUS 
CURRENT_GEAR = ""
CURRENT_SPEED = ""
CURRENT_WHEELS_ANGLES = ""

# MODE 
CONTROL_MODE = ""

def monitor():
	import time
	global CURRENT_SPEED
	global CURRENT_GEAR
	global CURRENT_WHEELS_ANGLES

	global CONTROL_MODE

	while True:
		print "current speed: ",CURRENT_SPEED
		print "current gear: ",CURRENT_GEAR
		print "currrent wheels angles: ",CURRENT_WHEELS_ANGLES
		print "\n"
		time.sleep(1)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)
    server = Server("", 7789)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")
