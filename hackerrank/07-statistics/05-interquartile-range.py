from statistics import median

def quartiles(x):
    l = len(x)
    l1 = int(l/2) 
    
    q1 = median(x[0:l1])
    q2 = median(x)
    if l % 2 == 0:
        q3 = median(x[l1:])
    else:
        q3 = median(x[l1+1:])
    return q1, q2, q3

t = "6"
x_i = "10 40 30 50 20 10 40 30 50 20"
f_i = "1 2 3 4 5 6 7 8 9 10"

x = list(map(lambda x: int(x), x_i.split(" ")))
f = list(map(lambda x: int(x), f_i.split(" ")))
s = []
for i, j in zip(x, f):
    for t in range(j):
        s.append(i)

s.sort()
q1, q2, q3 = quartiles(s)
print("{:.1f}".format(q3 - q1))