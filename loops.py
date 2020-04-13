
a,b = 0,1
fh = open('fibo.txt',"w")

#While loop
while b < 40:   
    fh.writelines(str(b)+"\n")
    a,b = b, b + a

fh.close()
print("Output done")

fh =  open('fibo.txt', "r")
# For loops
for line in fh.readlines():
    print(line,end='')

print("Program done!")