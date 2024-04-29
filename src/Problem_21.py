def d(n):
    summ=0
    for i in range(1,n):
        if n%i==0:
            summ+=i
    return summ

def amicable(n):
    a = d(n)
    if d(n)==n:
        return 0
    if d(a)==n:
        return 1
    return 0

flag=[]
for i in range(1,10000):
    if amicable(i):
        flag.append(i)

print(sum(flag))