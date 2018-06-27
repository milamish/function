'''
usage:
 removeduplicates.py <astring>
 '''
import sys


#the following function removes all duplicates from the input string
def remove_duplicates(astring):
	newList = []
    #new empty list
	count = 0
    #variable to keep track of removed duplicates
	for ch in astring:
      #iterate over the string and append each character once into the empty list
		if ch not in newList:
			newList.append(ch)
		else:
			count += 1
            #increment the value of count each time a character is left out
	return(''.join(newList), count)
	

from docopt import docopt

args = docopt(__doc__, version = '1.0.0')

if __name__ == '__main__':
	remove_duplicates(str(args['<astring>']))

