#the following function takes a string as input and reverses it
def reverse(astring):
#time complexity is O(n), code does not depend on the size of input
	if not isinstance(astring, str):

		raise TypeError('input must be a string')
		
	return astring[::-1]
	