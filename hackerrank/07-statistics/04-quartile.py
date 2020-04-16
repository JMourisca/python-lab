from statistics import median

def quartiles(x_i):
    x = list(map(lambda x: int(x), x_i.split(" ")))
    x.sort()
    l = len(x)
    l1 = int(l/2) 
    
    q1 = median(x[0:l1])
    q2 = median(x)
    if l % 2 == 0:
        q3 = median(x[l1:])
    else:
        q3 = median(x[l1+1:])
    print(int(q1))
    print(int(q2))
    print(int(q3))

n = int("9") # "9" to be replaced by input()
x1 = "3 7 8 5 12 14 21 13 18"
x2 = "4 17 7 14 18 12 3 16 10 4 4 12"
quartiles(x1)
print("----")
quartiles(x2)