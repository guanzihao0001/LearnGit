import Ex1

print("enter a positive integer or 0 to exit:",end="")
cur = int(input())
while (cur != 0):
    print("The ",cur,"st Fibonacci number is",Ex1.fib1(cur))
    print(" ")
    print("enter a positive integer or 0 to exit:",end="")
    cur=int(input())
