__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"

from datetime import datetime
import os

def writeFibonaci(filename,max_int):
    a,b = 0,1
       
    try:
        fh = open(filename,"w")
        #While loop
        while b < max_int:   
            fh.writelines(str(b)+"\n")
            a,b = b, b + a

    except:
        print("Could not open ", filename)

    
def printFile(filename):
    # Conditional Statement
    if os.path.exists(filename):
        with open(filename,"r") as fh:
            try:
                for line in fh.readlines():
                    print(line,end='')
            except:
                    print("Could not open/read file:", filename)
                    exit()
    else:
        print("The following file named (",filename,")could not be found")




myFile = "fibo2.txt"

if os.path.exists(myFile):
    os.rename(myFile,myFile+"."+ datetime.now().strftime("%S%M%H%m%d%Y"))

writeFibonaci(myFile, 40)
printFile(myFile)
