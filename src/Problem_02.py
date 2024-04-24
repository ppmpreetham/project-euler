def fib(n):
    return n+1 if n<2 else fib(n-1)+fib(n-2)

sum=0
for i in range(4_000_000):
    if fib(i)>4_000_000:
        break
    if fib(i)<4_000_000 and fib(i)%2==0:
        sum+=fib(i)
print(sum)
    