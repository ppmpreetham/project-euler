lst=0
for i in range(100):
    for j in range(100):
        if i**j > lst:
            lst = i**j

print(sum([int(x) for x in str(lst)]))