def binomial(n,m):
    result=1
    for i in range(m):
        result*=(n-i)/(i+1)
    return result

number=0

for n in range(1,101):
    for r in range(n+1):
        if binomial(n,r)>1_000_000:
            number+=1

print(number)