def recursive_fraction(n):
    flag=0
    flag+=1
    return 1/(1+recursive_fraction(n)) if flag!=n else n

recursive_fraction(12)
