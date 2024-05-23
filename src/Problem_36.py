def ispalindrome(n):
    return 1 if str(n)==str(n)[::-1] else 0

def isdoublebasepalindrome(n):
    return 1 if ispalindrome(n) and ispalindrome(str(bin(n))[2::]) else 0

summ=0
for i in range(1_000_001):
    if isdoublebasepalindrome(i):
        summ+=i

print(summ)