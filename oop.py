__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"



# Pi series
class series():
	def __init__(self):
	 super().__init__()
	 self.sum = 0
	 self.i = 1.0; 
	 self.j = 1

	def pi_series(self):
		while(1):
			self.sum = self.sum + self.j/self.i
			yield 4 * self.sum
			self.i = self.i + 2; self.j = self.j * -1
    

i = 0
p = series()

for n in p.pi_series():
    print(n)
    i += 1
    if i > 30:
        break 

