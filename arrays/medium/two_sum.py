def two_sum(arr,target):
    for i in range(0, n):
        for j in range(1, n):
            if arr[i] + arr[j] == target:
                return "YES"
            
    return "NO"
arr=[1,2,4,3,3]
n=len(arr)
print(two_sum(arr,6))

# Time Complexity: O(n^2) two loops r iterating the array.

# Space Complexity:O(1)

