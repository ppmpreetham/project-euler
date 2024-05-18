import math
from decimal import Decimal
def length(n: int) -> int:
    return math.ceil(math.log(n,10))+1

phi = ( 1 + Decimal(5).sqrt() ) / 2
phidash = phi-1

def fib(n: int) -> int:
    return int((phi**n - phidash**n) / Decimal(5).sqrt()) if n%2==0 else int((phi**n - phidash**n) / Decimal(5).sqrt())+1

for i in range(10000):
    if len(str(fib(i)))>=1000:
        print(i)
        break