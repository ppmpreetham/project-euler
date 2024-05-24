def to_set(n):
    return set(list(map(list,str(n).split()))[0])

def Permuted_multiple(n):
    if to_set(n)==to_set(2*n)==to_set(3*n)==to_set(4*n)==to_set(5*n)==to_set(6*n):
        return 1
    return 0

i=1
while 1:
    if Permuted_multiple(i)==1:
        print(i)
        break
    else:
        i+=1