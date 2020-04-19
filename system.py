__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


import sys
import os
import datetime

def main():
    print("Python version ().{}.{}".format(*sys.version_info))
    print(sys.platform)
    print(sys.api_version)
    print(os.name)
    print("Your path is")
    print(os.getenv("PATH"))

    print("The current path is ",os.getcwd())
    
    print("\nThe file in your diretory are:")
    for f in os.listdir():
        print(datetime.datetime.now(),"-",f)


if __name__ == "__main__" : main()