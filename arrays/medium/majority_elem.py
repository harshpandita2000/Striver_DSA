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

# arr = [2,2,1,1,1,2,2]
# print(majorityElement(arr))

# TC: O(nlogn) coz insertion tc of dicttionary is logn and we r running loop for n times ..
# SC:: O(n)

def moore(arr):
    n = len(arr)
    ele = None
    cnt = 0
    count = 0
    for i in range(n):
        if cnt == 0:
            ele = arr[i]
        if arr[i] == ele:
            cnt+=1
        else:
            cnt -= 1   
    for i in arr:
        if i == ele:
            count += 1
    if count > n//2:
        return ele
    else:
        return None
    
arr = [2,2,1,1,1,2,2,2,1]
print(f"majority element is:{moore(arr)} ")
# TC:O(n)+O(n)=O(n)
# SC:O(1)