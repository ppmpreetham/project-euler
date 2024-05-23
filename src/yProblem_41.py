def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def pandigital(n):
    return 1 if len(set(list(str(n))))==len(list(str(n))) else 0

i=7654321
while 1:
   if isPrime(i) and pandigital(i) and len(str(i))<=7:
       print(i)
       break
   i-=1