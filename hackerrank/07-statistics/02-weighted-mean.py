n = 5
x_i = "10 40 30 50 20"
w_i = "1 2 3 4 5"

x = list(map(lambda x: int(x), x_i.split(" ")))
w = list(map(lambda x: int(x), w_i.split(" ")))

sum_w = 0
sum = 0
while n > 0:
    i = n - 1
    sum += (x[i] * w[i])
    sum_w += w[i]
    n -= 1

print('{:.1f}'.format(sum/sum_w))