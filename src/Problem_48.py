def self_power_sum(x):
    summ=0
    for i in range(1,x+1):
        summ+=i**i
    return summ

print(self_power_sum(1000))