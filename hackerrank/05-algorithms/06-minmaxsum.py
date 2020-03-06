def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]), sum(arr[-4:]))

a = [1, 3, 5, 7, 9]
miniMaxSum(a)

a = [1, 2, 3, 4, 5]
miniMaxSum(a)

a = [5, 4, 1, 3, 2]
miniMaxSum(a)