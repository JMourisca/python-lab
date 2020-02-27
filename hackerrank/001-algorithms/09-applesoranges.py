
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countA = 0
    for ap in apples:
        if ap + a >= s and ap + a <= t:
            countA += 1 
    
    countO = 0
    for o in oranges:
        if o + b >= s and o + b <= t:
            countO += 1
    print(countA)
    print(countO)



s = 7 # integer, starting point of Sam's house location.
t = 11 # integer, ending location of Sam's house location.
a = 5 # integer, location of the Apple tree.
b = 15 # integer, location of the Orange tree.
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)


s = 7 # integer, starting point of Sam's house location.
t = 10 # integer, ending location of Sam's house location.
a = 4 # integer, location of the Apple tree.
b = 12 # integer, location of the Orange tree.
apples = [2, 3, -4]
oranges = [3, -2, -4]

countApplesAndOranges(s, t, a, b, apples, oranges)