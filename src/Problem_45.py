def triangle(n):
    lst=[]
    for i in range(n):
        lst.append(i*(i+1)/2)
    return lst
def pentagonal(n):
    lst=[]
    for i in range(n):
        lst.append(i*(3*i-1)/2)
    return lst
def hexagonal(n):
    lst=[]
    for i in range(n):
        lst.append(i*(2*i-1))
    return lst

n=100000
print(set(triangle(n)).intersection(set(pentagonal(n))).intersection(set(hexagonal(n)))) 