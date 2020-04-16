__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


def writeFibonaci(filename,max_int):
    a,b = 0,1
    fh = open(filename,"w")

    #While loop
    while b < max_int:   
        fh.writelines(str(b)+"\n")
        a,b = b, b + a

def printFile(filename):
    fh = open(filename)
    for line in fh.readlines():
        print(line,end='')


writeFibonaci("fibo2.txt", 40)
printFile("fibo2.txt")
