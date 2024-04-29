side=1001

def minSqrLess(x):
    num=1
    i=0
    while 1:
        i+=1
        if i%2!=0 and i**2<=x:
            num=i
        if i**2>x:
            break
    return num

def sumEdge(n):
    return (n**2)+(n**2-(n-1))+(n**2-2*(n-1))+(n**2-3*(n-1))

summ=1
for i in range(3,minSqrLess(side**2)+1)[::2]:
    summ+=sumEdge(i)

print(summ)
