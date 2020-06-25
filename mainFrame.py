from fields import field

def method(master, argument):
	return field(master, methodName(argument))

def methodName(argument):
	methods= ['area', 'distance', 'mass', 'volume', 'energy', 'temperature']
	return methods[argument]

