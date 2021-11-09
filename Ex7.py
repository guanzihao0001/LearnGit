def draw_front(size):
    for i in range(2*size-1):
        for j in range(2*size-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("/",end="")
        print("{:^s}".format("**"),end="")
        for j in range(i+1):
            print("{:^s}".format("\\"),end="")
        print("")
def draw_middle(size):
    print("+",end="")
    for i in range(size):
        print("=*=*",end="")
    print("+")
    for i in range(size):
        print("|", end="")
        for j in range(size-i-1):
            print(".",end="")
        for j in range(i+1):
            print("/\\",end="")
        for j in range(size-i-1):
            print("..", end="")
        for j in range(i+1):
            print("/\\",end="")
        for j in range(size-i-1):
            print(".",end="")
        print("|", end="")
        print("")
    for i in range(size):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(size-i):
            print("\\/",end="")
        for j in range(i):
            print('..',end="")
        for j in range(size-i):
            print("\\/",end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")
    print("+", end="")
    for i in range(size):
        print("=*=*", end="")
    print("+")
    for i in range(size):
        print("|",end="")
        for j in range(i):
            print(".", end="")
        for j in range(size-i):
            print("\\/",end="")
        for j in range(i):
            print('..',end="")
        for j in range(size-i):
            print("\\/",end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")
    for i in range(size):
        print("|", end="")
        for j in range(size-i-1):
            print(".",end="")
        for j in range(i+1):
            print("/\\",end="")
        for j in range(size-i-1):
            print("..", end="")
        for j in range(i+1):
            print("/\\",end="")
        for j in range(size-i-1):
            print(".",end="")
        print("|", end="")
        print("")
    print("+", end="")
    for i in range(size):
        print("=*=*", end="")
    print("+")

def draw_back(size):
    for i in range(2*size-2):
        for j in range(2*size-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("/",end="")
        print("{:^s}".format("**"),end="")
        for j in range(i+1):
            print("{:^s}".format("\\"),end="")
        print("")

def draw_rocket(size):
    draw_front(size)
    draw_middle(size)
    draw_back(size)

draw_rocket(2)