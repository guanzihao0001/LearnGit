print("enter the target unit('C' or 'F'):",end="")
T=input()
while(T!="C" and T!="F"):
    print("enter the target unit('C' or 'F'):", end="")
    T = input()
print("enter the start value:",end="")
stv=int(input())
print("enter the end value:",end="")
edv=int(input())


print("")
if T== "F":
    print("Celsius Farenheit")
    if stv>edv:
        for i in range(stv,edv-1,-1):
            print("{:^10d}".format(i), "{:^.2f}".format(1.8 * i + 32))
    else:
        for i in range(stv,edv):
            print("{:^10d}".format(i), "{:^.2f}".format(1.8 * i + 32))
elif T=="C":
    print("Farenheit Celsius")
    if stv > edv:
        for i in range(stv, edv - 1, -1):
            print("{:^10d}".format(i), "{:^.2f}".format((i - 32)/1.8))
    else:
        for i in range(stv, edv):
            print("{:^10d}".format(i), "{:^.2f}".format((i - 32) / 1.8))