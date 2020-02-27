def kangaroo(x1, v1, x2, v2):
    # if they have the same speed, since x2 > x1, v1 will never reach v2
    if v1 == v2: 
        return "NO"

    res = (x2 - x1) / (v1 - v2)
    resmod = (x2 - x1) % (v1 - v2)
     
    if res < 0:
        return "NO"
    else:
        if resmod == 0:
            return "YES"
        
    return "NO"

print(kangaroo(0, 2, 5, 3))
print(kangaroo(0, 3, 4, 2))
print(kangaroo(21, 6, 47, 3))