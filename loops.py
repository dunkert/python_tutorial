__author__ = "Daniel Jean-Baptiste"
__copyright__ = "Copyright 2017, The Smarter Engineering Project"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Jean-Baptiste"
__status__ = "Production"


# For loops examples

for n in (1,2,3,4,5,6):
	print(n)

print("")

for n in range(1,6):
	print(n)

print("")

for n in ["apple", "banana", "orange"]:
	print(n)

print("")

fruits = ["apple", "banana", "orange"]
for n in fruits:
	print(n)
else:
	print("Ther is no more fruits")

print("")

for x in range(1,6):
	for y in range(1,6):
		print("* ",end='')
	print("")

print("")
# Let's create a few simple examples using 'while' loops.



# while loop
i = 1
while i < 6:
	print(i)
	i+=1

print("")

i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

print("")

a,b = 0,1

filename = "fibo.txt"
fh = open(filename,"w")

while b < 40:
	print("Writting the value ",b," in", filename)
	fh.writelines(str(b)+"\n")
	a,b = b, b + a

fh.close()

print("")

fh = open(filename, "r")

print("Reading the file:", filename)
# 'for' loops using an iterator
for line in fh.readlines():
	print(line,end='')