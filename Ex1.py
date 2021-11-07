def sum(n):
    return int((n+1)*n/2)

def fact1(n):
    sum=1
    for i in range(n):
        sum=sum*(i+1)
    return sum

def fact2(n):
    if n==1:
        return 1
    else:
        return n*fact2(n-1)

def fib1(k):
    f1 = 1
    f2 = 1
    if k==1 or k==2:return 1
    else:
        for i in range(k-2):
            f=f1+f2
            f1=f2
            f2=f
        return f

print(fib1(10))


