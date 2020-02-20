#################
# Linear search #
#################

# Linearly search x in arr[]. If x is present  
# then return the index, otherwise return -1 
#   * Worst case: When the searched number is not in the array. The search will traverse all N elements of the array before returning -1,
#                 therefore, this algorithm runs with complexity of O(n)
def search(arr, n, x): 
    i = 0
    for i in range(i, n): 
        if (arr[i] == x): 
            return i 
    return -1
  
# Driver Code 
arr = [1, 10, 30, 15] 
x = 30
n = len(arr) 
print(x, "is present at index", search(arr, n, x)) 
  