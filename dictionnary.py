__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


def main():
    mydicti =  {'apple':2, 'orange':1, 'pear':3, 'salad':4}
    
    print("dictionary keys:")
    for k in mydicti.keys():
        print("keys ",k)

    print("dictionary values")
    for v in mydicti.values():
        print(v)
    print("")

    print("Search for a pear")

    print("Found a pear:",mydicti.get("pear"))

    print("Sorting the keys")
    for k in sorted(mydicti.keys()):
        print(k)

    mydicti.clear()


if __name__ == "__main__": main()