set1={}
for a in range(2,101):
    for b in range(2,101):
        set1.update({a**b:0})

print(len(set1))
