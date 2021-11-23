print("enter the start value:",end="")
stv=int(input())
print("enter the end value:",end="")
edv=int(input())
print("Celsius Farenheit")
for i in range(stv,edv+1):
    print("{:^10d}".format(i),"{:^.2f}".format(1.8*i+32))