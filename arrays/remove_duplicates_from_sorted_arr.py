def removeDuplicatesArray(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

arr = [1, 2, 2, 3, 4]
k = removeDuplicatesArray(arr)
for i in range(k):
    print(arr[i],end=" ")

# TC:O(n) 
# SC:O(1) 