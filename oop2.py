__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"

class Animal:
	def speak(self): return self.sound
	def legs(self): return  self.number_of_legs
	def name(self): return self.name

class duck(Animal):
	sound = "quacks"
	legs =  "2 legs"
	name = "duck"

class human(Animal):
	sound = "speaks"
	legs = "2 legs"
	name =  "human"

class dog(Animal):
	sound = "barks"
	legs = "4 legs"
	name =  "dog"


def main():
	print("Starting program")
	dg = dog()
	hm = human()
	dk = duck()

	for n in (dg, hm , dk):
		print("A {} has {} and {}".format(n.name, n.legs, n.sound))

if __name__ == "__main__": main()