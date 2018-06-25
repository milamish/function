
'''usage:
    isogram.py <word>
'''


import sys




def is_isogram(astring):
  
  if not astring:
    
    print('Empty string not a valid isogram')

    return(astring, False)

  elif len(astring) == len(set(astring)):

    
    return (astring, True)

  else:
    
    return (astring, False)
  
  
  if not isinstance(astring, str):
    
    raise TypeError('Argument should be a string')
    
    return (astring, False)

from docopt import docopt

args = docopt(__doc__, sys.argv[1])




if __name__ == '__main__':

  is_isogram(str(args['<word>']))


  

  


