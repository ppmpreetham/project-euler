constant=''
for i in range(1_000_000):
    constant+=str(i)

answer=1
for i in range(1,7):
    answer*=int(constant[10**i])

print(answer)