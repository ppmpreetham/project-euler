def sum_digit(n):
    flag=0
    string=str(n)
    for i in range(len(string)):
        flag+=int(string[i])
    return flag

def s(n):
    i=1
    while 1:
        if sum_digit(i)==n:
            return i
        else:
            i+=1

def S(k):
    result=0
    for i in range(1,k+1):
        result+=s(i)
    return result

def fib(n):
    return n if n<2 else fib(n-1)+fib(n-2)

from time import time
a=time()
result=0
for i in range(90):
    result+=S(fib(i))
    print(result)
    b=time()
    print(b-a)

