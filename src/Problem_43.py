def isPanDigital(num):
    counter=0
    string = str(num)
    for i in range(7):
        if int(string[1+i:4+i])%[2, 3, 5, 7, 11, 13, 17][i]==0:
            counter+=1
    return True if counter==7 else False

total=0
for i in range(1000000000,9999999999):
    if isPanDigital(i):
        total+=i

print(total)