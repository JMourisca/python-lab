import math

n = int("5") # replace 5 for input()
x_i = "10 40 30 50 20"

x = list(map(lambda x: int(x), x_i.split(" ")))

print(x)

# Calculate mean
mean = sum(x) / len(x)

variance = sum(list(map(lambda v: ((v - mean)**2)/len(x) , x)))
standard_deviaton = math.sqrt(variance)

print('{:.1f}'.format(standard_deviaton))