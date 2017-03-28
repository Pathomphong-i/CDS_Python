def taskManager(param):
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