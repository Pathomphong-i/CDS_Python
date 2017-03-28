def taskManager(param):
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
					task(in_head, in_data)
					#print 'decode:' +in_head +in_data
				## decode done

	else: 
	
		for h in range( _len ):
			#print param[h]
			
			if param[h] in __header__:
				#print 'decode :'+in_head +in_data
				task(in_head, in_data) 
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
		g= str(in_data)
		global gear
		gear = g
		#input_status(in_head,g)
	else:
		raise
	

