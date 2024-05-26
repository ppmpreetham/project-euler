# Sum square
def sum_square(n):
    return n*(n+1)*(2*n+1)/6

def sum_nat(n):
    return n*(n+1)/2

print(sum_nat(100)**2-sum_square(100))