def prime_no(n):
    prime = []
    for i in range(2, n+1):
        if i == 2:
            prime.append(i)
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                elif j == i-1:
                    prime.append(i)
    return prime

print(prime_no(200000)[10001])