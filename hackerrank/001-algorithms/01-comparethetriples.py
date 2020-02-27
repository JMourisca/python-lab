def compareTriplets(a, b):
    at = 0
    bt = 0

    for i in range(0, 3):
        if a[i] > b[i]:
            at += 1
        elif a[i] < b[i]:
            bt += 1

    return at, bt

a = [5,6,7]
b = [3,6,10]
print(compareTriplets(a, b))

a = [17,28,30]
b = [99,16,8]
print(compareTriplets(a, b))