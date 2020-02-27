def diagonalDifference(arr):
    firstd = 0
    secondd = 0
    size = len(arr)
    for i in range(size):
        firstd += arr[i][i]
        secondd += arr[i][size - 1 - i]

    return abs(firstd - secondd)


a = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDifference(a))