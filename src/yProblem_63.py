def n_power(n):
    i=1
    while 1:
        if len(str(i**n))==n:
            # print(f"{i}^{n},{str(i**n)}")
            return 1
        elif len(str(i**n))>n:
            return 0
        else:
            i+=1

total=0 
for i in range(10000):
    if n_power(i):
        total+=1

print(total)