# Narcissistic numbers are numbers that are equal to the sum of their digits raised to the power of the number of digits. For example, 9474 is a narcissistic number because 9^4 + 4^4 + 7^4 + 4^4 = 9474. Find the sum of all 5-digit narcissistic numbers.

def power_5(num):
    summ=0
    for i in str(num):
        summ+=int(i)**5
    return summ

total=0
for i in range(2,9999999):
    if i==power_5(i):
        total+=i
        # print(i)
print(total)