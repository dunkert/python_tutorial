__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


import re

myList = ["The year is 1999","The year is 2000","The year is 1998","The year is 1997","The year is 2001","The year is 2002"]

for i in sorted(myList):
    print(i)

for i in sorted(myList):
    if re.search("(20??)",i):
        print(i)
else:
    print("Nothing else to find")

print("\nSearch for the occurence of 'e' in ", myList[0])

print(re.findall("e",myList[0]))

print(re.sub("bad","good","This is very bad"))

print(re.split("\s","This is a very long text"))




