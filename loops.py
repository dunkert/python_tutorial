
a,b = 0,1
fh = open('fibo.txt',"w")

# "while" loop
while b < 40:   
    fh.writelines(str(b)+"\n")
    a,b = b, b + a

fh.close()
print("Output done")

fh =  open('fibo.txt', "r")

# "for" loops using an iterator
for line in fh.readlines():
    print(line,end='')

print("\nOther for loop exmaples\n")
# Using "for" loops using range
for n in range(1,10):
    print(n)

print("\nAnother example")
for n in (1,2,3,4,5,7):
    print(n)

print("Program done!")