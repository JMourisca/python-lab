# Complete the plusMinus function below.
def plusMinus(arr):
    plus = 0.0
    minus = 0.0 
    zero = 0.0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1
    
    total = len(arr)
    print("%2.6f" % (plus / total))
    print("%2.6f" % (minus / total))
    print("%2.6f" % (zero / total))


a = [-4, 3, -9, 0, 4, 1]
plusMinus(a)