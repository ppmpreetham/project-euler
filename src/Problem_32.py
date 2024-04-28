def fact(n):
    return n * fact(n-1) if n > 1 else 1

def sumfact(n):
    summ=0
    for i in str(n):
        summ+=fact(int(i))
    if summ==n:
        print(n)

for i in range(10000000):
    sumfact(i)