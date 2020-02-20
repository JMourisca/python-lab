import time

#arr = [1, 3, 3, 5, 6, 6, 7, 7, 8, 9, 9, 9, 15]
arr = list(range(1, 10000000))

target = arr[len(arr) - 1]
output = []
# linear time O(n)
def linearSearch(a, t):
    for i, data in enumerate(a):
        if data == target:
            return i
        if data > target:
            return -1

start = time.time()
print(linearSearch(arr, target))
print(time.time() - start)

def binarySearch(a, t):    
    def bs(a, lower, higher, t):
        while True:
            mid = (higher + lower) // 2
            
            if higher < lower:
                return -1 

            if a[mid] == target and (mid == 0 or target > a[mid - 1]):
                return mid

            if target > a[mid]:
                lower = mid + 1
            else:
                higher = mid - 1
    return bs(a, 0, len(a) - 1, t)

start = time.time()
print(binarySearch(arr, target))
print(time.time() - start)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


arr = list(range(1, 10000000))
length = 1000
i = 0
while i < length:
    num = arr[i]
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
    i += 1