def weirdness(n):
    if (n % 2 != 0) or (n in range(6, 21)):
        print('Weird')
    else:
        print('Not Weird')

for i in range(-5, 25):
    print(i, end=" - ")
    weirdness(i)