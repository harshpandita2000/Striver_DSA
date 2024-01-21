def majorityElement(arr):
    n = len(arr)
    counts = {}

    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    for element, count in counts.items():
        if count > n // 2:
            return element

    return -1

arr = [2,2,1,1,1,2,2]
print(majorityElement(arr))

# TC: O(n)
# SC: O(n)