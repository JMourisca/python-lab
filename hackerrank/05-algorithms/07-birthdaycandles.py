def birthdayCakeCandles(ar):
    maxcandle = max(ar)
    ar.sort()
    ar.reverse()
    count = 0
    for i in ar:
        if i < maxcandle:
            break
        count+=1
    return count



a = [3, 2, 1, 3]
print(birthdayCakeCandles(a))