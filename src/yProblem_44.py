def pentagonal_num(n):
    return int(n*(3*n-1)/2)

lst=[]

for i in range(100):
    lst.append(pentagonal_num(i))


def min_subarray(numbers):
    best_sum = -999
    current_sum = 0
    for i in numbers:
        current_sum = max(i, current_sum + i)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(min_subarray(lst))
