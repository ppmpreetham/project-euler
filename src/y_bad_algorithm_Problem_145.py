def count_reversible(limit):
    count = 0
    for i in range(1, limit):
        if i % 10 != 0 and (i + int(str(i)[::-1])) % 2 != 0:
            count += 1
    return count

limit = 10**9
reversible_count = count_reversible(limit)
print(reversible_count)