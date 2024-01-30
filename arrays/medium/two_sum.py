def two_summ(arr,target):
    n=len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return "YES"
            
    return "NO"
arry=[1,2,4,3,3]
print(two_summ(arry,8))

# Time Complexity: O(n^2) two loops r iterating the array.
# Space Complexity:O(1)


def two_sum(arr,target):
    seen_num = set()
    for ele in arr:
        diff = target - ele
        if diff not in seen_num:
            seen_num.add(ele)
        else:
            return "yes"
    return "no"
arr=[1,2,4,3,3]
# print(two_sum(arr,8))

def two_summ(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<right):
        sum=arr[left] + arr[right]
        if sum == target:
            return "YES"
        elif sum < target:
            left += 1
        else:
            right -= 1
        
    return "NO"

arr=[1,2,4,3,3]
print(two_sum(arr,8))

















    
        