__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


# Pi series
def pi_series():
	sum = 0
	i = 1.0; j = 1
	while(1):
		sum = sum + j/i
		yield 4*sum
		i = i + 2; j = j * -1
    
i = 0

for n in pi_series():
    print(n)
    i += 1
    if i > 30:
        break 

