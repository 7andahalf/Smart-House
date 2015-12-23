import log,status,action
 
'''
This is the router script. It takes in incoming queries processes them
and returns the result to the server.
'''

def query(data):
	try:
		key, task, param = data.split("+")
		params = param.split("-")
		if not status.auth(key):
			return ['error', 'AUTH failed']
	except:
		return ['error', 'improper API format']

	if task == 'get_status':
		pass

	# etc tasks to be added

	return ['OK']

# Test cases
if __name__ == "__main__":
    print query('124#sh+skek+gbds-dg')

